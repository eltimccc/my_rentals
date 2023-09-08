from typing import Optional
from pydantic import BaseModel, PositiveInt


class CarBase(BaseModel):
    brand: str = "default"
    model: str = "default"
    price_id: int = 2
    photo_url: str = "default"
    description: str
    base_price: Optional[int] = 1999
    color: str = "default"
    transmission: str
    air_cold: str = "default"
    power: Optional[PositiveInt] = 100
    fuel_type: str = "default"
    fuel_rate: str = "default"
    year: Optional[PositiveInt] = 1990


class CarCreate(CarBase):
    pass


class CarUpdate(CarBase):
    pass


class CarSchema(CarBase):
    id: int

    class Config:
        orm_mode = True
