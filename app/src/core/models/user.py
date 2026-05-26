from typing import Annotated, Self
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

from app.src.core.security.hashing import hash_password


class UserInputModel(BaseModel):
    username: Annotated[str, Field(..., min_length=3, max_length=20)]
    email: EmailStr
    password: Annotated[str, Field(..., min_length=8)]

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        if not value.isalnum():
            raise ValueError("Username must be alphanumeric")
        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if not any(c.islower() for c in value):
            raise ValueError("Password must contain at least one lowercase letter")

        if not any(c.isupper() for c in value):
            raise ValueError("Password must contain at least one uppercase letter")

        if not any(c.isdigit() for c in value):
            raise ValueError("Password must contain at least one digit")

        return value


class UserUpdateModel(BaseModel):
    username: Annotated[str | None, Field(default=None, min_length=3, max_length=20)]
    email: EmailStr | None = None

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str | None) -> str | None:
        if value is not None and not value.isalnum():
            raise ValueError("Username must be alphanumeric")
        return value


class UserDTO(BaseModel):
    username: str
    email: str
    hashed_password: str

    @classmethod
    def from_input(cls, username: str, email: str, password: str) -> Self:
        return cls(
            username=username, email=email, hashed_password=hash_password(password)
        )


class UserResponseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: str
    email: str
    hashed_password: str = Field(exclude=True)
