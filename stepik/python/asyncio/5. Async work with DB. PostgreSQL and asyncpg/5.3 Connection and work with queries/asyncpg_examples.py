import asyncio
import asyncpg


# get data
# fetchval
# RANGE = 10_000
#
#
# async def main():
#     conn: asyncpg.Connection = await asyncpg.connect(dsn="postgresql://postgres:admin@localhost:5434/demo")
#     result = await conn.fetchval("SELECT * FROM bookings.aircrafts_data WHERE range>$1",
#                                  RANGE,
#                                  column=1,
#                                  )
#     print(result)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

# fetchrow
# RANGE = 10_000
#
#
# async def main():
#     conn: asyncpg.Connection = await asyncpg.connect(dsn="postgresql://postgres:admin@localhost:5434/demo")
#     result: asyncpg.Record = await conn.fetchrow("SELECT * FROM bookings.aircrafts_data WHERE range>$1",
#                                                  RANGE,
#                                                  )
#     for k, v in result.items():
#         print(f"{k}: {v}")
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

# fetch
# import json
#
#
# async def main():
#     conn: asyncpg.Connection = await asyncpg.connect(dsn="postgresql://postgres:admin@localhost:5434/demo")
#     records: list[asyncpg.Record] = await conn.fetch("SELECT * FROM bookings.aircrafts_data ORDER BY range")
#     for record in records:
#         model_data = json.loads(record["model"])  # используем json для работы с данными в колонке model
#         ru_model = model_data.get("ru", "Нет данных")
#         print(f"{ru_model:<20} имеет дальность {record['range']:>6}км.")
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

# add data
# execute
# async def main():
#     conn: asyncpg.Connection = await asyncpg.connect(dsn="postgresql://postgres:admin@localhost:5434/demo")
#     status = await conn.execute("""INSERT INTO bookings.aircrafts_data (aircraft_code, model, range)
#                                 VALUES ($1, $2, $3)""",
#                                 '32N', '{"en": "Airbus A320neo", "ru": "Аэробус А320нео"}', 6850,
#                                 )
#     print(status)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


# cursor
# import json
#
#
# async def main():
#     conn: asyncpg.Connection = await asyncpg.connect(dsn="postgresql://postgres:admin@localhost:5434/demo")
#     # Оборачиваем работу с курсором в транзакцию
#     async with conn.transaction():
#         # Создаем курсор для запроса, ограничивая итерацию частями по пять строк
#         async for record in conn.cursor("SELECT * FROM bookings.aircrafts_data ORDER BY range", prefetch=5):
#             ru_model = json.loads(record['model'])['ru']
#             print(f"{ru_model:<20} имеет дальность {record['range']:>6}км.")
#
#     await conn.close()
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

# create pool
# async def main():
#     pool: asyncpg.Pool = await asyncpg.create_pool(port="5434",
#                                                    user="postgres",
#                                                    password="admin",
#                                                    database="demo",
#                                                    )
#     print(type(pool))  # Смотрим тип пула соединений
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


# pool usage
# # может быть использован с async with для выполнения запроса
# async with asyncpg.create_pool(user='postgres',
#                                command_timeout=60) as pool:
#     await pool.fetch('SELECT 1')
#
#
# # ... или для нескольких запросов в контексте одного соединения пула
# async with asyncpg.create_pool(user='postgres',
#                                command_timeout=60) as pool:
#     async with pool.acquire() as con:
#         await con.execute('''
#            CREATE TABLE names (
#               id serial PRIMARY KEY,
#               name VARCHAR (255) NOT NULL)
#         ''')
#         await con.fetch('SELECT 1')
#
#
# # или просто через await (не рекомендуется)
# pool = await asyncpg.create_pool(user='postgres', command_timeout=60)
# con = await pool.acquire()
# try:
#     await con.fetch('SELECT 1')
# finally:
#     await pool.release(con)


# pool settings
# async def main():
#     async with asyncpg.create_pool(port="5434",
#                                    user="postgres",
#                                    password="admin",
#                                    database="demo",
#                                    max_inactive_connection_lifetime=1,
#                                    ) as pool:
#         print("Всего соединений в пуле перед ожиданием:", pool.get_size())
#         await asyncio.sleep(2)
#         print("Всего соединений в пуле после ожидания:", pool.get_size())
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


# set_connect_args 1
# async def main():
#     async with asyncpg.create_pool(port="5434",
#                                    user="postgres",
#                                    password="admin",
#                                    database="demo",
#                                    max_queries=1,
#                                    ) as pool:
#         pool.set_connect_args(port="5434", user="postgres", password="admin", database="postgres")
#
#         db_name = await pool.fetchval("SELECT current_database()")
#         print(f"Подтверждаем, что подключились к БД: {db_name}")
#
#         db_name = await pool.fetchval("SELECT current_database()")
#         print(f"Подтверждаем, что подключились к БД: {db_name}")

# set_connect_args 2
# async def main():
#     async with asyncpg.create_pool(port="5434",
#                                    user="postgres",
#                                    password="admin",
#                                    database="demo",
#                                    max_inactive_connection_lifetime=1) as pool:
#         pool.set_connect_args(port="5434", user="postgres", password="admin", database="postgres")
#
#         db_name = await pool.fetchval("SELECT current_database()")
#         print(f"Подтверждаем, что подключились к БД: {db_name}")
#         await asyncio.sleep(2)
#         db_name = await pool.fetchval("SELECT current_database()")
#         print(f"Подтверждаем, что подключились к БД: {db_name}")

# set_connect_args 3
# async def main():
#     async with asyncpg.create_pool(port="5434",
#                                    user="postgres",
#                                    password="admin",
#                                    database="demo",
#                                    min_size=1,
#                                    ) as pool:
#         pool.set_connect_args(port="5434", user="postgres", password="admin", database="postgres")
#         async with pool.acquire() as conn_1, pool.acquire() as conn_2:
#             db_name = await conn_1.fetchval("SELECT current_database()")
#             print(f"Подтверждаем, что подключились к БД: {db_name}")
#             db_name = await conn_2.fetchval("SELECT current_database()")
#             print(f"Подтверждаем, что подключились к БД: {db_name}")
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


# LIFO connection queue
async def main():
    async with asyncpg.create_pool(port="5434",
                                   user="postgres",
                                   password="admin",
                                   database="demo",
                                   max_inactive_connection_lifetime=2,
                                   ) as pool:
        await asyncio.sleep(1)
        connections = [await pool.acquire() for _ in range(3)]
        for conn in connections:
            print("PID backend-процесса:", await conn.fetchval('SELECT pg_backend_pid()'))
            await pool.release(conn)

        await asyncio.sleep(1.5)
        connections = [await pool.acquire() for _ in range(3)]
        for conn in connections:
            print("PID backend-процесса:", await conn.fetchval('SELECT pg_backend_pid()'))
        for conn in connections:
            await pool.release(conn)


if __name__ == '__main__':
    asyncio.run(main())
