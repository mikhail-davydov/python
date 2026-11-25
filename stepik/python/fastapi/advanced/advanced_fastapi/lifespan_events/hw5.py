from contextlib import asynccontextmanager

from fastapi import FastAPI, Request


class FakePool:
    def __init__(self):
        self.is_open = False

    async def open(self):
        self.is_open = True

    async def close(self):
        self.is_open = False


@asynccontextmanager
async def lifespan(app: FastAPI):
    pool = FakePool()
    await pool.open()
    app.state.pool = pool

    try:
        yield
    finally:
        await pool.close()


app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def health(request: Request):
    return {"pool_open": request.app.state.pool.is_open}
