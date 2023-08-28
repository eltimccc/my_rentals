from sqlalchemy import Column, ForeignKey, String, Integer, Text
from src.core.db import Base
from sqlalchemy.orm import relationship


class Car(Base):
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String)
    price_id = Column(Integer, ForeignKey("price.id"))
    price = relationship("Price", back_populates="cars_association")
    photo_url = Column(String)
    description = Column(Text)
    base_price = Column(Integer)
    color = Column(String(50))
    transmission = Column(String(50))
    air_cold = Column(String(50))
    power= Column(Integer)
    fuel_type = Column(String(50))
    fuel_rate = Column(String(50))
    year = Column(Integer)