from pydantic import BaseModel


class Post(BaseModel):
    post_id: int
    title: str
    content: str
    author: 'User'  # Отложенная ссылка


class User(BaseModel):
    user_id: int
    name: str
    posts: list['Post'] = []  # Отложенная ссылка


alice = User(user_id=1, name="Alice", posts=[])
post1 = Post(post_id=101, title="My First Post", content="Hello Pydantic!", author=alice)
alice.posts.append(post1)

print(alice)
print(post1)
