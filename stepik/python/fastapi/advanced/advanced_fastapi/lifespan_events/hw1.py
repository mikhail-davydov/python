from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application is starting...")

    yield

    print("Application is shutting down...")


app = FastAPI(lifespan=lifespan)
