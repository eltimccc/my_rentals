from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/{booking_id}",
)
async def get_booking_by_id():
    pass
