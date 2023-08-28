from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound

from src.schemas.price import PriceCreate
from src.models.price import Price


class PriceRepository:
    def __init__(self, db: AsyncSession):
        self._db = db

    async def create_price(self, price_create: PriceCreate) -> Price:
        price = Price(**price_create.dict())
        self._db.add(price)
        await self._db.commit()
        await self._db.refresh(price)
        return price

    async def get_price_by_id(self, price_id: int) -> Price:
        query = select(Price).where(Price.id == price_id)
        try:
            result = await self._db.execute(query)
            price = result.scalar_one()
            return price
        except NoResultFound:
            return None

    async def get_all_prices(self) -> List[Price]:
        query = select(Price)
        result = await self._db.execute(query)
        prices = result.scalars().all()
        return prices

    async def update_price(self, price_id: int, price_update: PriceCreate) -> Price:
        query = select(Price).where(Price.id == price_id)
        try:
            result = await self._db.execute(query)
            price = result.scalar_one()
            for attr, value in price_update.dict().items():
                setattr(price, attr, value)
            await self._db.commit()
            await self._db.refresh(price)
            return price
        except NoResultFound:
            return None

    async def patch_price(self, price_id: int, price_update: PriceCreate) -> Price:
        query = select(Price).where(Price.id == price_id)
        try:
            result = await self._db.execute(query)
            price = result.scalar_one()
            for attr, value in price_update.dict().items():
                setattr(price, attr, value)
            await self._db.commit()
            await self._db.refresh(price)
            return price
        except NoResultFound:
            return None

    async def delete_price(self, price_id: int) -> Price:
        query = select(Price).where(Price.id == price_id)
        try:
            result = await self._db.execute(query)
            price = result.scalar_one()
            await self._db.delete(price)
            await self._db.commit()
            return price
        except NoResultFound:
            return None
