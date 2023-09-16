from src.service.booking_service import calculate_total_amount
from src.models.car import Car
from src.schemas.booking import BookingCarCreate
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.price import Price
from src.crud.booking import bookingcar_crud


async def calculate_and_add_booking(
    booking: BookingCarCreate,
    session: AsyncSession,
):
    new_booking = await bookingcar_crud.create(booking, session)

    car = await session.get(Car, new_booking.car_id)
    price = await session.get(Price, car.price_id)

    # Рассчитайте total_amount
    total_amount = calculate_total_amount(
        new_booking.from_reserve,
        new_booking.to_reserve,
        price,
    )

    new_booking.total_amount = total_amount

    session.add(new_booking)
    await session.commit()
    await session.refresh(new_booking)

    return new_booking
