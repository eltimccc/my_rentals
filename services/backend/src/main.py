from fastapi import FastAPI

from src.core.config import settings
from src.api.routers import main_router
from src.core.init_db import create_first_superuser


app = FastAPI(title=settings.app_title,
              description=settings.description,
              docs_url='/swagger')


app.include_router(main_router)


@app.on_event('startup')
async def startup():
    await create_first_superuser() 



