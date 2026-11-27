from pydantic import BaseModel, ConfigDict


class ImmutablePoint(BaseModel):
    model_config = ConfigDict(frozen=True)  # Делаем модель неизменяемой
    x: int
    y: int


# frozen=True - Демонстрация
print("\n--- frozen=True ---")
point = ImmutablePoint(x=10, y=20)
print("Создана неизменяемая точка:", point)

try:
    point.x = 30  # Попытка изменить поле
    print("Успешно изменено (не должно быть):", point)
except TypeError as e:
    print(f"Ошибка при попытке изменить поле: {e}")
    # Вывод: TypeError: "ImmutablePoint" is immutable and does not support item assignment
