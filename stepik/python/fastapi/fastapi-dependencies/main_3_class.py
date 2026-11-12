from fastapi import FastAPI, Depends

app = FastAPI()


class Paginator:
    def __init__(self):
        self.limit = 10
        self.page = 1

    def __call__(self, limit: int):
        if limit < self.limit:
            return [{'limit': self.limit, 'page': self.page}]
        else:
            return [{'limit': limit, 'page': self.page}]


my_paginator = Paginator()


@app.get("/users")
async def all_users(pagination: list = Depends(my_paginator)):
    return {"user": pagination}
