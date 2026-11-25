from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.request_count = 0
    print("Request counter initialized")

    yield

    print(f"Total requests: {app.state.request_count}")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    app.state.request_count += 1
    return {"message": "Hello, World!"}
