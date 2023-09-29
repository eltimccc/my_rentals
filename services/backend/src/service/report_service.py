import pandas as pd
from sqlalchemy import Date, func, select
from datetime import date
from src.models.booking import BookingCar
from src.models.car import Car
from sqlalchemy.ext.asyncio import AsyncSession


async def generate_report(start_date: date, end_date: date, session: AsyncSession):
    try:
        result = await session.execute(
            select(Car.brand, func.sum(BookingCar.total_amount).label("total_revenue"))
            .join(BookingCar, Car.id == BookingCar.car_id)
            .filter(
                BookingCar.from_reserve.cast(Date) >= start_date,
                BookingCar.to_reserve.cast(Date) <= end_date,
            )
            .group_by(Car.brand)
        )

        report_df = pd.DataFrame(
            result.fetchall(), columns=["Автомобиль", "Сумма, руб."]
        )

        excel_file = "booking_report.xlsx"
        report_df.to_excel(excel_file, index=False)

        return excel_file
    except Exception as e:
        raise
