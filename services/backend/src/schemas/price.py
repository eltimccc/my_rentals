
from typing import Any, Dict
from pydantic import BaseModel

class PriceBase(BaseModel):
    name: str
    one_day: int
    two_three_days: int
    four_seven_days: int
    eight_fourteen_days: int
    fifteen_thirty_days: int
    weekend: int
    deposit: int

class PriceCreate(PriceBase):
    pass

class PriceUpdate(PriceBase):
    pass

class Price(PriceBase):
    id: int

    class Config:
        orm_mode = True
