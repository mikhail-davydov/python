from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/country/{country}")
async def list_cities(country: str, limit: int) -> dict:
    return {'country': f'{country}', 'cities': country_dict[country][:limit]}


country_dict = {
    'Russia': ['Moscow', 'St. Petersburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan'],
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia'],
}


@app.get("/users")
async def users(name: Optional[str] = 'Undefined', age: Optional[int] = 18) -> dict:
    return {'user_name': f'{name}', 'user_age': age}


@app.get("/products")
async def detail_view(item_id: int) -> dict:
    return {'product': f'Stock number {item_id}'}


@app.get("/users/admin")
async def admin() -> dict:
    return {'message': 'Hello admin'}


@app.get("/")
async def welcome() -> dict:
    return {"message": "My first project in FastAPI"}


@app.get("/hello/{user}")
async def hello(user: str) -> dict:
    return {"message": f"Hello, {user}!"}


@app.get("/user")
async def login(username: Optional[str] = None, age: Optional[int] = None) -> dict:
    return {"user": username, "age": age}


@app.get("/employee/{name}/company/{company}")
async def get_employee(name: str, department: str, company: str) -> dict:
    return {"Employee": name, "Company": company, "Department": department}
