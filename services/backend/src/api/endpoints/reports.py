import pandas as pd
from fastapi.responses import FileResponse
# from src.reports.rep import generate_top_cars_report
from fastapi import APIRouter

router = APIRouter()

@router.get("/top_cars_report_excel")
async def top_cars_report_excel():
    # Получите данные для отчета
    pass