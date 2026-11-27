from typing import TypeVar, Generic

from pydantic import BaseModel, ValidationError

T = TypeVar('T')  # Определяем переменную типа T


class ApiResponse(BaseModel, Generic[T]):
    status: str
    message: str
    data: T  # Вот здесь используется переменная типа 'T'


# Определим простую модель User для использования в дженерике
class User(BaseModel):
    id: int
    name: str
    email: str


# --- Создание экземпляров с конкретными типами ---

print("\n--- ApiResponse[User] ---")
try:
    user_response = ApiResponse[User](
        status="success",
        message="User profile data",
        data={
            "id": 1,
            "name": "Alice",
            "email": "alice@example.com"
        }
    )
    print(f"Успешно создано: {user_response.model_dump_json(indent=2)}")
    print(f"Тип данных: {type(user_response.data)}")  # <class '__main__.User'>
except ValidationError as e:
    print(f"Ошибка: {e}")

# --- Демонстрация автоматической валидации ---

print("\n--- Ошибка валидации: Ожидается int, получена str ---")
try:
    # Здесь Pydantic попытается преобразовать "not_an_int" в int и выдаст ошибку
    invalid_int_response = ApiResponse[int](
        status="error",
        message="Invalid data type",
        data="not_an_int"
    )
    print(f"Успешно создано: {invalid_int_response.model_dump_json(indent=2)}")
except ValidationError as e:
    print(f"Ошибка валидации:\n{e}")

print("\n--- Ошибка валидации: Некорректные данные для User ---")
try:
    # Здесь Pydantic попытается создать User, но поле 'id' некорректно
    invalid_user_response = ApiResponse[User](
        status="error",
        message="Invalid user data",
        data={
            "id": "abc",  # Должно быть число
            "name": "Bob",
            "email": "bob@example.com"
        }
    )
    print(f"Успешно создано: {invalid_user_response.model_dump_json(indent=2)}")
except ValidationError as e:
    print(f"Ошибка валидации:\n{e}")
