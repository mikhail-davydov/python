from pydantic import BaseModel, SecretStr


class Credentials(BaseModel):
    username: str
    api_key: SecretStr
    db_password: SecretStr


creds = Credentials(
    username="admin",
    api_key="sk-your-secret-api-key-12345",
    db_password="SuperSecurePassword!"
)

print(f"\n--- Использование SecretStr ---")
print(f"Username: {creds.username}")
# При обычной печати SecretStr скрывает значение
print(f"API Key (прямая печать): {creds.api_key}")  # Выведет что-то вроде "**********"
print(f"DB Password (прямая печать): {creds.db_password}")  # Выведет что-то вроде "**********"

# Для получения реального значения используется .get_secret_value()
print(f"API Key (раскрыто): {creds.api_key.get_secret_value()}")
print(f"DB Password (раскрыто): {creds.db_password.get_secret_value()}")
