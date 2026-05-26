from uuid import UUID

from app.src.core.models.user import UserInputModel, UserResponseModel, UserUpdateModel
from app.src.core.repositories.user import AbstractUserRepository


class UserService:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    async def get_user_by_id(self, user_id: UUID) -> UserResponseModel | None:
        return await self.user_repo.get_by_id(user_id)

    async def get_user_by_username(self, username: str) -> UserResponseModel | None:
        return await self.user_repo.get_by_username(username)

    async def get_user_by_email(self, email: str) -> UserResponseModel | None:
        return await self.user_repo.get_by_email(email)

    async def add_user(self, user: UserInputModel):
        await self.user_repo.create(user)

    async def update_user(self, user_id: UUID, user: UserUpdateModel):
        await self.user_repo.update(user_id, user)

    async def delete_user(self, user_id: UUID):
        await self.user_repo.delete(user_id)
