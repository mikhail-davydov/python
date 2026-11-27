from typing import Generic, TypeVar

from pydantic import BaseModel, ValidationError

T = TypeVar("T")


class DataContainer(BaseModel, Generic[T]):
    data: T


if __name__ == "__main__":
    print("--- DataContainer[str] ---")
    str_container = DataContainer[str](data="some text")
    print(f"Успешно создано: {str_container.model_dump_json(indent=2)}")

    print("\n--- DataContainer[int] ---")
    int_container = DataContainer[int](data=42)
    print(f"Успешно создано: {int_container.model_dump_json(indent=2)}")

    print("\n--- Ошибка валидации: ожидается int ---")
    try:
        DataContainer[int](data="not_an_int")
    except ValidationError as e:
        print(f"Ошибка валидации:\n{e}")
