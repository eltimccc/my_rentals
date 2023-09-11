from datetime import datetime
from pydantic import BaseModel, validator, root_validator


class BookingCarBase(BaseModel):
    from_reserve: datetime
    to_reserve: datetime

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


class BookingCarCreate(BookingCarBase):
    car_id: int


class BookingCarUpdate(BookingCarBase):
    pass


class BookingCarDB(BookingCarBase):
    id: int
    car_id: int

    class Config:
        orm_mode = True
