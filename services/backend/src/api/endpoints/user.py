from http import HTTPStatus
from typing import List
from fastapi import APIRouter, HTTPException
from src.core.db import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.user import current_superuser
from src.crud.base import CRUDBase
from src.models.user import User
from fastapi import APIRouter, Depends, HTTPException

from src.core.user import auth_backend, fastapi_users
from src.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

user_crud = CRUDBase(User)


@router.get(
    "/users/",
    tags=("For admin",),
    response_model=List[UserRead],
    dependencies=[Depends(current_superuser)],
    description="Получение всех пользователей",
)
async def get_users(session: AsyncSession = Depends(get_async_session)):
    users = await user_crud.get_multi(session)
    return users


@router.delete("/users/{id}", tags=("users",), deprecated=True)
def delete_user(id: str):
    """Не используйте удаление, деактивируйте пользователей."""
    raise HTTPException(
        status_code=HTTPStatus.METHOD_NOT_ALLOWED,
        detail="Удаление пользователей запрещено!",
    )
