from fastapi import FastAPI, Depends, Query

app = FastAPI()


def get_limit(limit: int = Query(10)) -> dict:
    return {"limit": limit}


@app.get("/items")
async def items(limit: dict = Depends(get_limit)) -> dict:
    return limit
