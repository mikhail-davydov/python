from functools import lru_cache
from typing import Literal

from fastapi import Depends, FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: Literal["dev", "test", "prod"] = "dev"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


app = FastAPI()


@app.get("/env")
def read_environment(settings: Settings = Depends(get_settings)):
    return {"environment": settings.environment}
