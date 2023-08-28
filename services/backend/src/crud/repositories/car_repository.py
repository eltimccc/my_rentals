from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound

from src.models.car import Car
from src.schemas.car import CarCreate, CarUpdate


class CarRepository:
    def __init__(self, db: AsyncSession):
        self._db = db

    async def create_car(self, car_create: CarCreate) -> Car:
        car = Car(**car_create.dict())
        self._db.add(car)
        await self._db.commit()
        await self._db.refresh(car)
        return car

    async def get_car_by_id(self, car_id: int) -> Car:
        query = select(Car).where(Car.id == car_id)
        try:
            result = await self._db.execute(query)
            car = result.scalar_one()
            return car
        except NoResultFound:
            return None

    async def update_car(self, car_id: int, car_update: CarUpdate) -> Car:
        query = select(Car).where(Car.id == car_id)
        try:
            result = await self._db.execute(query)
            car = result.scalar_one()
            for attr, value in car_update.dict().items():
                setattr(car, attr, value)
            await self._db.commit()
            await self._db.refresh(car)
            return car
        except NoResultFound:
            return None

    async def patch_car(self, car_id: int, car_update: CarUpdate) -> Car:
        query = select(Car).where(Car.id == car_id)
        try:
            result = await self._db.execute(query)
            car = result.scalar_one()
            for attr, value in car_update.dict().items():
                setattr(car, attr, value)
            await self._db.commit()
            await self._db.refresh(car)
            return car
        except NoResultFound:
            return None

    async def get_all_cars(self) -> List[Car]:
        query = select(Car)
        result = await self._db.execute(query)
        cars = result.scalars().all()
        return cars

    async def delete_car(self, car_id: int) -> Car:
        query = select(Car).where(Car.id == car_id)
        try:
            result = await self._db.execute(query)
            car = result.scalar_one()
            await self._db.delete(car)
            await self._db.commit()
            return car
        except NoResultFound:
            return None
