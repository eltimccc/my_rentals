import contextlib

from fastapi_users.exceptions import UserAlreadyExists
from pydantic import EmailStr

from src.core.config import settings
from src.core.db import get_async_session
from src.core.user import get_user_db, get_user_manager
from src.schemas.user import UserCreate
from typing import Optional


get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(
    email: EmailStr,
    password: str,
    full_name: str,
    phone_number: str,
    address: str,
    is_superuser: bool = False,
):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user_create = UserCreate(
                        email=email,
                        password=password,
                        is_superuser=is_superuser,
                        full_name=full_name,
                        phone_number=phone_number,
                        address=address,
                    )
                    await user_manager.create(user_create)
    except UserAlreadyExists:
        pass


async def create_first_superuser():
    if (
        settings.first_superuser_email is not None
        and settings.first_superuser_password is not None
    ):
        await create_user(
            email=settings.first_superuser_email,
            password=settings.first_superuser_password,
            is_superuser=True,
            full_name=settings.full_name,
            phone_number=settings.phone_number,
            address=settings.address,
        )
