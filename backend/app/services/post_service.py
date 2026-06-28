from sqlalchemy.ext.asyncio import AsyncSession
from app.models.post import Post
from app.schemas.post import PostCreate

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