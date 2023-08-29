from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.base import CRUDBase
from src.models.car import Car
from src.schemas.car import CarCreate, CarSchema, CarUpdate
from src.core.db import get_async_session


router = APIRouter()

car_crud = CRUDBase(Car)


@router.get("/cars/{car_id}", response_model=CarSchema, tags=("CARS",))
async def get_car_by_id(
    car_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        car = await car_crud.get(obj_id=car_id, session=session)
        if not car:
            raise HTTPException(status_code=404, detail="Car not found")
        return car
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("cars/", response_model=List[CarSchema], tags=["CARS"])
async def get_all_cars(
    session: AsyncSession = Depends(get_async_session)
):
    cars = await car_crud.get_multi(session=session)
    return cars

@router.post("cars/", response_model=CarSchema, tags=["CARS"])
async def create_car(
    car_data: CarCreate,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        car = await car_crud.create(obj_in=car_data, session=session)
        return car
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("cars/{car_id}", response_model=CarSchema, tags=["CARS"])
async def patch_car(
    car_id: int,
    car_data: CarUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        car = await car_crud.get(obj_id=car_id, session=session)
        if not car:
            raise HTTPException(status_code=404, detail="Car not found")
        
        patched_car = await car_crud.patch(db_obj=car, obj_in=car_data, session=session)
        return patched_car
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("cars/{car_id}", response_model=CarSchema, tags=["CARS"])
async def update_car(
    car_id: int,
    car_data: CarUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        car = await car_crud.get(obj_id=car_id, session=session)
        if not car:
            raise HTTPException(status_code=404, detail="Car not found")
        
        updated_car = await car_crud.update(db_obj=car, obj_in=car_data, session=session)
        return updated_car
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("cars/{car_id}", response_model=CarSchema, tags=["CARS"])
async def delete_car(
    car_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        car = await car_crud.get(obj_id=car_id, session=session)
        if not car:
            raise HTTPException(status_code=404, detail="Car not found")
        
        deleted_car = await car_crud.remove(db_obj=car, session=session)
        return deleted_car
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# from typing import List
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession
# from src.models.car import Car
# from src.crud.repositories.car_repository import CarRepository
# from src.schemas.car import CarCreate, CarUpdate, Car
# from src.core.db import get_async_session

# router = APIRouter()


# @router.post("/cars/", response_model=CarCreate, tags=("CARS",))
# async def create_car(
#     car_create: CarCreate, db: AsyncSession = Depends(get_async_session)
# ):
#     car_repo = CarRepository(db)
#     created_car = await car_repo.create_car(car_create)
#     return created_car


# @router.get("/cars/{car_id}", response_model=Car, tags=("CARS",))
# async def get_car_by_id(car_id: int, db: AsyncSession = Depends(get_async_session)):
#     car_repo = CarRepository(db)
#     car = await car_repo.get_car_by_id(car_id)
#     if car is None:
#         raise HTTPException(status_code=404, detail="Car not found")
#     return car


# @router.put("/cars/{car_id}", response_model=Car, tags=("CARS",))
# async def update_car(
#     car_id: int, car_update: CarUpdate, db: AsyncSession = Depends(get_async_session)
# ):
#     car_repo = CarRepository(db)
#     updated_car = await car_repo.update_car(car_id, car_update)
#     if updated_car is None:
#         raise HTTPException(status_code=404, detail="Car not found")
#     return updated_car


# @router.delete("/cars/{car_id}", response_model=Car, tags=("CARS",))
# async def delete_car(car_id: int, db: AsyncSession = Depends(get_async_session)):
#     car_repo = CarRepository(db)
#     deleted_car = await car_repo.delete_car(car_id)
#     if deleted_car is None:
#         raise HTTPException(status_code=404, detail="Car not found")
#     return deleted_car


# @router.get("/cars/", response_model=List[Car], tags=("CARS",))
# async def get_all_cars(db: AsyncSession = Depends(get_async_session)):
#     car_repo = CarRepository(db)
#     cars = await car_repo.get_all_cars()
#     return cars


# @router.patch("/cars/{car_id}", response_model=Car, tags=("CARS",))
# async def patch_car(
#     car_id: int, car_update: CarUpdate, db: AsyncSession = Depends(get_async_session)
# ):
#     car_repo = CarRepository(db)
#     patched_car = await car_repo.patch_car(car_id, car_update)
#     if patched_car is None:
#         raise HTTPException(status_code=404, detail="Car not found")
#     return patched_car
