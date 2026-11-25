from fastapi import APIRouter, Body, FastAPI, HTTPException, Request, Response
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute


class ValidationRoute(APIRoute):
    def get_route_handler(self):
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                return await original_route_handler(request)
            except RequestValidationError as exc:
                body = await request.body()
                raise HTTPException(
                    status_code=422,
                    detail={
                        "errors": jsonable_encoder(exc.errors()),
                        "body": body.decode("utf-8"),
                    },
                )

        return custom_route_handler


app = FastAPI()

router = APIRouter(route_class=ValidationRoute)


@router.post("/numbers")
async def sum_numbers(numbers: list[int] = Body(...)) -> int:
    return sum(numbers)


app.include_router(router)
