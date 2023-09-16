from src.models.price import Price
from src.schemas.booking import BookingCarCreate
from src.service.calculate import calculate_total_amount
from src.crud.base import CRUDBase
from src.models.booking import BookingCar
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDBookingCar(CRUDBase):
    pass


bookingcar_crud = CRUDBookingCar(BookingCar)
