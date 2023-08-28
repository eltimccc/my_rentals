from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import get_async_session
from src.crud.repositories.price_repository import PriceRepository
from src.schemas.price import PriceCreate, Price

router = APIRouter()


@router.post("/prices/", response_model=Price, tags=("PRICES",))
async def create_price(
    price: PriceCreate, db: AsyncSession = Depends(get_async_session)
):
    price_repo = PriceRepository(db)
    created_price = await price_repo.create_price(price)
    return created_price


@router.get("/prices/{price_id}", response_model=Price, tags=("PRICES",))
async def get_price_by_id(price_id: int, db: AsyncSession = Depends(get_async_session)):
    price_repo = PriceRepository(db)
    price = await price_repo.get_price_by_id(price_id)
    if price is None:
        raise HTTPException(status_code=404, detail="Price not found")
    return price


@router.get("/prices/", response_model=List[Price], tags=("PRICES",))
async def get_all_prices(db: AsyncSession = Depends(get_async_session)):
    price_repo = PriceRepository(db)
    prices = await price_repo.get_all_prices()
    return prices


@router.put("/prices/{price_id}", response_model=Price, tags=("PRICES",))
async def update_price(
    price_id: int,
    price_update: PriceCreate,
    db: AsyncSession = Depends(get_async_session),
):
    price_repo = PriceRepository(db)
    updated_price = await price_repo.update_price(price_id, price_update)

    if updated_price is None:
        raise HTTPException(status_code=404, detail="Price not found")

    return updated_price


@router.patch("/prices/{price_id}", response_model=Price, tags=("PRICES",))
async def patch_price(
    price_id: int,
    price_update: PriceCreate,
    db: AsyncSession = Depends(get_async_session),
):
    price_repo = PriceRepository(db)
    patched_price = await price_repo.patch_price(price_id, price_update)

    if patched_price is None:
        raise HTTPException(status_code=404, detail="Price not found")

    return patched_price


@router.delete("/prices/{price_id}", response_model=Price, tags=("PRICES",))
async def delete_price(price_id: int, db: AsyncSession = Depends(get_async_session)):
    price_repo = PriceRepository(db)
    deleted_price = await price_repo.delete_price(price_id)

    if deleted_price is None:
        raise HTTPException(status_code=404, detail="Price not found")

    return deleted_price
