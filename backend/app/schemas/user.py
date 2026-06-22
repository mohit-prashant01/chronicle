from pydantic import(
    BaseModel,
    EmailStr,
    ConfigDict,
    Field
)

class UserBase(BaseModel):
    username:str
    email:EmailStr

class UserCreate(UserBase):
    password:str =Field(
        min_length=8
    )

class UserResponse(UserBase):
    id:int
    model_config=ConfigDict(
        from_attributes=True
    )

class LoginRequest(BaseModel):
    email:EmailStr
    password:str

class TokenResponse(BaseModel):
    access_token:str
    token_type:str