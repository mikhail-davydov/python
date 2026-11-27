from pydantic import BaseModel, ConfigDict, Field


class UserPayload(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    full_name: str = Field(alias="fullName")
    age: int


if __name__ == "__main__":
    user_by_alias = UserPayload(fullName="John Doe", age=30)
    print(user_by_alias)

    user_by_name = UserPayload(full_name="Jane Doe", age=25)
    print(user_by_name)

    print(user_by_alias.model_dump(by_alias=True))
