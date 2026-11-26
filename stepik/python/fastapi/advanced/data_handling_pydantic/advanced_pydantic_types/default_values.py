import datetime
import time
from typing import List

from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str
    tags: List[str] = []
    created_at: datetime.datetime = datetime.datetime.now()  # А вот здесь проблема!


product1 = Product(name="Laptop")

# Подождем немного, чтобы время точно изменилось

time.sleep(0.01)
product2 = Product(name="Mouse")

product1.tags.append("Electronics")

print(f"Product 1 Tags: {product1.tags}")  # Выведет: ['Electronics']
print(f"Product 2 Tags: {product2.tags}")  # Выведет: [] - Отлично, работает!

print(f"Product 1 Created At: {product1.created_at}")
print(f"Product 2 Created At: {product2.created_at}")  # А вот тут не работает !!!


### make it right

class Product(BaseModel):
    name: str
    tags: List[str] = []
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)  # Вот правильное использование!


product1 = Product(name="Laptop")

# Подождем немного, чтобы время точно изменилось

time.sleep(0.01)
product2 = Product(name="Mouse")

print(f"Product 1 Created At: {product1.created_at}")  # Выведет время создания product1
print(f"Product 2 Created At: {product2.created_at}")  # Выведет время создания product2, которое будет позже!
