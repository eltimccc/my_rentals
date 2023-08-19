from typing import Optional
from pydantic import EmailStr
from pydantic_settings import BaseSettings

LIFETIME = 3600

class Settings(BaseSettings):
    app_title: str = 'Прокат Псков set'
    description: str ='oO'
    database_url: str
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    postgres_user: str  # Добавьте это поле
    postgres_password: str  # Добавьте это поле
    postgres_db: str  # Добавьте это поле

    class Config:
        env_file = ".env"

settings = Settings()
