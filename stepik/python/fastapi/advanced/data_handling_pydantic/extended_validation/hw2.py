from pydantic import BaseModel, field_validator


class User(BaseModel):
    name: str

    @field_validator('name')
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value or not value.replace(' ', '').isalpha():
            raise ValueError('Name must contain only letters and spaces')
        return value


if __name__ == '__main__':
    print(User(name="John Doe"))

    try:
        User(name="")
    except ValueError as e:
        print(e)

    try:
        User(name="John123")
    except ValueError as e:
        print(e)
