from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.service.services_constants import services_constants
from src.api.endpoints.car import get_car_by_id
from src.core.email_service import send_email_booking

from src.api.validators import validate_booking_exists, validate_car_exists
from src.service.calculate import calculate_and_add_booking
from src.core.db import AsyncSessionLocal, get_async_session
from src.core.user import current_superuser
from src.schemas.booking import BookingCarCreate, BookingCarDB, BookingCarUpdate
from src.crud.booking import bookingcar_crud

router = APIRouter()


@router.get(
    "/",
    response_model=List[BookingCarDB],
    description="Получение всех броней из БД",
    # dependencies=[Depends(current_superuser)], ## Активировать на проде
)
async def get_all_bookings(session: AsyncSession = Depends(get_async_session)):
    bookings = await bookingcar_crud.get_multi(session=session)
    return bookings


@router.get(
    "/{booking_id}",
    response_model=BookingCarDB,
    description="Получение бронирования по его ID",
    # dependencies=[Depends(current_superuser)], ## Активировать на проде
)
async def get_booking_by_id(
    booking_id: int, session: AsyncSession = Depends(get_async_session)
):
    await validate_booking_exists(session, booking_id)
    booking = await bookingcar_crud.get(obj_id=booking_id, session=session)

    return booking


@router.post(
    "/",
    response_model=BookingCarDB,
    description="Создание бронирования автомобиля",
)
async def create_booking(
    booking: BookingCarCreate,
    session: AsyncSession = Depends(get_async_session),
):
    await validate_car_exists(session, booking.car_id)

    total_additional_services_cost = 0
    additional_services = booking.additional_services

    for service, quantity in additional_services.items():
        if service in services_constants:
            total_additional_services_cost += services_constants[service] * quantity

    new_booking = await calculate_and_add_booking(booking, session)
    new_booking.total_amount += total_additional_services_cost
    car_data = await get_car_by_id(booking.car_id, session)

    send_email_booking(new_booking, car_data, services_constants)

    return new_booking


@router.patch(
    "/{booking_id}",
    response_model=BookingCarDB,
    description="Update booking by ID",
    # dependencies=[Depends(current_superuser)], ## Активировать на проде
)
async def update_booking_by_id(
    booking_id: int,
    booking_update: BookingCarUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    booking = await bookingcar_crud.get(obj_id=booking_id, session=session)

    updated_booking = await bookingcar_crud.patch(
        db_obj=booking, obj_in=booking_update, session=session
    )
    return updated_booking


@router.get(
    "/car/",
    response_model=List[BookingCarDB],
    description="Получение списка бронирований для конкретного автомобиля",
)
async def get_bookings_for_car(
    car_id: int, session: AsyncSession = Depends(get_async_session)
):
    bookings = await bookingcar_crud.get_bookings_for_car(
        car_id=car_id, session=session
    )

    return bookings


@router.delete(
    "/{booking_id}",
    response_model=BookingCarDB,
    description="Удаление бронирования по его ID",
    dependencies=[Depends(current_superuser)],
)
async def delete_booking(
    booking_id: int,
    session: AsyncSessionLocal = Depends(get_async_session),
):
    booking = await validate_booking_exists(session=session, booking_id=booking_id)

    deleted_booking = await bookingcar_crud.remove(db_obj=booking, session=session)
    return deleted_booking
