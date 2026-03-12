from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.models.database import Base


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    parent_id: Mapped[int | None] = mapped_column(
        BigInteger, ForeignKey("departments.id"), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )

    employees: Mapped[list["Employee"]] = relationship(back_populates="department")
    parent: Mapped["Department | None"] = relationship(remote_side=[id])
