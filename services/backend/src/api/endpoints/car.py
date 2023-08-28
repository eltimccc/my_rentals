from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.base import CRUDBase
from src.models.car import Car
from src.schemas.car import CarCreate
from src.core.db import get_async_session
from src.schemas.car import CarInfo

router = APIRouter()

car_crud = CRUDBase(Car)


@router.post("/", response_model=CarInfo, tags=("CARS",))
async def create_car(
    car_data: CarCreate,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        car = await car_crud.create(session=session, obj_in=car_data)
        return car
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/list", response_model=list[CarInfo], tags=("CARS",))
async def get_car_list(
    session: AsyncSession = Depends(get_async_session)
):
    car_list = await car_crud.get_multi(session)
    return car_list


@router.patch("/", response_model=List[CarInfo], tags=('CARS',))
async def update_car(
    session: AsyncSession = Depends(get_async_session),
) -> List[CarInfo]:
    return