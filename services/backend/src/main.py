from fastapi import FastAPI

from src.core.config import settings
from src.api.routers import main_router



app = FastAPI(title=settings.app_title,
              description=settings.description,
              docs_url='/swagger')


app.include_router(main_router)

# @app.get("/")
# def home():

#     return "DESCRIPTION"



