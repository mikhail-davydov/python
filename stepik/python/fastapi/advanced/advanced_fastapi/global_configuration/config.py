from functools import lru_cache  # Импортируем lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


# Наш класс настроек для приложения
class Settings(BaseSettings):
    # Имя приложения - по умолчанию "MyApp"
    app_name: str = "MyApp"
    # Режим работы: "development", "testing" или "production"
    environment: Literal["development", "testing", "production"] = "development"
    # URL для подключения к базе данных
    database_url: str = "sqlite:///./local.db"
    # Секретный ключ для различных операций
    secret_key: str = "super_insecure_default_key"

    model_config = SettingsConfigDict(
        env_file=".env",  # Pydantic будет искать файл .env
        env_file_encoding="utf-8"  # Указываем кодировку файла
    )


# Функция, которая будет возвращать синглтон-экземпляр настроек
@lru_cache()  # Декоратор кэширует результат первого вызова
def get_settings() -> Settings:
    print("Загрузка настроек...")  # Это сообщение появится только один раз при первом запуске
    return Settings()
