from typing import TypeVar, Generic, Dict

from pydantic import BaseModel, ValidationError

# Определяем две переменные типа: для ключа (K) и для значения (V)
K = TypeVar('K')
V = TypeVar('V')


class ConfigStore(BaseModel, Generic[K, V]):
    # Здесь K будет типом ключей словаря, V - типом значений
    settings: Dict[K, V]
    description: str = "A generic configuration store."


# Демонстрация использования
print("--- ConfigStore с ключами str и значениями int ---")
try:
    int_config = ConfigStore[str, int](
        settings={"timeout": 60, "retries": 3},
        description="Integer settings"
    )
    print(f"Успешно создано: {int_config.model_dump_json(indent=2)}")
except ValidationError as e:
    print(f"Ошибка: {e}")

print("\n--- ConfigStore с ключами str и значениями bool ---")
try:
    bool_config = ConfigStore[str, bool](
        settings={"feature_a_enabled": True, "debug_mode": False},
        description="Boolean flags"
    )
    print(f"Успешно создано: {bool_config.model_dump_json(indent=2)}")
except ValidationError as e:
    print(f"Ошибка: {e}")

print("\n--- Ошибка: Ожидается int, получена str ---")
try:
    # Попытка передать некорректный тип значения
    ConfigStore[str, int](
        settings={"timeout": "not_an_int"},
        description="Invalid config"
    )
except ValidationError as e:
    print(f"Ошибка валидации:\n{e}")
