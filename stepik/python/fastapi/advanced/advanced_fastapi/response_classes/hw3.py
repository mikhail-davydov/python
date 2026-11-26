from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/welcome", response_class=HTMLResponse)
async def welcome() -> HTMLResponse:
    return HTMLResponse(content="<h1>Welcome to FastAPI</h1>")
