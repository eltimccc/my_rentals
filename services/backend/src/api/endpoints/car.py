import os
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.base import CRUDBase
from src.models.car import Car
from src.schemas.car import CarCreate, CarSchema, CarUpdate
from src.core.db import get_async_session
import shutil


router = APIRouter()

car_crud = CRUDBase(Car)


@router.get("/cars/{car_id}", response_model=CarSchema, tags=("CARS",))
async def get_car_by_id(
    car_id: int, session: AsyncSession = Depends(get_async_session)
):
    try:
        car = await car_crud.get(obj_id=car_id, session=session)
        if not car:
            raise HTTPException(status_code=404, detail="Car not found")
        return car
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/cars", response_model=List[CarSchema], tags=("CARS",))
async def get_all_cars(session: AsyncSession = Depends(get_async_session)):
    cars = await car_crud.get_multi(session=session)
    return cars


@router.post("/cars", response_model=CarSchema, tags=["CARS"])
async def create_car(
    car_data: CarCreate, session: AsyncSession = Depends(get_async_session)
):
    try:
        car = await car_crud.create(obj_in=car_data, session=session)
        return car
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @router.post("/uploadfile/", tags=["CARS"])
# async def create_img(
#     photo: UploadFile = File(...), session: AsyncSession = Depends(get_async_session)
# ):
#     with open(f"uploads/{photo.filename}", "wb") as buffer:
#         shutil.copyfileobj(photo.file, buffer)
#     photo_url = f"uploads/{photo.filename}"
#     print(photo_url)
#     return {'photo': photo.filename}


@router.put("/cars/{car_id}", response_model=CarSchema, tags=("CARS",))
async def update_car(
    car_id: int, car_data: CarUpdate, session: AsyncSession = Depends(get_async_session)
):
    try:
        car = await car_crud.get(obj_id=car_id, session=session)
        if not car:
            raise HTTPException(status_code=404, detail="Car not found")

        updated_car = await car_crud.update(
            db_obj=car, obj_in=car_data, session=session
        )
        return updated_car
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/cars/{car_id}", response_model=CarSchema, tags=("CARS",))
async def patch_car(
    car_id: int, car_data: CarUpdate, session: AsyncSession = Depends(get_async_session)
):
    try:
        car = await car_crud.get(obj_id=car_id, session=session)
        if not car:
            raise HTTPException(status_code=404, detail="Car not found")

        patched_car = await car_crud.patch(db_obj=car, obj_in=car_data, session=session)
        return patched_car
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/cars/{car_id}", response_model=CarSchema, tags=("CARS",))
async def delete_car(car_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        car = await car_crud.get(obj_id=car_id, session=session)
        if not car:
            raise HTTPException(status_code=404, detail="Car not found")

        deleted_car = await car_crud.remove(db_obj=car, session=session)
        return deleted_car
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
