from datetime import datetime
from decimal import Decimal
from typing import Annotated

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, EmailStr, PositiveInt, NonNegativeInt, SecretStr

app = FastAPI()


class User(BaseModel):
    username: Annotated[
        str,
        Field(
            min_length=5,
            max_length=20,
            description="Пользовательское имя, от 5 до 20 символов"
        )
    ]
    password: Annotated[
        SecretStr,
        Field(
            min_length=8,
            max_length=50,
            description="Пароль, от 8 до 50 символов"
        )
    ]
    email: Annotated[
        EmailStr,
        Field(
            description="Электронная почта"
        )
    ]
    first_name: Annotated[
        str | None,
        Field(
            default=None,
            min_length=2,
            max_length=30,
            description="Имя, от 2 до 30 символов"
        )
    ]
    last_name: Annotated[
        str | None,
        Field(
            default=None,
            min_length=2,
            max_length=30,
            description="Фамилия, от 2 до 30 символов"
        )
    ]
    is_active: Annotated[
        bool,
        Field(
            default=True,
            description="Учётная запись активна"
        )
    ]
    is_staff: Annotated[
        bool,
        Field(
            default=False,
            description="Является служебным пользователем"
        )
    ]
    is_superuser: Annotated[
        bool,
        Field(
            default=False,
            description="Является суперпользователем"
        )
    ]
    date_joined: Annotated[
        datetime,
        Field(
            default_factory=datetime.now,
            description="Зарегистрирован"
        )
    ]
    last_login: Annotated[
        datetime | None,
        Field(
            default=None,
            description="Последнее посещение"
        )
    ]


class Post(BaseModel):
    author_id: Annotated[
        PositiveInt,
        Field(
            description="Идентификатор автора"
        )
    ]
    title: Annotated[
        str,
        Field(
            max_length=100,
            description="Заголовок записи, не более 100 символов"
        )
    ]
    description: Annotated[
        str | None,
        Field(
            default=None,
            max_length=250,
            description="Описание записи, не более 250 символов"
        )
    ]
    content: Annotated[
        str,
        Field(
            description="Контент записи"
        )
    ]
    created_at: Annotated[
        datetime,
        Field(
            default_factory=datetime.now,
            description="Запись создана"
        )
    ]
    updated_at: Annotated[
        datetime | None,
        Field(
            default=None,
            description="Запись обновлена"
        )
    ]
    is_published: Annotated[
        bool,
        Field(
            default=False,
            description="Запись опубликована"
        )
    ]
    tags: Annotated[
        list[str],
        Field(
            default_factory=list,
            description="Теги записи"
        )
    ]


class Product(BaseModel):
    product_slug: Annotated[
        str,
        Field(
            min_length=3,
            max_length=120,
            pattern=r"^[a-zA-Z0-9-_]+$",
            description="Слаг продукта"
        )
    ]
    name: Annotated[
        str,
        Field(
            min_length=3,
            max_length=100,
            description="Название продукта"
        )
    ]
    price: Annotated[
        Decimal,
        Field(
            gt=0,
            description="Цена продукта"
        )
    ]
    stock: Annotated[
        NonNegativeInt,
        Field(
            default=0,
            description="Количество продукта на складе"
        )
    ]


class Address(BaseModel):
    user_id: Annotated[
        PositiveInt,
        Field(
            description="Идентификатор пользователя"
        )
    ]
    city: Annotated[
        str,
        Field(
            min_length=2,
            max_length=100,
            description="Город"
        )
    ]
    street: Annotated[
        str,
        Field(
            min_length=2,
            max_length=200,
            description="Улица"
        )
    ]
    postal_code: Annotated[
        PositiveInt,
        Field(
            ge=101000,
            le=999999,
            description="Почтовый индекс"
        )
    ]


class Order(BaseModel):
    order_id: Annotated[
        PositiveInt,
        Field(
            description="Уникальный идентификатор заказа"
        )
    ]
    user_id: Annotated[
        PositiveInt,
        Field(
            description="Идентификатор пользователя, сделавшего заказ"
        )
    ]
    total_amount: Annotated[
        Decimal,
        Field(
            ge=0,
            description="Общая сумма заказа"
        )
    ]
    created_at: Annotated[
        datetime,
        Field(
            description="Дата и время создания заказа"
        )
    ]


class Task(BaseModel):
    title: Annotated[
        str,
        Field(
            min_length=1,
            max_length=100,
            description="Название задачи"
        )
    ]
    description: Annotated[
        str | None,
        Field(
            default=None,
            max_length=500,
            description="Описание задачи"
        )
    ]
    is_completed: Annotated[
        bool,
        Field(
            default=False,
            description="Статус завершения задачи"
        )
    ]


# class User(BaseModel):
#     username: Annotated[
#         str,
#         Field(
#             min_length=3,
#             max_length=50,
#             description="Имя пользователя"
#         )
#     ]
#     email: Annotated[
#         EmailStr,
#         Field(
#             description="Электронная почта пользователя"
#         )
#     ]
#     is_active: Annotated[
#         bool,
#         Field(
#             default=True,
#             description="Статус активности пользователя"
#         )
#     ]


#


# Модель для входных данных (запросов: создание и обновление)
class MessageCreate(BaseModel):
    content: str


# Модель для ответов и хранения в базе данных
class Message(BaseModel):
    id: int
    content: str


# Инициализируем messages_db как список объектов Message
messages_db: list[Message] = [
    Message(id=0, content="First post in FastAPI")
]


# GET /messages: Возвращает весь список сообщений
@app.get("/messages", response_model=list[Message])
async def read_messages() -> list[Message]:
    return messages_db


# GET /messages/{message_id}: Получение одного сообщения по ID
@app.get("/messages/{message_id}", response_model=Message)
async def read_message(message_id: int) -> Message:
    for message in messages_db:
        if message.id == message_id:
            return message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


# POST /messages: Создание нового сообщения
@app.post("/messages", response_model=Message, status_code=status.HTTP_201_CREATED)
async def create_message(message_create: MessageCreate) -> Message:
    # Генерируем новый ID на основе максимального существующего
    next_id = max((msg.id for msg in messages_db), default=-1) + 1
    new_message = Message(id=next_id, content=message_create.content)
    messages_db.append(new_message)
    return new_message


# PUT /messages/{message_id}: Обновление существующего сообщения
@app.put("/messages/{message_id}", status_code=status.HTTP_200_OK, response_model=Message)
async def update_message(message_id: int, message_create: MessageCreate) -> Message:
    for i, message in enumerate(messages_db):
        if message.id == message_id:
            updated_message = Message(id=message_id, content=message_create.content)
            messages_db[i] = updated_message
            return updated_message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


# DELETE /messages/{message_id}: Удаление одного сообщения
@app.delete("/messages/{message_id}", status_code=status.HTTP_200_OK)
async def delete_message(message_id: int) -> dict:
    for i, message in enumerate(messages_db):
        if message.id == message_id:
            messages_db.pop(i)
            return {"detail": f"Message ID={message_id} deleted!"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


# DELETE /messages: Удаление всех сообщений
@app.delete("/messages", status_code=status.HTTP_200_OK)
async def delete_messages() -> dict:
    messages_db.clear()
    return {"detail": "All messages deleted!"}
