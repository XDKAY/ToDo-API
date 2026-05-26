from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from app.src.core.models.user import UserInputModel

from .dependencies import UserServiceDP

router = APIRouter(prefix="/users", tags=["Users 👥"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserInputModel, user_service: UserServiceDP):
    existing_user = (await user_service.get_user_by_username(user.username)) or (
        await user_service.get_user_by_email(user.email)
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The user with this username and email already exists",
        )

    await user_service.add_user(user)

    return {"message": "User registered successfully", "user": user}
