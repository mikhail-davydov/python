from pydantic import BaseModel


class Profile(BaseModel):
    bio: str
    age: int


class User(BaseModel):
    name: str
    profile: Profile


user = User(
    name="Alice",
    profile=Profile(bio="Python developer", age=30),
)

result = user.model_dump()
