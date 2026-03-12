import logging

from sqlalchemy.ext.asyncio import AsyncSession

from server.models.audit_log import AuditLog

logger = logging.getLogger(__name__)


async def log_audit(
    session: AsyncSession,
    requester_id: int,
    action: str,
    query_text: str,
    result_status: str,
    target_employee_id: int | None = None,
    target_department_id: int | None = None,
    result_count: int | None = None,
    security_level: str = "general",
):
    """감사 로그 기록"""
    audit = AuditLog(
        requester_id=requester_id,
        action=action,
        target_employee_id=target_employee_id,
        target_department_id=target_department_id,
        query_text=query_text,
        result_status=result_status,
        result_count=result_count,
        security_level=security_level,
    )
    session.add(audit)
    await session.commit()
    logger.info(
        f"Audit: requester={requester_id} action={action} status={result_status} "
        f"security_level={security_level}"
    )
