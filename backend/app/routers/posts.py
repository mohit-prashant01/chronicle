from fastapi import (APIRouter,Depends)
from sqlalchemy.ext.asyncio import (AsyncSession)
from app.db.database import (get_db)
from app.models.user import (User)
from app.schemas.post import(PostCreate,PostResponse)
from app.services.post_service import (create_post)
from app.core.dependencies import (get_current_user)

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
