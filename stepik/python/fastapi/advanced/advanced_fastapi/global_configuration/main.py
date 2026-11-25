from fastapi import FastAPI, Depends

from config import Settings, get_settings  # Импортируем наш класс настроек и геттер

app = FastAPI()


@app.get("/settings")
async def get_app_settings(settings: Settings = Depends(get_settings)):
    """
    Возвращает текущие настройки приложения.
    """
    return {
        "app_name": settings.app_name,
        "environment": settings.environment,
        "database_url": settings.database_url,
        "secret_key_snippet": settings.secret_key[:8] + "..."
    }
