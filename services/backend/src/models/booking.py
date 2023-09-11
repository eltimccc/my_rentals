from sqlalchemy import Column, DateTime, ForeignKey, Integer
from src.core.db import Base


class BookingCar(Base):
    from_reserve = Column(DateTime)
    to_reserve = Column(DateTime)
    car_id = Column(Integer, ForeignKey("car.id"))
