from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/hello")
async def hello() -> JSONResponse:
    return JSONResponse(
        content={"message": "Hello, API!"},
        headers={"X-API-Version": "1.0"},
    )
