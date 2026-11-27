from pydantic import BaseModel, ConfigDict


class LoginForm(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    username: str
    password: str


# 3.1 str_strip_whitespace=True - Демонстрация
print("\n--- str_strip_whitespace=True ---")
login_data = {"username": "  admin  ", "password": "  mypass  "}
login_form = LoginForm.model_validate(login_data)
print(f"Исходный username: '{login_data['username']}'")
print(f"Обработанный username: '{login_form.username}'")  # Пробелы удалены
print(f"Исходный password: '{login_data['password']}'")
print(f"Обработанный password: '{login_form.password}'")  # Пробелы удалены
