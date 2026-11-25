from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseModel):
    host: str = "localhost"
    port: int = 5432


class Settings(BaseSettings):
    database: DatabaseSettings = DatabaseSettings()

    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_prefix="APP_",
    )
