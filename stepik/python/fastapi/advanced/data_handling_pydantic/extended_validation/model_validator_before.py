from typing import Dict, Any

from pydantic import BaseModel, ValidationError, model_validator


class Item(BaseModel):
    item_id: str
    quantity: int

    @model_validator(mode='before')
    @classmethod # <-- Это важно для mode = before!!!
    def remap_legacy_id(cls, values: Dict[str, Any]):
        if 'legacy_id' in values and 'item_id' not in values:
            values['item_id'] = values.pop('legacy_id')  # Переименовываем и удаляем старый ключ
        return values


if __name__ == '__main__':

    # Демонстрация работы `mode='before'`
    try:
        item1 = Item(item_id="A123", quantity=5)
        print(f"Успех (стандартный ввод): {item1}")
    except ValidationError as e:
        print(f"Ошибка: {e}")

    try:
        item2 = Item(legacy_id="B456", quantity=10)  # Используем старый ключ
        print(f"Успех (с переименованным legacy_id): {item2}")
    except ValidationError as e:
        print(f"Ошибка: {e}")

    try:
        Item(some_other_id="C789", quantity=2)  # Отсутствует ожидаемый item_id или legacy_id
    except ValidationError as e:
        print(f"\nОшибка валидации: {e}")
