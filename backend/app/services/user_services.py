from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password


async def create_user(
        payload:UserCreate,
        db:AsyncSession
):
    query= select(User).where(
        User.email==payload.email
    )

    existing = await db.execute(
        query
    )

    if existing.scalar():
        raise ValueError(
            "Email already exists"
        )
    
    user = User(
        username = payload.username,
        email=payload.email,
        password_hash=hash_password(
            payload.password
        )
    )


    db.add(user)

    await db.commit()

    await db.refresh(
        user
    )

    return user
    