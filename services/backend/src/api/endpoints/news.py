from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.news import NewsDelete

from src.schemas.news import NewsCreate, NewsSchema, NewsUpdate
from src.core.db import get_async_session
from src.crud.news import news_crud


router = APIRouter()


@router.get(
    "/",
    response_model=List[NewsSchema],
    tags=("NEWS",),
    description="Получение всех новостей",
)
async def get_all_news(session: AsyncSession = Depends(get_async_session)):
    news = await news_crud.get_multi(session=session)
    return news


@router.post(
    "/", response_model=NewsSchema, tags=("NEWS",), description="Создание новости"
)
async def create_news(
    news_data: NewsCreate,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        news = await news_crud.create(obj_in=news_data, session=session)
        return news
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/{news_id}",
    response_model=NewsSchema,
    tags=("NEWS",),
    description="Получение новости по ID",
)
async def read_news(
    news_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        news = await news_crud.get(obj_id=news_id, session=session)
        if not news:
            raise HTTPException(status_code=404, detail="News not found")
        return news
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put(
    "/{news_id}",
    response_model=NewsSchema,
    tags=("NEWS",),
    description="Обновление новости",
)
async def update_news(
    news_id: int,
    news_data: NewsUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        news = await news_crud.get(obj_id=news_id, session=session)
        if not news:
            raise HTTPException(status_code=404, detail="News not found")

        updated_news = await news_crud.update(
            db_obj=news, obj_in=news_data, session=session
        )
        return updated_news
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete(
    "/{news_id}",
    response_model=NewsDelete,
    tags=("NEWS",),
    description="Удаление новости",
)
async def delete_news(
    news_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        news = await news_crud.get(obj_id=news_id, session=session)
        if not news:
            raise HTTPException(status_code=404, detail="News not found")

        deleted_news = await news_crud.remove(db_obj=news, session=session)
        return deleted_news
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
