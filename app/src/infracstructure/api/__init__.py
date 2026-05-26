from fastapi import APIRouter

from .users import router as users_router

routers = APIRouter(prefix="/api")

routers.include_router(users_router)
