from functools import lru_cache

from fastapi import Depends, FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "sqlite:///./app.db"
    max_connections: int = 10

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


app = FastAPI()


@app.get("/db")
def read_db(cfg: Settings = Depends(get_settings)):
    return {"database_url": cfg.database_url, "max_connections": cfg.max_connections}
