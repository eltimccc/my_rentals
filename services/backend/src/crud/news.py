from src.crud.base import CRUDBase
from src.models.news import News


class CRUDNews(CRUDBase):
    pass


news_crud = CRUDNews(News)
