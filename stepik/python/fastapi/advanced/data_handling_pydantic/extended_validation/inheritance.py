from pydantic import BaseModel, ValidationError, EmailStr, field_validator


class BaseUser(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool = True

    @field_validator('username')
    @classmethod
    def username_must_be_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('Username должен содержать только буквы и цифры')
        return v

    @field_validator('id')
    @classmethod
    def id_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('ID должен быть положительным числом')
        return v


class AdminUser(BaseUser):  # AdminUser наследует от BaseUser
    is_admin: bool = True
    admin_level: int = 1

    @field_validator('admin_level')
    @classmethod
    def admin_level_must_be_valid(cls, v):
        if not 1 <= v <= 10:
            raise ValueError('Уровень администратора должен быть от 1 до 10')
        return v


if __name__ == '__main__':

    try:
        user = BaseUser(id=1, username="johndoe123", email="john@example.com")
        print(f"BaseUser успешно создан: {user}")

        admin = AdminUser(id=2, username="superadmin", email="admin@company.com", admin_level=5)
        print(f"\nAdminUser успешно создан: {admin}")

        # Ошибка в BaseUser (небуквенно-цифровое имя пользователя)
        BaseUser(id=3, username="user with space", email="fail@example.com")
    except ValidationError as e:
        print(f"\nОшибка BaseUser: {e}")

    try:
        # Ошибка в AdminUser (admin_level вне диапазона)
        AdminUser(id=4, username="testadmin", email="test@company.com", admin_level=15)
    except ValidationError as e:
        print(f"\nОшибка AdminUser: {e}")
