from typing import List

from pydantic import BaseModel, Field, ValidationError


class Item(BaseModel):
    product_id: int = Field(gt=0)
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)


class Order(BaseModel):
    order_id: str
    customer_id: int
    items: List[Item]  # Список вложенных моделей Item


# Демонстрация создания, сериализации и валидации
try:
    order_data = {
        "order_id": "ORD-001",
        "customer_id": 101,
        "items": [
            {"product_id": 1, "quantity": 2, "price": 10.50},
            {"product_id": 2, "quantity": 1, "price": 25.00}
        ]
    }
    order = Order(**order_data)
    print(f"\nOrder успешно создан:\n{order.model_dump_json(indent=2)}")
    print(f"Тип order.items[0]: {type(order.items[0])}")  # Покажет <class '__main__.Item'>

except ValidationError as e:
    print(f"Ошибка валидации: {e}")

# Демонстрация ошибки валидации внутри списка
print("\n--- Демонстрация ошибки валидации вложенного списка ---")
try:
    invalid_order_data = {
        "order_id": "ORD-002",
        "customer_id": 102,
        "items": [
            {"product_id": 3, "quantity": 0, "price": 5.00},  # quantity = 0 (некорректно)
            {"product_id": 4, "quantity": 1, "price": -1.00}  # price = -1.00 (некорректно)
        ]
    }
    Order(**invalid_order_data)
except ValidationError as e:
    print(f"Ошибка валидации:\n{e}")
