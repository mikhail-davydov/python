from fastapi import FastAPI, Depends
from starlette.requests import Request

app = FastAPI()


async def sub_dependency(request: Request) -> str:
    return request.method


async def main_dependency(sub_dependency_value: str = Depends(sub_dependency)) -> str:
    return sub_dependency_value


@app.get("/test/")
async def test_endpoint(test: str = Depends(main_dependency)):
    return test
