import time
from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.routing import APIRoute


class TimedRoute(APIRoute):
    def get_route_handler(self):
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            start_time = time.perf_counter()
            response: Response = await original_route_handler(request)
            elapsed = max(0.0, time.perf_counter() - start_time)
            response.headers["X-Response-Time"] = str(elapsed)
            return response

        return custom_route_handler


app = FastAPI()

router = APIRouter(route_class=TimedRoute)


@router.get("/timed")
async def timed_endpoint():
    return {"message": "timed"}


@app.get("/plain")
async def plain_endpoint():
    return {"message": "plain"}


app.include_router(router)
