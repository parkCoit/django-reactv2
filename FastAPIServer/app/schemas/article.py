from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from uuid import UUID

class ArticleDTO(BaseModel):
    artseq : Optional[int]
    title : Optional[str]
    content : Optional[str]
    created : Optional[str]
    modified : Optional[str]
    userid: Optional[str]

    class Config:
        orm_mode = True