from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.api import validators
from src.schemas.car import CarCreate, CarSchema, CarUpdate
from src.core.db import get_async_session
from src.crud.car import car_crud


router = APIRouter()


@router.get(
    "/{car_id}",
    response_model=CarSchema,
    description="Получение одного автомобиля по его id",
)
async def get_car_by_id(
    car_id: int, session: AsyncSession = Depends(get_async_session)
):
    await validators.validate_car_exists(session, car_id)
    car = await car_crud.get(obj_id=car_id, session=session)
    return car


@router.get(
    "/",
    response_model=List[CarSchema],
    description="Получение всех автомобилей из БД",
)
async def get_all_cars(session: AsyncSession = Depends(get_async_session)):
    cars = await car_crud.get_multi(session=session)
    return cars


## hateoas
# @router.get(
#     "/",
#     response_model=List[dict],
#     description="Получение всех автомобилей из БД",
# )
# async def get_all_cars(session: AsyncSession = Depends(get_async_session)):
#     cars = await session.execute(select(Car))

#     # Создаем список автомобилей с гиперссылками
#     cars_with_links = []
#     for car in cars.scalars():
#         car_dict = car.to_dict()
#         cars_with_links.append(car_dict)

#     return cars_with_links


@router.post(
    "/",
    response_model=CarSchema,
    description="Создание автомобиля",
)
async def create_car(
    car_data: CarCreate, session: AsyncSession = Depends(get_async_session)
):
    try:
        car = await car_crud.create(obj_in=car_data, session=session)
        return car
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch(
    "/{car_id}",
    response_model=CarSchema,
    description="Частичное редактирование автомобиля",
)
async def patch_car(
    car_id: int, car_data: CarUpdate, session: AsyncSession = Depends(get_async_session)
):
    await validators.validate_car_exists(session, car_id)

    car = await car_crud.get(obj_id=car_id, session=session)
    patched_car = await car_crud.patch(db_obj=car, obj_in=car_data, session=session)
    return patched_car


@router.put(
    "/{car_id}",
    response_model=CarSchema,
    description="Полное редактирование автомои=биля",
)
async def update_car(
    car_id: int, car_data: CarUpdate, session: AsyncSession = Depends(get_async_session)
):
    await validators.validate_car_exists(session, car_id)

    car = await car_crud.get(obj_id=car_id, session=session)
    updated_car = await car_crud.update(db_obj=car, obj_in=car_data, session=session)
    return updated_car


@router.delete(
    "/{car_id}",
    response_model=CarSchema,
    description="Удаление автомобиля по его id",
)
async def delete_car(car_id: int, session: AsyncSession = Depends(get_async_session)):
    car = await validators.validate_car_exists(session, car_id)

    deleted_car = await car_crud.remove(db_obj=car, session=session)
    return deleted_car
