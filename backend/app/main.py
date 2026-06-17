from contextlib import asynccontextmanager


from fastapi import FastAPI
from sqlalchemy import text

from app.db.base import Base
from app.db.database import engine

import app.models

@asynccontextmanager
async def lifespan(app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )
    yield



app = FastAPI(
    title="Chronicle API",
    lifespan=lifespan
)

@app.get("/")
async def root()-> dict[str,str]:
    return{"message":"Chronicles API is running"}


@app.get("/health/db")
async def check_db():
    async with engine.begin() as conn:
        await conn.execute(
            text("SELECT 1")
        )

    return {
    "database":"connected"
    }