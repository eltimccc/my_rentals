from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Прокат Псков set'
    description: str ='oO'
    database_url: str
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
