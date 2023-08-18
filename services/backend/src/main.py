from fastapi import FastAPI
from dotenv import load_dotenv

from src.core.config import settings




load_dotenv()

app = FastAPI(title=settings.app_title,
              description=settings.description)



@app.get("/")
def home():

    return "DESCRIPTION"



