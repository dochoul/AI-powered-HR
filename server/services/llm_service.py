import json
import logging
from dataclasses import dataclass

from google import genai
from google.genai import types

from server.config import settings
from server.tools.hr_tools import GEMINI_TOOLS

logger = logging.getLogger(__name__)

client = genai.Client(api_key=settings.gemini_api_key)

MODEL = "gemini-2.5-flash"

SYSTEM_PROMPT = """당신은 A회사의 인사정보 조회 챗봇입니다.

역할:
- 직원의 기본 인사정보(이름, 부서, 직급, 직책, 입사일, 이메일, 연락처)를 조회합니다.
- 부서별 소속 직원 목록을 제공합니다.
- 직급별 직원 목록을 제공합니다.
- 연봉 정보(개인 연봉, 부서별 평균 연봉)를 조회합니다.

중요 규칙:
- 사용자가 질문하면 반드시 적절한 함수를 호출하여 데이터를 조회하세요. 데이터를 추측하지 마세요.
- 연봉 관련 질문이 들어오면 반드시 get_employee_salary 또는 get_department_salary_stats 함수를 호출하세요. 권한 검증은 서버가 처리하므로 당신이 판단하지 마세요.
- 연봉 조회 결과를 응답할 때 "기밀 정보이므로 조회 이력이 기록됩니다" 안내를 포함합니다.
- 급여 명세서, 인사평가, 근태, 주민등록번호, 계좌번호 관련 질문에는 "현재 조회할 수 없는 정보"라고 안내합니다.
- HR과 관련 없는 질문에는 인사정보 조회 챗봇임을 안내하고 예시 질문을 제공합니다.
- 응답은 간결하고 정확하게, 존댓말(합니다체)로 작성합니다.
- 개인적인 의견이나 추측을 포함하지 않습니다.
- 동명이인이 있을 경우 목록을 제시하고 선택을 요청합니다.
- 근속년수를 계산할 때 오늘 날짜를 기준으로 합니다.
- 부서 인원이 20명을 초과하면 상위 직급부터 20명만 표시하고 "외 N명이 더 있습니다"로 안내합니다.
"""


@dataclass
class LLMResponse:
    """LLM 응답 통합 구조"""
    text: str | None = None
    tool_name: str | None = None
    tool_args: dict | None = None
    _raw_parts: list = None  # Gemini 원본 parts (tool_result 전달용)


async def chat_with_tools(user_message: str) -> LLMResponse:
    """Gemini API에 메시지를 보내고 Function Calling 응답을 받는다"""
    response = await client.aio.models.generate_content(
        model=MODEL,
        contents=user_message,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=GEMINI_TOOLS,
        ),
    )

    # Function Call 확인
    part = response.candidates[0].content.parts[0]
    if part.function_call:
        return LLMResponse(
            tool_name=part.function_call.name,
            tool_args=dict(part.function_call.args),
            _raw_parts=response.candidates[0].content.parts,
        )

    return LLMResponse(text=part.text)


async def chat_with_tool_result(
    user_message: str,
    tool_name: str,
    tool_args: dict,
    raw_parts: list,
    tool_result: str,
) -> str:
    """Tool 실행 결과를 Gemini에 전달하여 최종 응답을 받는다"""
    tool_result_data = json.loads(tool_result)

    response = await client.aio.models.generate_content(
        model=MODEL,
        contents=[
            types.Content(role="user", parts=[types.Part.from_text(text=user_message)]),
            types.Content(role="model", parts=raw_parts),
            types.Content(
                role="user",
                parts=[
                    types.Part.from_function_response(
                        name=tool_name,
                        response={"result": tool_result_data},
                    )
                ],
            ),
        ],
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=GEMINI_TOOLS,
        ),
    )

    return response.text
