from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Enum, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.models.database import Base


class EmployeeRole(Base):
    __tablename__ = "employee_roles"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    employee_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("employees.id"), nullable=False
    )
    role: Mapped[str] = mapped_column(
        Enum("executive", "hr_admin", "manager", "employee", name="role_type"),
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )

    employee: Mapped["Employee"] = relationship(back_populates="roles")
