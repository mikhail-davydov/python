from pydantic import BaseModel, ValidationError, ConfigDict


# Модель с extra='forbid'
class StrictUser(BaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
    email: str


print("\n--- extra='forbid' ---")
valid_data = {"name": "Alice", "email": "alice@example.com"}
try:
    user1 = StrictUser.model_validate(valid_data)
    print("Успешно (валидные данные):", user1.model_dump())
except ValidationError as e:
    print("Ошибка валидации (не должно быть):", e.json(indent=2))

invalid_data_forbid = {"name": "Bob", "email": "bob@example.com", "age": 30}
try:
    user2 = StrictUser.model_validate(invalid_data_forbid)
    print("Успешно (не должно быть):", user2.model_dump())
except ValidationError as e:
    print("Ошибка валидации (лишнее поле 'age'):")
    print(e.json(indent=2))  # ValidationError: Field 'age' is not permitted


# Модель с extra='ignore'
class LenientUser(BaseModel):
    model_config = ConfigDict(extra='ignore')
    name: str
    email: str


print("\n--- extra='ignore' ---")
data_with_extra_ignore = {"name": "Charlie", "email": "charlie@example.com", "city": "London"}
try:
    user3 = LenientUser.model_validate(data_with_extra_ignore)
    print("Успешно (лишнее поле 'city' проигнорировано):", user3.model_dump())
    # Поле 'city' не будет доступно через user3.city
except ValidationError as e:
    print("Ошибка валидации (не должно быть):", e.json(indent=2))


# Модель с extra='allow'
class FlexibleUser(BaseModel):
    model_config = ConfigDict(extra='allow')
    name: str
    email: str


print("\n--- extra='allow' ---")
data_with_extra_allow = {"name": "David", "email": "david@example.com", "phone": "123-456-7890"}
try:
    user4 = FlexibleUser.model_validate(data_with_extra_allow)
    print("Успешно (лишнее поле 'phone' добавлено):", user4.model_dump())
    print("Дополнительные поля (model_extra):", user4.model_extra)  # 'phone' будет здесь
except ValidationError as e:
    print("Ошибка валидации (не должно быть):", e.json(indent=2))
