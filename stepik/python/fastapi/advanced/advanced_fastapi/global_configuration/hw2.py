from functools import lru_cache
from pathlib import Path

from fastapi import Depends, FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_key: str = "default-secret"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / ".env",
        env_file_encoding="utf-8",
        # В .env есть и другие переменные — игнорируем их
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


app = FastAPI()


@app.get("/secret")
def read_secret(settings: Settings = Depends(get_settings)):
    return {"secret_key": settings.secret_key[:4] + "..."}
