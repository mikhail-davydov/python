from fastapi import FastAPI, Request, Response
from fastapi.routing import APIRoute, APIRouter


# Определяем новый класс, наследующийся от APIRoute
class CustomHeaderRoute(APIRoute):
    # Переопределяем метод get_route_handler
    # Этот метод возвращает асинхронную функцию, которая будет обрабатывать запрос
    def get_route_handler(self):
        # Получаем оригинальный обработчик маршрута.
        # Это та функция, которую FastAPI обычно вызывает для обработки запроса.
        original_route_handler = super().get_route_handler()

        # Определяем нашу кастомную асинхронную функцию-обработчик
        async def custom_route_handler(request: Request) -> Response:
            # Вызываем оригинальный обработчик маршрута
            # Он выполнит все обычные операции: разрешение зависимостей,
            # вызов функции эндпоинта, валидацию ответа и т.д.
            response: Response = await original_route_handler(request)

            # После того как оригинальный обработчик вернул ответ,
            # мы можем модифицировать его.
            response.headers["X-Custom-Header"] = "Hello from Custom Route!"
            return response

        # Возвращаем нашу обертку над оригинальным обработчиком
        return custom_route_handler


# Создаем собственный класс APIRouter, который будет использовать наш CustomHeaderRoute
class CustomRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        # Передаем наш CustomHeaderRoute в качестве route_class по умолчанию
        # для всех маршрутов, зарегистрированных этим роутером
        super().__init__(*args, route_class=CustomHeaderRoute, **kwargs)


app = FastAPI()

# Создаем экземпляр нашего кастомного роутера
custom_router = CustomRouter()


# Регистрируем маршрут, используя методы нашего custom_router
@custom_router.get("/items")
async def read_items_with_custom_header():
    """
    Этот эндпоинт будет использовать CustomHeaderRoute, потому что он
    зарегистрирован через CustomRouter.
    """
    return {"message": "Reading items with custom header via CustomRouter."}


# Включаем наш кастомный роутер в основное приложение FastAPI
app.include_router(custom_router)


# Для сравнения, обычный маршрут, зарегистрированный напрямую в app
@app.get("/users")
async def read_users():
    """
    Этот эндпоинт не будет использовать CustomHeaderRoute.
    """
    return {"message": "Reading users (no custom header)."}
