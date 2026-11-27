from pydantic import BaseModel, field_validator


class ProductModel(BaseModel):
    name: str
    price: float

    @field_validator('name', mode='before')
    @classmethod
    def strip_name(cls, value: any) -> str:
        if not isinstance(value, str):
            raise ValueError('Имя продукта должно быть строкой')
        return value.strip()


if __name__ == '__main__':
    product = ProductModel(name="  Laptop  ", price=999.99)
    print(product)  # name='Laptop' price=999.99

    try:
        ProductModel(name=123, price=999.99)
    except ValueError as e:
        print(e)  # Ошибка: Имя продукта должно быть строкой
