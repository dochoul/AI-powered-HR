import json
import logging

from server.models.database import async_session
from server.services.auth_service import authenticate_slack_user, can_access_confidential
from server.services.audit_service import log_audit
from server.services.llm_service import chat_with_tools, chat_with_tool_result
from server.services.slack_service import send_message
from server.services import hr_data_service
from server.tools.hr_tools import CONFIDENTIAL_TOOLS

logger = logging.getLogger(__name__)

TOOL_HANDLERS = {
    "get_employee_by_name": hr_data_service.get_employee_by_name,
    "get_employees_by_department": hr_data_service.get_employees_by_department,
    "get_employees_by_position": hr_data_service.get_employees_by_position,
    "get_recent_hires": hr_data_service.get_recent_hires,
    "get_employee_salary": hr_data_service.get_employee_salary,
    "get_department_salary_stats": hr_data_service.get_department_salary_stats,
}


async def handle_message(slack_user_id: str, text: str, channel: str):
    """메시지 수신 → 인증 → Gemini → DB 조회 → 응답 전송"""
    try:
        async with async_session() as session:
            # 1. 인증/권한 확인
            auth = await authenticate_slack_user(session, slack_user_id)
            if not auth.authorized:
                if auth.employee_id:
                    await log_audit(
                        session,
                        requester_id=auth.employee_id,
                        action="unauthorized_access",
                        query_text=text,
                        result_status="unauthorized",
                    )
                await send_message(channel, auth.error_message)
                return

            # 2. Gemini API 호출
            llm_response = await chat_with_tools(text)

            # 3. Tool Call이 없으면 텍스트 응답 직접 전송
            if not llm_response.tool_name:
                await log_audit(
                    session,
                    requester_id=auth.employee_id,
                    action="no_tool_call",
                    query_text=text,
                    result_status="success",
                )
                await send_message(channel, llm_response.text or "")
                return

            tool_name = llm_response.tool_name
            tool_args = llm_response.tool_args

            # 4. 기밀 등급 도구인 경우 권한 이중 검증
            security_level = "general"
            if tool_name in CONFIDENTIAL_TOOLS:
                if not can_access_confidential(auth.role):
                    await log_audit(
                        session,
                        requester_id=auth.employee_id,
                        action=f"{tool_name}_unauthorized",
                        query_text=text,
                        result_status="unauthorized",
                        security_level="confidential",
                    )
                    await send_message(
                        channel,
                        "죄송합니다. 연봉 정보는 조회 권한이 없습니다.\n급여 관련 문의는 HR팀에 직접 문의해 주세요.",
                    )
                    return
                security_level = "confidential"

            # 5. DB 조회 실행
            handler = TOOL_HANDLERS.get(tool_name)
            if not handler:
                logger.error(f"Unknown tool: {tool_name}")
                await send_message(channel, "일시적인 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.")
                return

            tool_result = await handler(session, **tool_args)
            tool_result_str = json.dumps(tool_result, ensure_ascii=False, default=str)

            # 6. Gemini에 Tool 결과 전달 → 자연어 응답 생성
            final_text = await chat_with_tool_result(
                user_message=text,
                tool_name=tool_name,
                tool_args=tool_args,
                raw_parts=llm_response._raw_parts,
                tool_result=tool_result_str,
            )

            # 7. 감사 로그 기록
            result_count = len(tool_result) if isinstance(tool_result, list) else (1 if tool_result else 0)
            await log_audit(
                session,
                requester_id=auth.employee_id,
                action=tool_name,
                query_text=text,
                result_status="success" if tool_result else "not_found",
                result_count=result_count,
                security_level=security_level,
            )

            # 8. 슬랙 응답 발송
            await send_message(channel, final_text)

    except Exception as e:
        logger.exception(f"Error handling message: {e}")
        await send_message(channel, "일시적인 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.")
