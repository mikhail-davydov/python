from typing import Optional

from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    role: str


class Company(BaseModel):
    company_name: str
    manager: Optional['Employee'] = None  # Строковая аннотация и значение по умолчанию
