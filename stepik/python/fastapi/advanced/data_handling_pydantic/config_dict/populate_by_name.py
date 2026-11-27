from pydantic import BaseModel, Field, ConfigDict, ValidationError


class UserData(BaseModel):
    model_config = ConfigDict(populate_by_name=False)  # По умолчанию False
    user_name: str = Field(alias="userName")
    user_email: str = Field(alias="userEmail")


# populate_by_name=False (по умолчанию)
print("\n--- populate_by_name=False ---")
# Десериализация по алиасу (верно)
try:
    user_data1 = UserData.model_validate({"userName": "John Doe", "userEmail": "john@example.com"})
    print("Успешно (по алиасу):", user_data1.model_dump())
except ValidationError as e:
    print("Ошибка (не должно быть):", e.json(indent=2))

# Попытка десериализации по имени поля Python (вызовет ошибку)
try:
    user_data2 = UserData.model_validate({"user_name": "Jane Doe", "user_email": "jane@example.com"})
    print("Успешно (не должно быть):", user_data2.model_dump())
except ValidationError as e:
    print("Ошибка валидации (по имени поля не работает):")
    print(e.json(indent=2))  # ValidationError: Field required


# Модель с populate_by_name=True
class UserDataFlexible(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_name: str = Field(alias="userName")
    user_email: str = Field(alias="userEmail")


print("\n--- populate_by_name=True ---")
# Десериализация по алиасу (верно)
try:
    user_data3 = UserDataFlexible.model_validate({"userName": "Chris", "userEmail": "chris@example.com"})
    print("Успешно (по алиасу):", user_data3.model_dump())
except ValidationError as e:
    print("Ошибка (не должно быть):", e.json(indent=2))

# Десериализация по имени поля Python
try:
    user_data4 = UserDataFlexible.model_validate({"user_name": "Sarah", "user_email": "sarah@example.com"})
    print("Успешно (по имени поля):", user_data4.model_dump())
except ValidationError as e:
    print("Ошибка (не должно быть):", e.json(indent=2))
