from datetime import datetime
from uuid import UUID

from sqlalchemy import ARRAY, ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column

from app.src.infracstructure.db.base import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    userd_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    title: Mapped[str]
    description: Mapped[str]

    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    is_complated: Mapped[bool] = mapped_column(default=False)
    compalted_at: Mapped[datetime | None] = mapped_column(default=None)

    tags: Mapped[list[str]] = mapped_column(ARRAY(String))
