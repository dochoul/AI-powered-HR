"""슬랙 없이 챗봇 핵심 로직을 테스트하기 위한 HTTP 엔드포인트

사용법:
  POST /api/chat
  {
    "slack_user_id": "U_CEO_001",
    "message": "홍길동 정보 알려줘"
  }
"""
import json
import logging

from fastapi import APIRouter
from pydantic import BaseModel

from server.models.database import async_session
from server.services.auth_service import authenticate_slack_user, can_access_confidential
from server.services.audit_service import log_audit
from server.services.llm_service import chat_with_tools, chat_with_tool_result
from server.services import hr_data_service
from server.tools.hr_tools import CONFIDENTIAL_TOOLS

logger = logging.getLogger(__name__)

router = APIRouter()

TOOL_HANDLERS = {
    "get_employee_by_name": hr_data_service.get_employee_by_name,
    "get_employees_by_department": hr_data_service.get_employees_by_department,
    "get_employees_by_position": hr_data_service.get_employees_by_position,
    "get_recent_hires": hr_data_service.get_recent_hires,
    "get_employee_salary": hr_data_service.get_employee_salary,
    "get_department_salary_stats": hr_data_service.get_department_salary_stats,
}


class ChatRequest(BaseModel):
    slack_user_id: str
    message: str


class ChatResponse(BaseModel):
    success: bool
    response: str
    tool_used: str | None = None
    security_level: str = "general"


@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    async with async_session() as session:
        # 1. 인증/권한 확인
        auth = await authenticate_slack_user(session, req.slack_user_id)
        if not auth.authorized:
            if auth.employee_id:
                await log_audit(
                    session,
                    requester_id=auth.employee_id,
                    action="unauthorized_access",
                    query_text=req.message,
                    result_status="unauthorized",
                )
            return ChatResponse(success=False, response=auth.error_message)

        # 2. Gemini API 호출 (의도 분석 + Function Calling)
        try:
            llm_response = await chat_with_tools(req.message)
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                return ChatResponse(
                    success=False,
                    response="API 호출 한도를 초과했습니다. 잠시 후 다시 시도해 주세요.",
                )
            return ChatResponse(
                success=False,
                response="일시적인 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.",
            )

        # 3. Tool Call이 없으면 텍스트 응답 직접 전송
        if not llm_response.tool_name:
            await log_audit(
                session,
                requester_id=auth.employee_id,
                action="no_tool_call",
                query_text=req.message,
                result_status="success",
            )
            return ChatResponse(success=True, response=llm_response.text or "")

        tool_name = llm_response.tool_name
        tool_args = llm_response.tool_args

        # 4. 기밀 등급 이중 검증
        security_level = "general"
        if tool_name in CONFIDENTIAL_TOOLS:
            if not can_access_confidential(auth.role):
                await log_audit(
                    session,
                    requester_id=auth.employee_id,
                    action=f"{tool_name}_unauthorized",
                    query_text=req.message,
                    result_status="unauthorized",
                    security_level="confidential",
                )
                return ChatResponse(
                    success=False,
                    response="죄송합니다. 연봉 정보는 조회 권한이 없습니다.\n급여 관련 문의는 HR팀에 직접 문의해 주세요.",
                    security_level="confidential",
                )
            security_level = "confidential"

        # 5. DB 조회
        handler = TOOL_HANDLERS.get(tool_name)
        if not handler:
            return ChatResponse(success=False, response="일시적인 오류가 발생했습니다.")

        tool_result = await handler(session, **tool_args)
        tool_result_str = json.dumps(tool_result, ensure_ascii=False, default=str)

        # 6. Gemini에 결과 전달 → 최종 자연어 응답
        final_text = await chat_with_tool_result(
            user_message=req.message,
            tool_name=tool_name,
            tool_args=tool_args,
            raw_parts=llm_response._raw_parts,
            tool_result=tool_result_str,
        )

        # 7. 감사 로그
        result_count = len(tool_result) if isinstance(tool_result, list) else (1 if tool_result else 0)
        await log_audit(
            session,
            requester_id=auth.employee_id,
            action=tool_name,
            query_text=req.message,
            result_status="success" if tool_result else "not_found",
            result_count=result_count,
            security_level=security_level,
        )

        return ChatResponse(
            success=True,
            response=final_text,
            tool_used=tool_name,
            security_level=security_level,
        )
