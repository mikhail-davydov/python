from functools import lru_cache

from fastapi import Depends, FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    api_version: str = "v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="APP_",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


app = FastAPI()


@app.get("/info")
def read_info(cfg: Settings = Depends(get_settings)):
    return {"app_name": cfg.app_name, "api_version": cfg.api_version}
