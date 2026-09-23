import time

import asyncio
import random
import string

ADDRESS = ("localhost", 5555)
CLIENTS_COUNT = 10000
NAME_LENGTH = 5


def get_random_message():
    return f'{random.randint(1, 10)} {random.randint(1, 10)} {random.randint(1, 10)}'


def random_string():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=NAME_LENGTH))


async def create_client():
    msg_count = random.randint(1, 10)
    reader, writer = await asyncio.open_connection(*ADDRESS)
    client_name = random_string()

    while msg_count:
        msg = get_random_message()
        full_client_msg = f'{client_name} {msg_count} {msg}'
        start = time.perf_counter()
        writer.write(full_client_msg.encode())
        await writer.drain()
        # print(f"Клиент {client_name} отправил сообщение {msg}")

        data = await reader.read(1024)
        print(f"Клиент {client_name} получил сообщение {data.decode()} за {time.perf_counter() - start:.2f}")
        msg_count -= 1

    writer.close()
    await writer.wait_closed()
    # print(f"Клиент {client_name} закрыл соединение")


async def client() -> None:
    tasks = [asyncio.create_task(create_client()) for _ in range(CLIENTS_COUNT)]
    await asyncio.wait(tasks)


if __name__ == "__main__":
    asyncio.run(client())
