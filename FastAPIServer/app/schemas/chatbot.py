from typing import Optional

from pydantic import BaseModel


class ChatBotDTO(BaseModel):
    sentence: Optional[str]

    class Config:
        orm_mode = True
