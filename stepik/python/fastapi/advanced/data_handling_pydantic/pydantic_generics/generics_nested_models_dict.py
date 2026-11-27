from typing import TypeVar, Generic, Dict

from pydantic import BaseModel, ValidationError

# Определяем переменные типов
K = TypeVar('K')
V = TypeVar('V')


# Делаем ConfigItem обобщённым
class ConfigItem(BaseModel, Generic[V]):
    key_name: str
    value_data: V


# ConfigStore использует ConfigItem
class ConfigStore(BaseModel, Generic[K, V]):
    settings: Dict[K, ConfigItem[V]]  # Словарь с ConfigItem
    description: str = "A generic configuration store."


# Демонстрация использования
print("--- ConfigStore с ключами str и значениями int ---")
try:
    int_config = ConfigStore[str, int](
        settings={
            "timeout": ConfigItem(key_name="timeout", value_data=60),
            "retries": ConfigItem(key_name="retries", value_data=3)
        },
        description="Integer settings"
    )
    print(f"Успешно создано: {int_config.model_dump_json(indent=2)}")
except ValidationError as e:
    print(f"Ошибка: {e}")

print("\n--- ConfigStore с ключами str и значениями bool ---")
try:
    bool_config = ConfigStore[str, bool](
        settings={
            "feature_a_enabled": ConfigItem(key_name="feature_a_enabled", value_data=True),
            "debug_mode": ConfigItem(key_name="debug_mode", value_data=False)
        },
        description="Boolean flags"
    )
    print(f"Успешно создано: {bool_config.model_dump_json(indent=2)}")
except ValidationError as e:
    print(f"Ошибка: {e}")

print("\n--- Ошибка: Ожидается int, получена str ---")
try:
    invalid_config = ConfigStore[str, int](
        settings={
            "timeout": ConfigItem(key_name="timeout", value_data="not_an_int")
        },
        description="Invalid config"
    )
except ValidationError as e:
    print(f"Ошибка валидации:\n{e}")
