from fastapi import FastAPI, Depends
from starlette.requests import Request

log_user = []


def log_client(request: Request):
    log_user.append({**request.headers, **{"url": request.url.path}})


app = FastAPI(dependencies=[Depends(log_client)])


@app.get("/log_user")
async def print_log_user():
    return {"user": log_user}


@app.get("/messages")
async def messages(request: Request) -> dict:
    return {"url": request.url.path}


@app.get("/users")
async def messages(request: Request) -> dict:
    return {"url": request.url.path}


@app.get("/dummy")
async def messages(request: Request) -> dict:
    return {"url": request.url.path}
