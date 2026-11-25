import os
from contextlib import asynccontextmanager

from fastapi import FastAPI

FILE_PATH = "temp.txt"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # При запуске создаём временный файл в текущей директории
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        file.write("Hello, FastAPI!")
    print("Temporary file created")

    try:
        yield
    finally:
        # При завершении работы удаляем файл, если он существует
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
            print("Temporary file deleted")


app = FastAPI(lifespan=lifespan)
