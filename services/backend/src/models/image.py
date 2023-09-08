from src.core.db import Base
from sqlalchemy import Column, Integer, LargeBinary, String


class Image(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    data = Column(LargeBinary)
