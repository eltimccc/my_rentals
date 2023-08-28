# from typing import List
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession
# from src.crud.base import CRUDBase
# from src.models.car import Car
# from src.schemas.car import CarCreate
# from src.core.db import get_async_session
# from src.schemas.car import CarInfo, CarCreate

# router = APIRouter()

# car_crud = CRUDBase(Car)


# @router.post("/", response_model=CarCreate, tags=("CARS",))
# async def create_car(
#     car_data: CarCreate,
#     session: AsyncSession = Depends(get_async_session)
# ):
#     try:
#         car = await car_crud.create(session=session, obj_in=car_data)
#         return car
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.car import Car
from src.crud.repositories.car_repository import CarRepository
from src.schemas.car import CarCreate, CarUpdate, Car
from src.core.db import get_async_session

router = APIRouter()


@router.post("/cars/", response_model=CarCreate, tags=("CARS",))
async def create_car(
    car_create: CarCreate, db: AsyncSession = Depends(get_async_session)
):
    car_repo = CarRepository(db)
    created_car = await car_repo.create_car(car_create)
    return created_car


@router.get("/cars/{car_id}", response_model=Car, tags=("CARS",))
async def get_car_by_id(car_id: int, db: AsyncSession = Depends(get_async_session)):
    car_repo = CarRepository(db)
    car = await car_repo.get_car_by_id(car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


@router.put("/cars/{car_id}", response_model=Car, tags=("CARS",))
async def update_car(
    car_id: int, car_update: CarUpdate, db: AsyncSession = Depends(get_async_session)
):
    car_repo = CarRepository(db)
    updated_car = await car_repo.update_car(car_id, car_update)
    if updated_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return updated_car


@router.delete("/cars/{car_id}", response_model=Car, tags=("CARS",))
async def delete_car(car_id: int, db: AsyncSession = Depends(get_async_session)):
    car_repo = CarRepository(db)
    deleted_car = await car_repo.delete_car(car_id)
    if deleted_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return deleted_car


@router.get("/cars/", response_model=List[Car], tags=("CARS",))
async def get_all_cars(db: AsyncSession = Depends(get_async_session)):
    car_repo = CarRepository(db)
    cars = await car_repo.get_all_cars()
    return cars


@router.patch("/cars/{car_id}", response_model=Car, tags=("CARS",))
async def patch_car(
    car_id: int, car_update: CarUpdate, db: AsyncSession = Depends(get_async_session)
):
    car_repo = CarRepository(db)
    patched_car = await car_repo.patch_car(car_id, car_update)
    if patched_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return patched_car
