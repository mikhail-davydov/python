from functools import lru_cache

from fastapi import Depends, FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    my_app_name: str = "Simple App"

    # Load only from defaults or environment variables (no .env file)
    model_config = SettingsConfigDict(env_file=None)


@lru_cache
def get_settings() -> Settings:
    return Settings()


app = FastAPI()


@app.get("/name")
def read_name(cfg: Settings = Depends(get_settings)):
    return {"my_app_name": cfg.my_app_name}
