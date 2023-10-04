from fastapi import APIRouter, Query, Depends
from fastapi.responses import FileResponse
from src.core.db import get_async_session
from datetime import datetime
from src.service.report_service import generate_report
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get(
    "/generate_report",
    description="Отчет за указанный период по доходу с каждого автомобиля",
)
async def generate_report(
    start_date_str: str = Query(
        ..., description="Дата начала периода в формате 'дд.мм.гггг'"
    ),
    end_date_str: str = Query(
        ..., description="Дата окончания периода в формате 'дд.мм.гггг'"
    ),
    session: AsyncSession = Depends(get_async_session),
):
    try:
        start_date = datetime.strptime(start_date_str, "%d.%m.%Y").date()
        end_date = datetime.strptime(end_date_str, "%d.%m.%Y").date()

        excel_file = await generate_report(start_date, end_date, session)

        return FileResponse(
            excel_file,
            filename=excel_file,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    except Exception as e:
        raise
