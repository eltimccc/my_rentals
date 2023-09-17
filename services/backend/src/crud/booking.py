from sqlalchemy import select
from src.crud.base import CRUDBase
from src.models.booking import BookingCar
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDBookingCar(CRUDBase):
    async def get_bookings_for_car(self, car_id: int, session: AsyncSession):
        query = select(self.model).filter(self.model.car_id == car_id)
        db_objs = await session.execute(query)
        return db_objs.scalars().all()


bookingcar_crud = CRUDBookingCar(BookingCar)
