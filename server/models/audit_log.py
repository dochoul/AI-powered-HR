from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Enum, ForeignKey, Index, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from server.models.database import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"
    __table_args__ = (
        Index("idx_audit_logs_requester", "requester_id", "created_at"),
        Index("idx_audit_logs_created", "created_at"),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    requester_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("employees.id"), nullable=False
    )
    action: Mapped[str] = mapped_column(String(50), nullable=False)
    target_employee_id: Mapped[int | None] = mapped_column(
        BigInteger, ForeignKey("employees.id")
    )
    target_department_id: Mapped[int | None] = mapped_column(
        BigInteger, ForeignKey("departments.id")
    )
    query_text: Mapped[str] = mapped_column(Text, nullable=False)
    result_status: Mapped[str] = mapped_column(
        Enum("success", "not_found", "unauthorized", "error", name="result_status_type"),
        nullable=False,
    )
    result_count: Mapped[int | None] = mapped_column(Integer)
    security_level: Mapped[str] = mapped_column(
        Enum("general", "restricted", "confidential", name="security_level_type"),
        server_default="general",
    )
    ip_address: Mapped[str | None] = mapped_column(String(45))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )
