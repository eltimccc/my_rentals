from src.crud.base import CRUDBase
from src.models.booking import BookingCar


class CRUDBookingCar(CRUDBase):
    pass


bookingcar_crud = CRUDBookingCar(BookingCar)
