from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str

    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    SECRET_KEY: str
    SECRET_KEY_REFRESH: str
    ACCESS_TOKEN_EXPIRES_IN: int
    REFRESH_TOKEN_EXPIRES_IN: int

    class Config:
        env_file = './.env'


settings = Settings()
