from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import categories, products, users, reviews, cart, orders, payments

# Создаём приложение FastAPI
app = FastAPI(
    title="FastAPI Интернет-магазин",
    version="0.1.0",
)

app_v1 = FastAPI(
    title="My API v1",
    description="API v1",
)

app_v2 = FastAPI(
    title="My API v2",
    description="API v2",
)

app.mount("/v1", app_v1)
app.mount("/v2", app_v2)

# app.mount("/media", StaticFiles(directory="media"), name="media")

# Подключаем маршруты
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(users.router)
app.include_router(reviews.router)
app.include_router(cart.router)
app.include_router(orders.router)
app.include_router(payments.router)


# Корневой эндпоинт для проверки
@app.get("/")
async def root():
    """
    Корневой маршрут, подтверждающий, что API работает.
    """
    return {"message": "Добро пожаловать в API интернет-магазина!"}


@app_v1.get("/")
async def v1_root():
    """
    Корневой маршрут, подтверждающий, что API v1 работает.
    """
    return {"message": "Добро пожаловать в API v1 интернет-магазина!"}


@app_v2.get("/")
async def v2_root():
    """
    Корневой маршрут, подтверждающий, что API v2 работает.
    """
    return {"message": "Добро пожаловать в API v2 интернет-магазина!"}


if __name__ == "__main__":
    import uvicorn

    app.mount("/media", StaticFiles(directory="../media"), name="media")
    uvicorn.run(app, host="0.0.0.0", port=8000)
else:
    app.mount("/media", StaticFiles(directory="media"), name="media")