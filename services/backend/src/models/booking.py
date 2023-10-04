from sqlalchemy import (
    JSON,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from datetime import datetime
from src.core.db import Base


class BookingCar(Base):
    application_date = Column(DateTime, default=datetime.now)
    from_reserve = Column(DateTime)
    to_reserve = Column(DateTime)
    car_id = Column(Integer, ForeignKey("car.id"))
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    email = Column(String)
    additional_services = Column(
        JSON, default={}
    )
    total_amount = Column(
        Integer, default=0
    )
