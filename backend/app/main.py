from fastapi import FastAPI
from sqlalchemy import text


from app.db.database import engine

app = FastAPI(
    title="Chronicle API"
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