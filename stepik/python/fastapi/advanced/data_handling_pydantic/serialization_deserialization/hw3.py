from pydantic import BaseModel


class Item(BaseModel):
    item_name: str
    price: float


class Order(BaseModel):
    order_id: int
    items: list[Item]


order = Order(
    order_id=1,
    items=[
        Item(item_name="Laptop", price=1200.0),
        Item(item_name="Mouse", price=25.5),
    ],
)

result = order.model_dump_json()
