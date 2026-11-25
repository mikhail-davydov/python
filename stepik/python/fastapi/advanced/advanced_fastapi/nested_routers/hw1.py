from fastapi import FastAPI, APIRouter, HTTPException

app = FastAPI(title="Nested Users API")

# фейковые данные
_users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]


@app.get("/")
def app_root():
    return {"message": "Welcome to Nested Users API"}


users_router = APIRouter(prefix="/users")


@users_router.get("")
def get_users():
    return _users


@users_router.get("/{user_id}")
def get_user(user_id: int):
    for user in _users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


root_router = APIRouter()


@root_router.get("/")
def root():
    return {"message": "Welcome to the API"}


root_router.include_router(users_router)

app.include_router(root_router, prefix="/api")
