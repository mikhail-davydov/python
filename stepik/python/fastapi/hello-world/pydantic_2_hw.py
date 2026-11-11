from typing import Annotated

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


# task 5
class Note(BaseModel):
    id: int
    text: str


notes = [
    Note(id=1, text="Купить хлеб"),
    Note(id=2, text="Написать отчет"),
    Note(id=3, text="Позвонить маме"),
    Note(id=4, text="Сходить в спортзал"),
    Note(id=5, text="Прочитать книгу")
]


@app.delete("/notes/{note_id}")
async def delete_note(note_id: int) -> Note:
    for i, note in enumerate(notes):
        if note.id == note_id:
            return notes.pop(i)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Note not found"
    )

# # task 4
# # Напишите здесь ваши модели.
# class UserUpdate(BaseModel):
#     name: str
#     age: Annotated[
#         int,
#         Field(
#             gt=0
#         )
#     ]
#
#
# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#
#
# users = [
#     User(id=1, name="Алексей", age=25),
#     User(id=2, name="Мария", age=30),
#     User(id=3, name="Иван", age=22),
#     User(id=4, name="Елена", age=28),
#     User(id=5, name="Дмитрий", age=35)
# ]
#
#
# # Напишите здесь ваше решение.
# @app.put("/users/{user_id}")
# async def update_user(user_id: int, userUpdate: UserUpdate) -> User:
#     for i, user in enumerate(users):
#         if user.id == user_id:
#             updated = User(
#                 id=user_id,
#                 name=userUpdate.name,
#                 age=userUpdate.age
#             )
#             users[i] = updated
#             return updated
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

# # task 3
# class User(BaseModel):
#     id: int
#     name: str
#     email: str
#
#
# users = [
#     User(id=1, name="Алексей", email="alexey@example.com"),
#     User(id=2, name="Мария", email="maria@example.com"),
#     User(id=3, name="Иван", email="ivan@example.com"),
#     User(id=4, name="Елена", email="elena@example.com"),
#     User(id=5, name="Дмитрий", email="dmitry@example.com")
# ]
#
#
# @app.get("/users/{user_id}")
# async def get_user(user_id: int) -> User:
#     for user in users:
#         if user.id == user_id:
#             return user
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#
#
# # Напишите здесь ваше решение.
#
# # task 2
# users_2 = []
#
#
# # Напишите здесь ваше решение.
# class UserCreate(BaseModel):
#     name: str
#     age: Annotated[
#         int,
#         Field(
#             ge=18
#         )
#     ]
#
#
# class User2(BaseModel):
#     id: int
#     name: str
#     age: Annotated[
#         int,
#         Field(
#             ge=18
#         )
#     ]
#
#
# @app.post("/users")
# async def create_user(user: UserCreate) -> User2:
#     next_id = len(users_2) + 1
#     created = User2(
#         id=next_id,
#         name=user.name,
#         age=user.age
#     )
#     users_2.append(created)
#     return created
#
#
# @app.get("/users")
# async def get_users() -> list[User2]:
#     return users_2
#
#
# # task 1
# # Напишите здесь вашу модель.
# class Task(BaseModel):
#     id: int
#     title: str
#     completed: bool
#
#
# tasks = [
#     Task(id=1, title="Купить молоко", completed=False),
#     Task(id=2, title="Позвонить другу", completed=True),
#     Task(id=3, title="Сделать домашку", completed=False),
#     Task(id=4, title="Погулять с собакой", completed=True),
#     Task(id=5, title="Записаться на тренировку", completed=False)
# ]
#
#
# # Напишите здесь ваше решение.
# @app.get("/tasks")
# async def get_tasks() -> list[Task]:
#     return tasks
