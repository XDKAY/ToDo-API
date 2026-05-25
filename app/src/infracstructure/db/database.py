from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import settings

from .base import Base
from .models.task import Tasks
from .models.user import Users

engine = create_async_engine(settings.db.url)
session_local = async_sessionmaker(engine)


async def connect_database() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def disconnect_database() -> None:
    await engine.dispose()


async def get_db_session() -> AsyncGenerator[AsyncSession]:
    async with session_local() as session:
        yield session
        await session.commit()
