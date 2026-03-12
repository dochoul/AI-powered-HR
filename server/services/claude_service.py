import json
import logging

import anthropic

from server.config import settings
from server.tools.hr_tools import TOOLS

logger = logging.getLogger(__name__)

client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)

SYSTEM_PROMPT = """당신은 A회사의 인사정보 조회 챗봇입니다.

역할:
- 직원의 기본 인사정보(이름, 부서, 직급, 직책, 입사일, 이메일, 연락처)를 조회합니다.
- 부서별 소속 직원 목록을 제공합니다.
- 직급별 직원 목록을 제공합니다.
- 경영진/HR 담당자에게 연봉 정보(개인 연봉, 부서별 평균 연봉)를 제공합니다.

규칙:
- 연봉 정보는 기밀 등급입니다. 경영진 또는 HR 담당자 권한이 확인된 경우에만 조회합니다.
- 연봉 조회 시 응답에 "기밀 정보이므로 조회 이력이 기록됩니다" 안내를 포함합니다.
- 급여 명세서, 인사평가, 근태, 주민등록번호, 계좌번호 관련 질문에는 "현재 조회할 수 없는 정보"라고 안내합니다.
- HR과 관련 없는 질문에는 인사정보 조회 챗봇임을 안내하고 예시 질문을 제공합니다.
- 응답은 간결하고 정확하게, 존댓말(합니다체)로 작성합니다.
- 개인적인 의견이나 추측을 포함하지 않습니다.
- 동명이인이 있을 경우 목록을 제시하고 선택을 요청합니다.
- 근속년수를 계산할 때 오늘 날짜를 기준으로 합니다.
- 부서 인원이 20명을 초과하면 상위 직급부터 20명만 표시하고 "외 N명이 더 있습니다"로 안내합니다.
"""


async def chat_with_tools(user_message: str) -> anthropic.types.Message:
    """Claude API에 메시지를 보내고 Tool Use 응답을 받는다"""
    response = await client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        tools=TOOLS,
        messages=[{"role": "user", "content": user_message}],
    )
    return response


async def chat_with_tool_result(
    user_message: str,
    assistant_message: anthropic.types.Message,
    tool_use_id: str,
    tool_result: str,
) -> anthropic.types.Message:
    """Tool 실행 결과를 Claude에 전달하여 최종 응답을 받는다"""
    response = await client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        tools=TOOLS,
        messages=[
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": assistant_message.content},
            {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": tool_use_id,
                        "content": tool_result,
                    }
                ],
            },
        ],
    )
    return response
