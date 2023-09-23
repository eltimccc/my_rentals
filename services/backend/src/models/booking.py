from sqlalchemy import JSON, Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from src.core.db import Base


# class BookingCar(Base):
#     from_reserve = Column(DateTime)
#     to_reserve = Column(DateTime)
#     car_id = Column(Integer, ForeignKey("car.id"))
#     first_name = Column(String)
#     last_name = Column(String)
#     phone = Column(String)
#     email = Column(String)
#     additional_services_airport = Column(Boolean, default=False)
#     additional_services_railway_station = Column(Boolean, default=False)
#     additional_services_your_address = Column(Boolean, default=False)
#     additional_services_add_driver = Column(Boolean, default=False)
#     additional_services_washing = Column(Boolean, default=False)
#     total_amount = Column(Integer)

class BookingCar(Base):
    from_reserve = Column(DateTime)
    to_reserve = Column(DateTime)
    car_id = Column(Integer, ForeignKey("car.id"))
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    email = Column(String)
    additional_services = Column(JSON, default={})  # JSON-поле для хранения информации о дополнительных услугах и их количестве
    total_amount = Column(Integer, default=0)  # Поле для хранения общей стоимости бронирования