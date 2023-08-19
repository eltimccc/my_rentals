from sqlalchemy import Column, String, Integer
from src.core.db import Base
from sqlalchemy.orm import relationship


class Price(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    cars = relationship('Car', back_populates='price')
    one_day = Column(Integer)
    two_three_days = Column(Integer)
    four_seven_days = Column(Integer)
    eight_fourteen_days = Column(Integer)
    fifteen_thirty_days = Column(Integer)
    weekend = Column(Integer)
    deposit = Column(Integer)