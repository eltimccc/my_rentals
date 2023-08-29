from typing import Optional
from pydantic import BaseModel, Field, PositiveInt


class CarBase(BaseModel):
    brand: str = Field(..., min_length=1, max_length=50)
    price_id: int
    photo_url: Optional[str] = "default"
    description: str = Field("descr", min_length=1, max_length=500)
    base_price: Optional[int] = 0
    color: str = Field("Black", min_length=1, max_length=50)
    transmission: str = Field("transm", min_length=1, max_length=20)
    air_cold: Optional[str] = "default"
    power: Optional[PositiveInt] = 0
    fuel_type: Optional[str] = "default"
    fuel_rate: Optional[str] = "default"
    year: Optional[PositiveInt] = 0


class CarCreate(CarBase):
    pass


class CarUpdate(CarBase):
    pass


# class Car(CarBase):
#     id: int

#     class Config:
#         orm_mode = True

class CarSchema(CarBase):
    id: int

    class Config:
        orm_mode = True
