from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.base import CRUDBase
from src.models.price import Price
from src.schemas.price import PriceCreate, PriceSchema, PriceUpdate
from src.core.db import get_async_session
from src.crud.price import price_crud


router = APIRouter()

# price_crud = CRUDBase(Price)


@router.get("/{price_id}", response_model=PriceSchema)
async def get_price_by_id(
    price_id: int, session: AsyncSession = Depends(get_async_session)
):
    try:
        price = await price_crud.get(obj_id=price_id, session=session)
        if not price:
            raise HTTPException(status_code=404, detail="Price not found")
        return price
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=List[PriceSchema])
async def get_all_prices(session: AsyncSession = Depends(get_async_session)):
    prices = await price_crud.get_multi(session=session)
    return prices


@router.post("/", response_model=PriceSchema)
async def create_price(
    price_data: PriceCreate, session: AsyncSession = Depends(get_async_session)
):
    try:
        price = await price_crud.create(obj_in=price_data, session=session)
        return price
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{price_id}", response_model=PriceSchema)
async def patch_price(
    price_id: int,
    price_data: PriceUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        price = await price_crud.get(obj_id=price_id, session=session)
        if not price:
            raise HTTPException(status_code=404, detail="Price not found")

        patched_car = await price_crud.patch(
            db_obj=price, obj_in=price_data, session=session
        )
        return patched_car
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{price_id}", response_model=PriceSchema)
async def delete_price(
    price_id: int, session: AsyncSession = Depends(get_async_session)
):
    try:
        price = await price_crud.get(obj_id=price_id, session=session)
        if not price:
            raise HTTPException(status_code=404, detail="Price not found")

        deleted_price = await price_crud.remove(db_obj=price, session=session)
        return deleted_price
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{price_id}", response_model=PriceSchema)
async def update_price(
    price_id: int,
    price_data: PriceUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        price = await price_crud.get(obj_id=price_id, session=session)
        if not price:
            raise HTTPException(status_code=404, detail="Price not found")

        updated_price = await price_crud.update(
            db_obj=price, obj_in=price_data, session=session
        )
        return updated_price
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
