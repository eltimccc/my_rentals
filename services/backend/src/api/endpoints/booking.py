from typing import List
from fastapi import APIRouter, HTTPException
from src.core.db import get_async_session
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.booking import BookingCarCreate
from src.schemas.booking import BookingCarDB
from src.crud.booking import bookingcar_crud

router = APIRouter()


@router.get(
    "/",
    response_model=List[BookingCarDB],
    description="Получение всех автомобилей из БД",
)
async def get_all_bookings(session: AsyncSession = Depends(get_async_session)):
    bookings = await bookingcar_crud.get_multi(session=session)
    return bookings


@router.get(
    "/{booking_id}",
    response_model=BookingCarDB,
    description="Получение бронирования по его ID",
)
async def get_booking_by_id(
    booking_id: int, session: AsyncSession = Depends(get_async_session)
):
    booking = await bookingcar_crud.get(obj_id=booking_id, session=session)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking


@router.post("/", response_model=BookingCarDB)
async def create_booking(
    booking: BookingCarCreate,
    session: AsyncSession = Depends(get_async_session),
):
    new_booking = await bookingcar_crud.create(booking, session)
    return new_booking
