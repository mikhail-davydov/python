from pydantic import BaseModel, ConfigDict


class UserInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    username: str
    email: str


if __name__ == "__main__":
    user = UserInput(username=" alice ", email=" alice@example.com ")
    print(user.username)  # alice
    print(user.email)  # alice@example.com

    try:
        UserInput(username="alice", email="alice@example.com", role="admin")
    except Exception as e:
        print(type(e).__name__, e)
