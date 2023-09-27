# from src.models.booking import BookingCar
# from src.core.db import AsyncSessionLocal
# from sqlalchemy import func, desc, select

# async def generate_top_cars_report():
#     async with AsyncSessionLocal() as session:
#         result = (
#             await session.execute(
#                 select(
#                     BookingCar.car_id,
#                     func.sum(BookingCar.total_amount).label("total_revenue")
#                 )
#                 .group_by(BookingCar.car_id)
#                 .order_by(desc("total_revenue"))
#             )
#         )
        
#         report = result.fetchall()

#     return report