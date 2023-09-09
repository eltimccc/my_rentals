from src.core.db import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from typing import Optional


class News(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    author = Column(String)
    publication_date = Column(DateTime, default=datetime.utcnow)
    photo_url = Column(String, nullable=True)
