from src.crud.base import CRUDBase
from src.models.car import Car


class CRUDCar(CRUDBase):
    pass


car_crud = CRUDCar(Car)
