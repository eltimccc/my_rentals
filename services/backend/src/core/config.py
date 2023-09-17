import os
from typing import Optional
from pydantic import EmailStr
from pydantic_settings import BaseSettings

LIFETIME = 3600
UPLOAD_FOLDER = "uploads"


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


class Settings(BaseSettings):
    app_title: str = "Прокат Псков set"
    description: str = "oO"
    database_url: str
    secret: str = "SECRET"
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    full_name: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]
    postgres_user: str
    postgres_password: str
    postgres_db: str

    class Config:
        env_file = ".env"


settings = Settings()
