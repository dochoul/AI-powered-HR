import logging
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from server.models.employee import Employee
from server.models.employee_role import EmployeeRole
from server.models.user_slack_mapping import UserSlackMapping

logger = logging.getLogger(__name__)


@dataclass
class AuthResult:
    authorized: bool
    employee_id: int | None = None
    employee_name: str | None = None
    role: str | None = None
    error_message: str | None = None


# MVP에서 챗봇 접근 가능한 역할
CHATBOT_ALLOWED_ROLES = {"executive"}

# 기밀 등급(연봉) 조회 가능한 역할
CONFIDENTIAL_ALLOWED_ROLES = {"executive", "hr_admin"}


async def authenticate_slack_user(session: AsyncSession, slack_user_id: str) -> AuthResult:
    """슬랙 사용자 ID로 인증 및 권한 확인"""
    # 슬랙 ID → 직원 매핑 조회
    mapping_result = await session.execute(
        select(UserSlackMapping).where(UserSlackMapping.slack_user_id == slack_user_id)
    )
    mapping = mapping_result.scalar_one_or_none()

    if not mapping:
        return AuthResult(
            authorized=False,
            error_message="등록되지 않은 사용자입니다. 관리자에게 문의해 주세요.",
        )

    # 직원 정보 조회
    employee_result = await session.execute(
        select(Employee).where(Employee.id == mapping.employee_id)
    )
    employee = employee_result.scalar_one_or_none()

    if not employee:
        return AuthResult(
            authorized=False,
            error_message="등록되지 않은 사용자입니다. 관리자에게 문의해 주세요.",
        )

    # 역할 조회
    role_result = await session.execute(
        select(EmployeeRole).where(EmployeeRole.employee_id == employee.id)
    )
    role_record = role_result.scalar_one_or_none()

    if not role_record or role_record.role not in CHATBOT_ALLOWED_ROLES:
        return AuthResult(
            authorized=False,
            employee_id=employee.id,
            employee_name=employee.name,
            role=role_record.role if role_record else None,
            error_message="죄송합니다. 인사정보 조회 권한이 없습니다.\n필요하시면 HR팀에 문의해 주세요.",
        )

    return AuthResult(
        authorized=True,
        employee_id=employee.id,
        employee_name=employee.name,
        role=role_record.role,
    )


def can_access_confidential(role: str | None) -> bool:
    """기밀 등급 정보 접근 가능 여부"""
    return role in CONFIDENTIAL_ALLOWED_ROLES
