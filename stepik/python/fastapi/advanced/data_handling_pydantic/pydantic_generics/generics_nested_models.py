from typing import TypeVar, Generic, List

from pydantic import BaseModel, Field, ValidationError

T = TypeVar('T')


# Модель для одного элемента списка (например, товар)
class Item(BaseModel):
    item_id: int
    name: str
    quantity: int = Field(gt=0)


# Дженерик-модель для пагинированного ответа
class PaginatedResponse(BaseModel, Generic[T]):
    total_count: int
    page_number: int
    page_size: int
    items: List[T]  # Здесь 'items' - это список параметризованного типа


# Демонстрация использования PaginatedResponse с Item
print("\n--- PaginatedResponse[Item] ---")
try:
    paginated_items = PaginatedResponse[Item](
        total_count=100,
        page_number=1,
        page_size=10,
        items=[
            {"item_id": 1, "name": "Laptop", "quantity": 1},
            {"item_id": 2, "name": "Mouse", "quantity": 5}
        ]
    )
    print(f"Успешно создано: {paginated_items.model_dump_json(indent=2)}")
    print(f"Тип items[0]: {type(paginated_items.items[0])}")  # <class '__main__.Item'>
except ValidationError as e:
    print(f"Ошибка: {e}")

print("\n--- Ошибка валидации внутри вложенного дженерик-списка ---")
try:
    # Попытка создать с некорректным количеством товара (quantity = 0)
    PaginatedResponse[Item](
        total_count=50,
        page_number=2,
        page_size=5,
        items=[
            {"item_id": 3, "name": "Keyboard", "quantity": 0}  # Quantity must be > 0
        ]
    )
except ValidationError as e:
    print(f"Ошибка валидации:\n{e}")
