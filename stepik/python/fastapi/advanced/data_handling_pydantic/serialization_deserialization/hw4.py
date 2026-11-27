from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str


user = User(
    name="Alice",
    email="alice@example.com",
    password="super_secret",
)

result = user.model_dump_json(exclude={"password"})
