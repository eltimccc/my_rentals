from sqlalchemy import Column, ForeignKey, String, Integer, Text
from src.core.db import Base
from sqlalchemy.orm import relationship


class Car(Base):
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String)
    price_id = Column(Integer, ForeignKey("price.id"))
    price = relationship("Price", back_populates="cars_association")
    image_id = Column(Integer, ForeignKey("image.id"))
    photo_url = Column(String)
    description = Column(Text)
    base_price = Column(Integer)
    color = Column(String(50))
    transmission = Column(String(50))
    air_cold = Column(String(50))
    power = Column(Integer)
    fuel_type = Column(String(50))
    fuel_rate = Column(String(50))
    year = Column(Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "brand": self.brand,
            "model": self.model,
            "price_id": self.price_id,
            "photo_url": self.photo_url,
            "description": self.description,
            "base_price": self.base_price,
            "color": self.color,
            "transmission": self.transmission,
            "air_cold": self.air_cold,
            "power": self.power,
            "fuel_type": self.fuel_type,
            "fuel_rate": self.fuel_rate,
            "year": self.year,
            "links": {
                "self": f"/api/cars/{self.id}",
            }
        }
