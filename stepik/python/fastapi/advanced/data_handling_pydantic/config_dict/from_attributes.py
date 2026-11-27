from datetime import datetime

from pydantic import BaseModel, ConfigDict, ValidationError


# Простой класс-заглушка, имитирующий ORM-объект
class SQLAlchemyUser:
    def __init__(self, id, name, email, created_at):
        self.id = id
        self.name = name
        self.email = email
        self.created_at = created_at


# Модель Pydantic с from_attributes=True
class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # Ключевая настройка!
    id: int
    name: str
    email: str
    created_at: datetime


print("\n--- from_attributes=True ---")
# Создаем фиктивный ORM-объект
db_user_instance = SQLAlchemyUser(
    id=1,
    name="Grace Hopper",
    email="grace@example.com",
    created_at=datetime(2023, 1, 1, 10, 0, 0)
)

try:
    # Инициализация Pydantic модели прямо из ORM-объекта
    user_schema_instance = UserSchema.model_validate(db_user_instance)
    print("Успешно десериализовано из ORM-объекта:")
    print(user_schema_instance.model_dump_json(indent=2))
except ValidationError as e:
    print("Ошибка валидации (не должно быть):", e.json(indent=2))


# Без from_attributes=True это бы не сработало напрямую:
class UserSchemaNoFromAttributes(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime


print("\n--- Без from_attributes=True ---")
try:
    # Здесь Pydantic будет искать ключи в словаре, а не атрибуты объекта
    user_schema_fail = UserSchemaNoFromAttributes.model_validate(db_user_instance)
    print("Успешно (не должно быть):", user_schema_fail.model_dump())
except ValidationError as e:
    print("Ошибка валидации (попытка десериализации объекта без from_attributes):")
    print(e.json(indent=2))  # ValidationError: input is not a valid dictionary or model
