import asyncio
from concurrent.futures import ThreadPoolExecutor

import fastapi
import threading
import time
import uvicorn
from anyio import to_thread
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.concurrency import run_in_threadpool
from itertools import count

N = 45  # количество одновременных запросов
count_ = count(1)  # для вывода количества обработанных запросов


# AnyIO
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     to_thread.current_default_thread_limiter().total_tokens = N
#     yield


# thread pool
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.io_pool = ThreadPoolExecutor(max_workers=N, thread_name_prefix="io_thread")
    yield
    app.state.io_pool.shutdown(wait=True, cancel_futures=True)


print(f"FastAPI version: {fastapi.__version__}")
print(f"Uvicorn version: {uvicorn.__version__}")

app = FastAPI(lifespan=lifespan)


def blocking_task():
    time.sleep(0.5)
    return {"thread_name": threading.current_thread().name, "threads": threading.active_count()}


# AnyIO
# @app.get("/")
# async def read_root():
#     data = await run_in_threadpool(blocking_task)
#     return {"n": next(count_), "msg": data}


# thread pool
def get_io_pool() -> ThreadPoolExecutor:
    return app.state.io_pool


@app.get("/")
async def read_root(io_pool: ThreadPoolExecutor = Depends(get_io_pool)):
    loop = asyncio.get_running_loop()
    data = await loop.run_in_executor(io_pool, blocking_task)
    return {"n": next(count_), "msg": data}
