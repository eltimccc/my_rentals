# app/api/routers.py
from fastapi import APIRouter


from src.api.endpoints import (
    car_router,
    price_router,
    user_router,
    contact_router,
    image_router,
    news_router,
    bookingcar_router,
    reports_router
)

main_router = APIRouter()

main_router.include_router(bookingcar_router, prefix="/booking", tags=["BOOKING"])
main_router.include_router(car_router, prefix="/cars", tags=("CARS",))
main_router.include_router(price_router, prefix="/prices", tags=("PRICES",))
main_router.include_router(contact_router, prefix="/contacts", tags=("CONTACTS",))
main_router.include_router(image_router, prefix="/img", tags=("IMAGES",))
main_router.include_router(news_router, prefix="/news", tags=("NEWS",))
main_router.include_router(user_router)
main_router.include_router(reports_router)