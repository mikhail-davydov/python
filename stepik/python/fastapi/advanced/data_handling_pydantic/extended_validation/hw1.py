from pydantic import BaseModel, field_validator


class Item(BaseModel):
    item_name: str
    price: float

    @field_validator('price')
    @classmethod
    def validate_price(cls, value: float) -> float:
        if value <= 0:
            raise ValueError('Price must be positive')
        if value > 1000:
            raise ValueError('Price must not exceed 1000')
        return value


if __name__ == '__main__':
    print(Item(item_name="Book", price=19.99))

    try:
        Item(item_name="Book", price=0)
    except ValueError as e:
        print(e)

    try:
        Item(item_name="Book", price=1500)
    except ValueError as e:
        print(e)
