from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()


@app.get("/home")
async def home() -> JSONResponse:
    return JSONResponse(content={"page": "Home"})


@app.get("/go-home")
async def go_home() -> RedirectResponse:
    return RedirectResponse(url="/home")
