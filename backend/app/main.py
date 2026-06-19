from contextlib import asynccontextmanager


from fastapi import FastAPI


from app.db.base import Base
from app.db.database import engine
from app.schemas.user import UserCreate
from app.routers.auth import router as auth_router


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

app.include_router(
    auth_router
)

@app.get("/")
async def root()-> dict[str,str]:
    return{"message":"Chronicles API is running"}


@app.post("/validate-user")
async def validate_user(
    payload:UserCreate
):
    
    return {
        "validated_data":payload.model_dump()
    }