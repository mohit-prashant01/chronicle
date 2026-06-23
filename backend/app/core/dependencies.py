from jose import jwt
from jose import JWTError

from fastapi import(Depends,HTTPException,status)
from fastapi.security import(OAuth2PasswordBearer)

from sqlalchemy import select
from sqlalchemy.ext.asyncio import(AsyncSession)

from app.core.config import(settings)

from app.db.database import(get_db)

from app.models.user import(User)

oauth2scheme = OAuth2PasswordBearer(
    tokenUrl ="/auth/login"
)

async def get_current_user(
        token: str = Depends(oauth2scheme),
        db:AsyncSession=Depends(get_db)
):
    credentials_exception = (
        HTTPException(status_code=401,detail="Invalid token")
    )

    try:
        payload = jwt.decode(token,
                             settings.JWT_SECRET_KEY,
                             algorithms=[
                                 settings.JWT_ALGORITHM
                             ]
                            )
        
        user_id=payload.get("sub")
        if not user_id:
            raise credentials_exception
        
    except JWTError:
        raise credentials_exception
    
    query = select(User).where(User.id==int(user_id))

    result = await db.execute(query)
    user = result.scalar()

    if not user:
        raise credentials_exception
    
    return user
    