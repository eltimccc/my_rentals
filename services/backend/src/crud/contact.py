from src.crud.base import CRUDBase
from src.models.contact import Contact


class CRUDContact(CRUDBase):
    pass


contact_crud = CRUDContact(Contact)
