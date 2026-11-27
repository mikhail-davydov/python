from pydantic import BaseModel, field_validator


class UserModel(BaseModel):
    username: str
    password: str

    @field_validator('username')
    @classmethod
    def validate_username(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError('Имя пользователя должно содержать минимум 3 символа')
        if not value.isalnum():
            raise ValueError('Имя пользователя должно содержать только буквы и цифры')
        return value.lower()

    @field_validator('password', mode='after')  # <-- mode default
    @classmethod
    def validate_password(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError('Пароль должен содержать минимум 8 символов')
        return value


if __name__ == '__main__':
    user = UserModel(username="JohnDoe123", password="securepassword123")
    print(user)

    try:
        UserModel(username="ab", password="short")
    except ValueError as e:
        print(e)
