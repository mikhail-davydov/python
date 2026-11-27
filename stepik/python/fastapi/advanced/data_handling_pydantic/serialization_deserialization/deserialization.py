from datetime import datetime, date
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, ValidationError


# Определим простую Pydantic-модель
class UserRole(str, Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"


class UserProfile(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    age: int = Field(gt=0, le=120)  # Возраст от 1 до 120
    email: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)
    birth_date: date
    role: UserRole = UserRole.VIEWER


if __name__ == '__main__':

    # Пример "сырых" входных данных (обычно это приходит из JSON)
    data_dict = {
        "name": "Иван Петров",
        "age": 30,
        "email": "ivan.petrov@example.com",
        "is_active": "true",  # Обратите внимание, это строка!
        "birth_date": "1995-01-15",  # И это строка!
        "role": "admin"
    }

    # Десериализация и валидация
    try:
        user_profile_instance = UserProfile.model_validate(data_dict)
        print("Успешно десериализовано и провалидировано:")
        print(user_profile_instance)
    except ValidationError as e:
        print("Ошибка валидации:", e)

    try:
        user_profile_instance = UserProfile.model_validate(data_dict)
        print("Успешно десериализовано и провалидировано:")
        print(user_profile_instance)

        print(f"Тип id: {type(user_profile_instance.id)}")
        print(f"Тип age: {type(user_profile_instance.age)}")
        print(f"Тип is_active: {type(user_profile_instance.is_active)}")
        print(f"Тип created_at: {type(user_profile_instance.created_at)}")
        print(f"Тип birth_date: {type(user_profile_instance.birth_date)}")
        print(f"Тип role: {type(user_profile_instance.role)}")

    except ValidationError as e:
        print("Ошибка валидации:", e)
