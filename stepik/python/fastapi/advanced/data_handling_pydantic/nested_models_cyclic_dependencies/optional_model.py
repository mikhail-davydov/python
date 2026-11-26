from typing import Optional

from pydantic import BaseModel, ValidationError, Field, EmailStr


# Определяем вложенную модель Address
class Address(BaseModel):
    street: str
    city: str
    zip_code: str = Field(pattern=r"^\d{5}(?:[-\s]\d{4})?$")  # Пример валидации почтового индекса


class UserProfile(BaseModel):
    user_id: int
    username: str
    contact_email: EmailStr
    shipping_address: Optional[Address] = None  # Теперь адрес необязателен


# Демонстрация поведения при None
try:
    user1 = UserProfile(user_id=1, username="user_with_address", contact_email="user1@example.com",
                        shipping_address={
                            "street": "456 Side Road",
                            "city": "Villagetown",
                            "zip_code": "67890"
                        })
    print(f"\nUserProfile с адресом:\n{user1.model_dump_json(indent=2)}")

    user2 = UserProfile(user_id=2, username="user_without_address", contact_email="user2@example.com",
                        shipping_address=None)
    print(f"\nUserProfile без адреса (shipping_address=None):\n{user2.model_dump_json(indent=2)}")

    user3 = UserProfile(user_id=3, username="user_no_address_field", contact_email="user3@example.com")
    print(f"\nUserProfile без указания shipping_address (будет None по умолчанию):\n{user3.model_dump_json(indent=2)}")

except ValidationError as e:
    print(f"Ошибка валидации: {e}")
