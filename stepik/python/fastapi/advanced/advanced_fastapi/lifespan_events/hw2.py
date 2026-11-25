import time
from contextlib import asynccontextmanager

from fastapi import FastAPI

# Глобальная переменная для времени запуска приложения
start_time = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global start_time

    # Фиксируем время при запуске приложения
    start_time = time.time()

    try:
        yield
    finally:
        # При завершении работы вычисляем и выводим время работы приложения
        end_time = time.time()
        print(f"Application ran for {end_time - start_time:.2f} seconds")


app = FastAPI(lifespan=lifespan)
