from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from src.core.db import Base


class BookingCar(Base):
    from_reserve = Column(DateTime)
    to_reserve = Column(DateTime)
    car_id = Column(Integer, ForeignKey("car.id"))
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    email = Column(String)
    additional_services = Column(
        JSON, default={}
    )  # JSON-поле для хранения информации о дополнительных услугах и их количестве
    total_amount = Column(
        Integer, default=0
    )  # Поле для хранения общей стоимости бронирования
