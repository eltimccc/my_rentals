from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer

class News(BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    title: str
    content: str
    author: str
    publication_date: datetime
    photo_url: Optional[str]