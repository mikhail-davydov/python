# Импортируем BaseModel из Pydantic
from pydantic import BaseModel, ValidationError


# Определяем нашу первую модель пользователя
class User(BaseModel):
    id: int  # 'id' - целое число
    name: str  # 'name' - строка
    age: int  # 'age' - целое число
    email: str  # 'email' - строка
    is_active: bool = True  # 'is_active' - булево, по умолчанию True


# 1. Корректные данные: Pydantic успешно создаст экземпляр
valid_user_data = {
    "id": 101,
    "name": "Иван Иванов",
    "age": 28,
    "email": "ivan.ivanov@example.com"
}
user_1 = User(**valid_user_data)  # Распаковываем словарь в аргументы
print(f"Пользователь 1 (корректные данные): {user_1}")
print(f"ID: {user_1.id}, Имя: {user_1.name}, Активен: {user_1.is_active}")
print("-" * 30)

# 2. Недостающее обязательное поле: Pydantic выбросит ValidationError
missing_field_data = {
    "id": 102,
    "name": "Петр Петров",
    "age": 35
    # Поле 'email' отсутствует!
}
try:
    user_2 = User(**missing_field_data)
except ValidationError as e:
    print(f"Ошибка при создании пользователя 2 (недостающее поле):")
    print(e)
print("-" * 30)

# 3. Некорректный тип данных: Pydantic также выбросит ValidationError
incorrect_type_data = {
    "id": 103,
    "name": "Анна Сидорова",
    "age": "тридцать",  # Ошибка: ожидается int, получена строка
    "email": "anna.sidorova@example.com"
}
try:
    user_3 = User(**incorrect_type_data)
except ValidationError as e:
    print(f"Ошибка при создании пользователя 3 (некорректный тип):")
    print(e)
print("-" * 30)

# 4. Дополнительное поле: Pydantic по умолчанию игнорирует неизвестные поля
extra_field_data = {
    "id": 104,
    "name": "Мария Кузнецова",
    "age": 22,
    "email": "maria.kuznetsova@example.com",
    "city": "Москва"  # Это поле не определено в нашей модели User
}
user_4 = User(**extra_field_data)
print(f"Пользователь 4 (дополнительное поле 'city'): {user_4}")
# Обратите внимание, что 'city' не появится в объекте user_4, так как оно было проигнорировано.
# Мы можем настроить это поведение далее по курсу с помощью ConfigDict.
