from typing import Optional, Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/users")
async def retrieve_user_profile(
        username: Annotated[
            str,
            Query(
                description="Имя пользователя",
                min_length=2,
                max_length=50
            )
        ] = ""
) -> dict:
    return profiles_dict.get(username) or {'message': f'Пользователь {username} не найден.'}


profiles_dict = {
    'alex': {'name': 'Александр', 'age': 33, 'phone': '+79463456789', 'email': 'alex@my-site.com'},
}


@app.get("/category/{category_id}/products")
async def category(
        category_id: Annotated[
            int,
            Path(
                description="Category ID",
                gt=0
            )
        ],
        page: int = 0) -> dict:
    return {'category_id': category_id, 'page': page}


@app.get("/users/{name}")
async def get_user(
        name: Annotated[
            str,
            Path(
                min_length=4,
                max_length=20,
                description='Enter your name'
            )
        ]) -> dict:
    return {'user_name': f'{name}'}


@app.get("/user/{username}")
async def login(
        username: Annotated[
            str,
            Path(
                min_length=3,
                max_length=15,
                description='Enter your username',
                examples=['Ilya']
            )
        ],
        age: int) -> dict:
    return {"user": username, "age": age}


@app.get("/user/{username}/{age}")
async def login(
        username: str = Path(
            min_length=3,
            max_length=15,
            description='Enter your username',
            example='Custom name'
        ),
        age: int = Path(
            ge=0,
            le=100,
            description="Enter your age"
        )
) -> dict:
    return {"user": username, "age": age}


country_dict = {
    'Russia': ['Moscow', 'St. Petersburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan'],
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia'],
}


@app.get("/country/{country}")
async def list_cities(country: str, limit: int) -> dict:
    return {'country': f'{country}', 'cities': country_dict[country][:limit]}


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
