from fastapi import(
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.user import(UserCreate,UserResponse,LoginRequest, TokenResponse)
from app.services.user_services import(create_user,login_user)


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
async def register(
    payload:UserCreate,
    db:AsyncSession = Depends(
        get_db
    )
):
    try:
        return await create_user(
            payload,
            db
        )
    
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail = str(e)
        )


@router.post("/login",response_model=TokenResponse)
async def login(payload:LoginRequest,db:AsyncSession=Depends(get_db)):
    try:
        return await login_user(payload,db)
    except ValueError as e:
        raise HTTPException(status_code =401,detail=str(e))
    