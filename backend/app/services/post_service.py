from sqlalchemy.ext.asyncio import AsyncSession
from app.models.post import Post
from app.schemas.post import PostCreate
from sqlalchemy import (select)

async def create_post(
        payload:PostCreate,
        user_id:int,
        db:AsyncSession
):
    post=Post(title=payload.title,
              content=payload.content,
              owner_id=user_id)
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post


async def get_posts(db:AsyncSession):
    query=(select(Post).order_by(Post.created_at.desc()))
    result = await db.execute(query)
    return result.scalars().all()

async def get_post(post_id:int, db:AsyncSession):
    query=(select(Post).where(Post.id==post_id))
    result=await db.execute(query)
    post=result.scalar()
    return post