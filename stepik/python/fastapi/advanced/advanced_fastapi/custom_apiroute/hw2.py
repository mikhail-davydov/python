from uuid import uuid4
from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.routing import APIRoute


class RequestIdRoute(APIRoute):
    def get_route_handler(self):
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            request_id = request.headers.get("X-Request-ID")
            if not request_id or not request_id.strip():
                request_id = str(uuid4())

            response = await original_route_handler(request)
            response.headers["X-Request-ID"] = request_id
            return response

        return custom_route_handler


app = FastAPI()

router = APIRouter(route_class=RequestIdRoute)


@router.get("/orders/{order_id}")
async def get_order(order_id: int) -> dict:
    return {"order_id": order_id}


app.include_router(router)
