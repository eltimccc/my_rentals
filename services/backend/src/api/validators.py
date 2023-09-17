from src.models.booking import BookingCar
from src.core.db import AsyncSessionLocal
from src.models import Car
from fastapi import HTTPException


async def validate_car_exists(session: AsyncSessionLocal, car_id: int):
    car = await session.get(Car, car_id)

    if not car:
        raise HTTPException(status_code=404, detail="Автомобиль отсутствует")

    return car


async def validate_booking_exists(session: AsyncSessionLocal, booking_id: int):
    booking = await session.get(BookingCar, booking_id)

    if not booking:
        raise HTTPException(status_code=404, detail="Букинга не имеется")

    return booking
