import asyncio
import asyncpg
from asyncpg import Connection
from contextlib import asynccontextmanager


@asynccontextmanager
async def manage_connection(**con_args):
    conn: Connection = await asyncpg.connect(**con_args)
    try:
        yield conn
    finally:
        await conn.close()


async def main():
    con_args = {"port": 5434, "user": "postgres", "password": "admin", "database": "demo"}

    async with manage_connection(**con_args) as conn:
        print(f"Подключение по адресу {conn._addr} установлено!")
        db_name = await conn.fetchval("SELECT current_database()")
        print(f"Подтверждаем, что подключились к БД: {db_name}")


if __name__ == '__main__':
    asyncio.run(main())
