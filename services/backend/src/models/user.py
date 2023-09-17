from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from src.core.db import Base
from sqlalchemy import Column, String

class User(SQLAlchemyBaseUserTable[int], Base):
    full_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    address = Column(String, nullable=True)
