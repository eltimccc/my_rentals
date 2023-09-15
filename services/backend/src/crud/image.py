from src.crud.base import CRUDBase
from src.models.image import Image


class CRUDImage(CRUDBase):
    pass


img_crud = CRUDImage(Image)
