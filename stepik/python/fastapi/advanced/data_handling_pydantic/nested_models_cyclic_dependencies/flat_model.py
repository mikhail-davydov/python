from pydantic import BaseModel, Field, ValidationError


# Определяем вложенную модель Address
class Address(BaseModel):
    street: str
    city: str
    zip_code: str = Field(pattern=r"^\d{5}(?:[-\s]\d{4})?$")  # Пример валидации почтового индекса


# Определяем основную модель User, которая содержит поле типа Address
class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address  # Поле 'address' аннотируется как тип Address


# Демонстрация создания экземпляра User
try:
    user_data = {
        "id": 1,
        "name": "Alice Wonderland",
        "email": "alice@example.com",
        "address": {
            "street": "123 Rabbit Hole",
            "city": "Fairyland",
            "zip_code": "90210"
        }
    }
    user = User(**user_data)
    print(f"User успешно создан:\n{user.model_dump_json(indent=2)}")
    print(f"Тип user.address: {type(user.address)}")  # Покажет <class '__main__.Address'>

except ValidationError as e:
    print(f"Ошибка валидации: {e}")

# Показать ошибку валидации, если данные для address некорректны
print("\n--- Демонстрация ошибки валидации вложенной модели ---")
try:
    invalid_user_data = {
        "id": 2,
        "name": "Bob Builder",
        "email": "bob@example.com",
        "address": {
            "street": "Construction Site",
            "city": "Buildville",
            "zip_code": "ABCDEF"  # Некорректный zip_code
        }
    }
    User(**invalid_user_data)
except ValidationError as e:
    print(f"Ошибка валидации:\n{e}")
