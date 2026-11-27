from pydantic import BaseModel, ValidationError, Field, field_validator


class Address(BaseModel):
    street: str = Field(min_length=3)
    city: str = Field(min_length=2)
    zip_code: str  # Например, формат XX-YYY

    @field_validator('zip_code')
    @classmethod
    def validate_zip_code_format(cls, v):
        if not (len(v) == 6 and v[2] == '-'):  # Простая проверка XX-YYY
            raise ValueError('Неверный формат почтового индекса. Ожидается XX-YYY')
        return v


class Order(BaseModel):
    order_id: str
    customer_name: str
    shipping_address: Address  # Поле типа Address
    total_amount: float = Field(gt=0)

    @field_validator('order_id')
    @classmethod
    def order_id_must_be_numeric(cls, v):
        if not v.isdigit():
            raise ValueError('ID заказа должен быть только цифрами')
        return v


if __name__ == '__main__':

    # Демонстрация
    try:
        order1 = Order(
            order_id="12345",
            customer_name="Alice Smith",
            shipping_address={
                "street": "Main St 10",
                "city": "Springfield",
                "zip_code": "12-345"
            },
            total_amount=99.99
        )
        print(f"Order успешно создан: {order1}")

        # Ошибка во вложенной модели Address (неверный zip_code)
        Order(
            order_id="67890",
            customer_name="Bob Johnson",
            shipping_address={
                "street": "Oak Avenue",
                "city": "Gotham",
                "zip_code": "ABC-XYZ"  # Неверный формат
            },
            total_amount=50.0
        )
    except ValidationError as e:
        print(f"\nОшибка во вложенной модели Address: {e}")

    try:
        # Ошибка в самой модели Order (неверный order_id)
        Order(
            order_id="ABCDE",  # Не цифры
            customer_name="Charlie",
            shipping_address={
                "street": "Elm Street",
                "city": "Metropolis",
                "zip_code": "54-321"
            },
            total_amount=25.0
        )
    except ValidationError as e:
        print(f"\nОшибка в модели Order: {e}")
