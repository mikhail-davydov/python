import asyncio

import asyncpg


class DBConnectionContext:
    def __init__(self, **kwargs):
        self.conn_kwargs = kwargs

    async def __aenter__(self):
        self.conn = await asyncpg.connect(**self.conn_kwargs)
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()


async def main():
    con_args = {"port": 5434, "user": "postgres", "password": "admin", "database": "demo"}

    async with DBConnectionContext(**con_args) as conn:
        print(f"Подключение по адресу {conn._addr} установлено!")
        db_name = await conn.fetchval("SELECT current_database()")
        print(f"Подтверждаем, что подключились к БД: {db_name}")


if __name__ == '__main__':
    asyncio.run(main())
