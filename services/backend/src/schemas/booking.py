from datetime import datetime, timedelta
from typing import Dict, Optional
from pydantic import BaseModel, EmailStr, Extra, Field, validator, root_validator


FROM_TIME = (datetime.now() + timedelta(minutes=10)).isoformat(timespec="minutes")

TO_TIME = (datetime.now() + timedelta(hours=1)).isoformat(timespec="minutes")


class BookingCarBase(BaseModel):
    from_reserve: datetime = Field(..., example=FROM_TIME)
    to_reserve: datetime = Field(..., example=TO_TIME)
    first_name: str
    last_name: str
    phone: str
    email: str
    total_amount: Optional[int]
    additional_services: Dict[str, int] = {}  # Словарь для хранения выбранных дополнительных услуг и их количества


    class Config:
        extra = Extra.forbid


class BookingCarUpdate(BookingCarBase):
    @validator("from_reserve")
    def check_from_reserve_later_than_now(cls, value):
        if value <= datetime.now():
            raise ValueError(
                "Время начала бронирования не может быть меньше текущего времени"
            )
        return value

    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, values):
        if values["from_reserve"] >= values["to_reserve"]:
            raise ValueError(
                "Время начала бронирования не может быть больше времени окончания"
            )
        return values


class BookingCarCreate(BookingCarUpdate):
    car_id: int
    

class BookingCarDB(BookingCarBase):
    id: int
    car_id: int

    class Config:
        orm_mode = True


class BookingCarID(BookingCarBase):
    car_id: int

    class Config:
        orm_mode = True
