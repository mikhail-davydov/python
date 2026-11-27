from datetime import datetime, date
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel


class UserRole(str, Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"


class UserProfile(BaseModel):
    id: UUID
    name: str
    email: str
    created_at: datetime
    birth_date: date
    role: UserRole


user_instance = UserProfile(
    id=uuid4(),
    name="Alice Johnson",
    email="alice@example.com",
    created_at=datetime.now(),
    birth_date=date(1990, 5, 15),
    role=UserRole.EDITOR
)

# Экспорт в словарь (поведение по умолчанию, equivalent to mode='python')
default_dump_dict = user_instance.model_dump()
print("Словарь (поведение по умолчанию):")
print(default_dump_dict)
# Пример вывода: {'id': UUID('...'), 'name': 'Alice Johnson', 'email': 'alice@example.com', 'created_at': datetime.datetime(...), 'birth_date': datetime.date(...), 'role': <UserRole.EDITOR: 'editor'>}
print(f"Тип created_at в словаре: {type(default_dump_dict['created_at'])}")  # <class 'datetime.datetime'>
print(f"Тип id в словаре: {type(default_dump_dict['id'])}")  # <class 'uuid.UUID'>

# mode='json' (аналог .model_dump_json)

# Экспорт в словарь в 'json' моде
json_compatible_dict = user_instance.model_dump(mode='json')
print("\nСловарь в 'json' моде:")
print(json_compatible_dict)
# Пример вывода: {'id': '...', 'name': 'Alice Johnson', 'email': 'alice@example.com', 'created_at': 'YYYY-MM-DDTHH:MM:SS.ffffff', 'birth_date': 'YYYY-MM-DD', 'role': 'editor'}
print(f"Тип created_at в словаре: {type(json_compatible_dict['created_at'])}")  # <class 'str'>
print(f"Тип id в словаре: {type(json_compatible_dict['id'])}")  # <class 'str'>

# include

# Включение только определенных полей
limited_info_dict = user_instance.model_dump(include={'name', 'email'})
print("\nСловарь с ограниченным набором полей (include):")
print(limited_info_dict)


# Вывод: {'name': 'Alice Johnson', 'email': 'alice@example.com'}

# exclude

class SecureUserProfile(UserProfile):
    password_hash: str  # Допустим, это поле, которое мы не хотим экспортировать


secure_user_instance = SecureUserProfile(
    id=uuid4(),
    name="Bob Smith",
    email="bob@example.com",
    created_at=datetime.now(),
    birth_date=date(1985, 1, 1),
    role=UserRole.VIEWER,
    password_hash="super_secret_hash"
)

# Исключение определенных полей
public_user_dict = secure_user_instance.model_dump(exclude={'password_hash', 'id'})
print("\nСловарь с исключенными полями (exclude):")
print(public_user_dict)
# Пример вывода: {'name': 'Bob Smith', 'email': 'bob@example.com', 'created_at': '...', 'birth_date': '...', 'role': 'viewer'}

# by_alias

from pydantic import Field


class Item(BaseModel):
    item_id: int = Field(alias="id")
    item_name: str = Field(alias="name")
    price: float


item_instance = Item(id=101, name="Laptop", price=1200.0)

# Экспорт без алиасов (по умолчанию)
no_alias_dict = item_instance.model_dump()
print("\nСловарь без использования алиасов:")
print(no_alias_dict)
# Вывод: {'item_id': 101, 'item_name': 'Laptop', 'price': 1200.0}

# Экспорт с использованием алиасов
with_alias_dict = item_instance.model_dump(by_alias=True)
print("Словарь с использованием алиасов:")
print(with_alias_dict)
# Вывод: {'id': 101, 'name': 'Laptop', 'price': 1200.0}

# exclude_none

from typing import Optional


class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    available_at: Optional[datetime] = None


product_instance = Product(name="Book", price=25.0)  # description и available_at будут None

# Экспорт с None значениями (по умолчанию)
default_product_dump = product_instance.model_dump()
print("\nПродукт с None значениями (по умолчанию):")
print(default_product_dump)
# Пример вывода: {'name': 'Book', 'description': None, 'price': 25.0, 'available_at': None}

# Экспорт без None значений
excluded_none_product_dump = product_instance.model_dump(exclude_none=True)
print("Продукт без None значений:")
print(excluded_none_product_dump)
# Вывод: {'name': 'Book', 'price': 25.0}
