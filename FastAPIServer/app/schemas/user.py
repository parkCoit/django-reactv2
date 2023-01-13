from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from app.schemas.article import Article


class UserDTO(BaseModel):
    user_id : Optional[UUID]
    user_email : str
    password : str
    user_name : Optional[str]
    phone : Optional[str]
    birth : Optional[str]
    address : Optional[str]
    job : Optional[str]
    user_interests : Optional[str]
    token : Optional[str]
    create_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class UserList(UserDTO):
    articles: List[Article] = []


