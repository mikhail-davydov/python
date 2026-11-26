from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/status")
async def status() -> PlainTextResponse:
    return PlainTextResponse(content="API is running", status_code=200)
