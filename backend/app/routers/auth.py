from fastapi import(
    APIRouter,
    Depends,
    HTTPException
)
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.user import(UserCreate,UserResponse,LoginRequest, TokenResponse)
from app.services.user_services import(create_user,login_user)


from app.models.user import User
from app.core.dependencies import (get_current_user)

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
async def login(form_data:OAuth2PasswordRequestForm=Depends(),db:AsyncSession=Depends(get_db)):
    payload=LoginRequest(
        email=form_data.username,
        password=form_data.password
    )
    
    try:
        return await login_user(payload,db)
    except ValueError as e:
        raise HTTPException(status_code =401,detail=str(e))
    


@router.get(
    "/me",
    response_model=UserResponse
)
async def current_user(
    user:User = Depends(get_current_user)
):
    return user