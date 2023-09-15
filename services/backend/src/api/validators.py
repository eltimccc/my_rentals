from sqlalchemy import select
from src.core.db import AsyncSessionLocal
from src.models import Car
from fastapi import HTTPException


async def validate_car_exists(session: AsyncSessionLocal, car_id: int):
    async with session.begin():
        car = await session.execute(select(Car).filter(Car.id == car_id))
        car_obj = car.scalar_one_or_none()
        if not car_obj:
            raise HTTPException(status_code=404, detail="Автомобиль отсутствует")
        return car_obj
