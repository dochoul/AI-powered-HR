from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.models.database import Base


class UserSlackMapping(Base):
    __tablename__ = "user_slack_mapping"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    employee_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("employees.id"), unique=True, nullable=False
    )
    slack_user_id: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )

    employee: Mapped["Employee"] = relationship(back_populates="slack_mapping")
