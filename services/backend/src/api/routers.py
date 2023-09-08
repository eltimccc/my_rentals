# app/api/routers.py
from fastapi import APIRouter


from src.api.endpoints import (
    car_router,
    price_router,
    user_router,
    contact_router,
    image_router,
)


main_router = APIRouter()

main_router.include_router(car_router)
main_router.include_router(price_router)
main_router.include_router(contact_router)
main_router.include_router(image_router)
main_router.include_router(user_router)
