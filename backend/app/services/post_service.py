from sqlalchemy.ext.asyncio import AsyncSession
from app.models.post import Post
from app.schemas.post import PostCreate
from app.schemas.post import PostUpdate
from sqlalchemy import (select)
from app.utils.post_utils import (calculate_reading_time)


async def create_post(
        payload:PostCreate,
        user_id:int,
        db:AsyncSession
):
    post=Post(title=payload.title,
              content=payload.content,
              owner_id=user_id,
              reading_time=calculate_reading_time(payload.content))
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post


async def get_posts(db:AsyncSession,limit:int,offset:int):
    query=(select(Post).order_by(Post.created_at.desc()).limit(limit).offset(offset))
    result = await db.execute(query)
    return result.scalars().all()

async def get_post(post_id:int, db:AsyncSession):
    query=(select(Post).where(Post.id==post_id))
    result=await db.execute(query)
    post=result.scalar()
    return post

async def update_post(post_id:int,
                      payload:PostUpdate,
                      user_id:int,
                      db:AsyncSession):
    query=(select(Post).where(Post.id==post_id))
    result= await db.execute(query)
    post=result.scalar()

    if not post:
        return None
    
    if post.owner_id!=user_id:
        raise PermissionError("Not Allowed")
    
    updates=(payload.model_dump(exclude_unset=True))

    for key,value in updates.items():
        setattr(post,key,value)

    if payload.content:
        post.reading_time=(calculate_reading_time(payload.content))

    await db.commit()
    await db.refresh(post)
    return post


async def delete_post(post_id:int, user_id:int,db:AsyncSession):
    query=(select(Post).where(Post.id==post_id))
    result=await db.execute(query)
    post=result.scalar()
    if not post:
        return False
    
    if post.owner_id!=user_id:
        raise PermissionError("Not Allowed")
    
    await db.delete(post)
    await db.commit()
    return True
