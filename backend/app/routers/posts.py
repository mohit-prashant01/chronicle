from fastapi import (APIRouter,Depends)
from sqlalchemy.ext.asyncio import (AsyncSession)
from typing import List
from fastapi import (HTTPException)

from app.db.database import (get_db)
from app.models.user import (User)
from app.schemas.post import(PostCreate,PostResponse)
from app.services.post_service import (create_post)
from app.core.dependencies import (get_current_user)
from app.services.post_service import(create_post,get_posts,get_post)


router=APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post("/",response_model=PostResponse)
async def create_new_post(
    payload:PostCreate,
    db:AsyncSession=Depends(get_db),
    user:User=Depends(get_current_user)
):
    return await create_post(
        payload,
        user.id,
        db
    )


@router.get("/",response_model=List[PostResponse])
async def read_posts(db:AsyncSession=Depends(get_db)):
    return await get_posts(db)


@router.get("/{posts_id}",response_model=PostResponse)
async def read_post(post_id:int,db:AsyncSession=Depends(get_db)):
    post=await get_post(post_id,db)
    
    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post Not Found"
        )
    
    return post


