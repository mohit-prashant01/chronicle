from pydantic import BaseModel
from pydantic import ConfigDict
from datetime import datetime

class PostBase(BaseModel):
    title:str
    content:str


class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id:int
    owner_id:int
    created_at:datetime
    model_config=ConfigDict(
        from_attributes=True
    )