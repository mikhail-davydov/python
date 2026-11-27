from pydantic import BaseModel, field_validator, ValidationInfo


class UserModel(BaseModel):
    username: str
    password: str

    @field_validator('password')
    @classmethod
    def check_password_username(cls, value: str, info: ValidationInfo) -> str:
        username = info.data.get('username')
        if username and value == username:
            raise ValueError('Пароль не должен совпадать с именем пользователя')
        return value


if __name__ == '__main__':
    try:
        UserModel(username="john", password="john")
    except ValueError as e:
        print(e)  # Ошибка: Пароль не должен совпадать с именем пользователя
