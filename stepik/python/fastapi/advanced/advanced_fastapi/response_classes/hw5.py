from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()


@app.get("/check/{value}", response_model=None)
async def check(value: int) -> JSONResponse | RedirectResponse:
    if value > 10:
        return RedirectResponse(url="/high")
    return JSONResponse(content={"status": "Low value"}, status_code=200)


@app.get("/high")
async def high() -> JSONResponse:
    return JSONResponse(content={"status": "High value"})
