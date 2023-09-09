from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NewsBase(BaseModel):
    title: str
    content: str
    author: str
    photo_url: Optional[str] = None


class NewsCreate(NewsBase):
    pass


class NewsUpdate(NewsBase):
    pass


class NewsDelete(NewsBase):
    id: int


class NewsSchema(NewsBase):
    id: int
    publication_date: datetime

    class Config:
        orm_mode = True
