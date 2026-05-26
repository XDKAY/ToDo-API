from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.src.infracstructure.api import routers
from app.src.infracstructure.db.database import connect_database, disconnect_database


@asynccontextmanager
async def lifespan(_: FastAPI):
    await connect_database()
    yield
    await disconnect_database()


app = FastAPI(lifespan=lifespan)
app.include_router(routers)
