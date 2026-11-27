from pydantic import BaseModel, ConfigDict


class ORMUser:
    def __init__(self, id: int, name: str, email: str) -> None:
        self.id = id
        self.name = name
        self.email = email


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str


if __name__ == "__main__":
    orm_user = ORMUser(id=1, name="John Doe", email="john@example.com")
    user = UserSchema.model_validate(orm_user)
    print(user)
