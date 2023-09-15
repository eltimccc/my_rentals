from src.crud.base import CRUDBase
from src.models.price import Price


class CRUDPrice(CRUDBase):
    pass


price_crud = CRUDPrice(Price)
