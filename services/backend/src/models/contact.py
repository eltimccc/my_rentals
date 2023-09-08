from src.core.db import Base
from sqlalchemy import Column, String


class Contact(Base):
    email: str = Column(String(50))
    phone: str = Column(String(50))
    phone2: str = Column(String(50))
    vk: str = Column(String(50))
    address: str = Column(String(50))
    description: str = Column(String(50))
