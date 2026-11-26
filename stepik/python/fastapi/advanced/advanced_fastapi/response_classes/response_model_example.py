from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


# Внутренняя модель данных, возможно, из вашей базы данных
class UserInDB(BaseModel):
    id: int
    name: str
    email: EmailStr
    hashed_password: str  # Чувствительное поле, которое не должно уходить клиенту
    is_active: bool = True


# Модель ответа, которую мы будем показывать клиенту
class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr


# Эндпоинт для получения пользователя по ID
@app.get("/users/{user_id}", response_model=UserPublic)
async def read_user(user_id: int):
    # Предположим, это данные, полученные из базы данных
    user_from_db = UserInDB(
        id=user_id,
        name=f"User {user_id}",
        email=f"user{user_id}@example.com",
        hashed_password=f"supersecret{user_id}",  # Это поле будет отфильтровано
        is_active=True
    )
    # Мы возвращаем объект UserInDB. FastAPI автоматически:
    # 1. Проверит его на соответствие UserPublic.
    # 2. Отфильтрует поле 'hashed_password' (и 'is_active', если UserPublic его не содержит).
    # 3. Сериализует оставшиеся поля в JSON.
    return user_from_db

# Запустите Uvicorn: uvicorn your_module_name:app --reload
# Перейдите: GET http://127.0.0.1:8000/users/1
# Вы увидите JSON-ответ:
# {
#   "id": 1,
#   "name": "User 1",
#   "email": "user1@example.com"
# }
# Поле 'hashed_password' не будет в ответе!
