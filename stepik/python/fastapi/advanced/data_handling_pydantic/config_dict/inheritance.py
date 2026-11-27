from typing import Optional

from pydantic import BaseModel, ConfigDict


# Родительская модель с некоторыми настройками
class BaseSettings(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True  # Автоматически удалять пробелы из строк
    )
    id: int
    name: str


# Дочерняя модель наследуется от BaseSettings
class User(BaseSettings):
    email: str
    age: Optional[int] = None  # Новое поле


# Создаем экземпляр дочерней модели
print("\nUser модель (наследует ConfigDict от BaseSettings):")
user_data = {"id": 1, "name": "  Alice  ", "email": "alice@example.com"}

user = User.model_validate(user_data)
print("Исходный name:", user_data['name'])
print("Очищенный name (из-за str_strip_whitespace):", user.name)


###


# Родительская модель с некоторыми настройками
class BaseSettings(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,  # Автоматически удалять пробелы из строк
        extra='forbid'  # Нельзя лишние поля(по умолчанию)
    )
    id: int
    name: str


# Дочерняя модель наследуется от BaseSettings
class User(BaseSettings):
    email: str
    age: Optional[int] = None  # Новое поле


# Дочерняя модель, которая переопределяет extra
class AdminUser(User):  # Наследуется от User, которая наследуется от BaseSettings
    model_config = ConfigDict(
        extra='allow'  # Переопределяем: теперь разрешаем лишние поля

    )
    is_super_admin: bool = False
    last_login_ip: Optional[str] = None


# Создаем экземпляр AdminUser
print("\nAdminUser модель (переопределяет ConfigDict):")
admin_user_data = {
    "id": 3,
    "name": "  Charlie  ",
    "email": "charlie@admin.com",
    "is_super_admin": True,
    "department": "IT"  # Это лишнее поле
}

try:
    admin_user = AdminUser.model_validate(admin_user_data)
    print("Админ-пользователь создан:")
    print(admin_user.model_dump())
    print("Дополнительные поля (model_extra):", admin_user.model_extra)  # 'department' теперь разрешено

except TypeError as e:
    print(f"Ошибка при попытке изменить замороженное поле: {e}")
except Exception as e:
    print(f"Другая ошибка: {e}")

# Проверяем, что str_strip_whitespace все еще работает (наследуется от BaseSettings через User)
print("Исходный name для admin_user:", admin_user_data['name'])
print("Очищенный name для admin_user:", admin_user.name)
