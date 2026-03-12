from datetime import date, datetime

from sqlalchemy import BigInteger, Date, DateTime, Enum, ForeignKey, Index, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.models.database import Base


class Employee(Base):
    __tablename__ = "employees"
    __table_args__ = (
        Index("idx_employees_name", "name"),
        Index("idx_employees_department", "department_id", "status"),
        Index("idx_employees_position", "position_id", "status"),
        Index("idx_employees_hire_date", "hire_date"),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    phone: Mapped[str | None] = mapped_column(String(20))
    birth_date: Mapped[date | None] = mapped_column(Date)
    hire_date: Mapped[date] = mapped_column(Date, nullable=False)
    resign_date: Mapped[date | None] = mapped_column(Date)
    status: Mapped[str] = mapped_column(
        Enum("active", "on_leave", "resigned", name="employee_status"),
        nullable=False,
        server_default="active",
    )
    department_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("departments.id"), nullable=False
    )
    position_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("positions.id"), nullable=False
    )
    title: Mapped[str | None] = mapped_column(String(50))
    annual_salary: Mapped[int | None] = mapped_column(BigInteger)
    salary_updated_at: Mapped[datetime | None] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now()
    )

    department: Mapped["Department"] = relationship(back_populates="employees")
    position: Mapped["Position"] = relationship(back_populates="employees")
    slack_mapping: Mapped["UserSlackMapping | None"] = relationship(back_populates="employee")
    roles: Mapped[list["EmployeeRole"]] = relationship(back_populates="employee")
