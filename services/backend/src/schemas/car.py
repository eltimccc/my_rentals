from typing import Optional
from pydantic import BaseModel, Field, PositiveInt


class CarBase(BaseModel):
    name: str = Field(..., min_length=1,
                      max_length=50)
    price_id: int
    photo_url: Optional[str] = "default_photo_url"
    description: str = Field('desc here pls', min_length=1,
                             max_length=500)
    base_price: Optional[int] = 0
    color: str = Field("Black", min_length=1, max_length=50)
    transmission: str = Field('trans here pls', min_length=1,
                              max_length=10)
    air_cold: Optional[str] = "I want anything here"
    power: Optional[PositiveInt] = 0
    fuel_type: Optional[str] = "I want anything here"
    fuel_rate: Optional[str] = "I want anything here"
    year: Optional[PositiveInt] = 0


class CarCreate(CarBase):
    pass


class CarUpdate(CarBase):
    pass


class CarInfo(CarBase):
    id: int

    class Config:
        orm_mode = True
