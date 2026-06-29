from pydantic import BaseModel
from pydantic import ConfigDict
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title:str
    content:str


class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id:int
    owner_id:int
    reading_time:int
    created_at:datetime
    model_config=ConfigDict(
        from_attributes=True
    )

class PostUpdate(BaseModel):
    title:Optional[str]=None
    content:Optional[str]=None