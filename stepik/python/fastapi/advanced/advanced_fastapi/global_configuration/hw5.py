from functools import lru_cache

from fastapi import Depends, FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


app = FastAPI()


@app.get("/log")
def read_log_level(settings: Settings = Depends(get_settings)):
    return {"log_level": settings.log_level}
