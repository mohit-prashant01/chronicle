from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user import User
from app.schemas.user import UserCreate

from app.utils.security import (hash_password,verify_password)

from app.utils.token import create_access_token


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
    

async def login_user(payload,db):
    query=select(User).where(User.email==payload.email)

    result=await db.execute(query)

    user=result.scalar()

    if not user:
        raise ValueError("Invalid Credentials")
    

    valid = verify_password(payload.password,user.password_hash)
    if not valid:
        raise ValueError("Invalid Credentials")
    

    token = create_access_token(user.id)

    return {
        "access_token":token,
        "token_type":"bearer"
    }