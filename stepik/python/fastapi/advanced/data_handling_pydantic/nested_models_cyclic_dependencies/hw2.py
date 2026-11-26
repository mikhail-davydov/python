from typing import List

from pydantic import BaseModel


class Item(BaseModel):
    item_name: str
    price: float


class Order(BaseModel):
    order_id: int
    items: 'List[Item]'  # Строковая аннотация для отложенного определения
