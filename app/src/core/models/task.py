from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class TaskInputModel(BaseModel):
    title: Annotated[str, Field(..., min_length=1, max_length=100)]
    description: Annotated[str, Field(..., min_length=1, max_length=500)]
    tags: Annotated[list[str], Field(default_factory=list)]


class TaskUpdateModel(BaseModel):
    title: Annotated[str | None, Field(default=None, min_length=1, max_length=100)]
    description: Annotated[
        str | None, Field(default=None, min_length=1, max_length=500)
    ]

    is_completed: bool | None = None
    tags: Annotated[list[str] | None, Field(default=None)]


class TaskResponseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: UUID
    title: str
    description: str

    created_at: datetime
    updated_at: datetime

    is_completed: bool
    completed_at: datetime | None

    tags: list[str]
