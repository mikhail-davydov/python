import asyncio
from random import randint


async def client(client_id, address=('localhost', 5555)):
    reader, writer = await asyncio.open_connection(*address)
    for _ in range(randint(500, 1500)):
        msg = f'Клиент_№{client_id},{''.join([str(randint(1, 9999)) + ' ' for _ in range(randint(2, 5))])}'
        writer.write(msg.encode())
        await writer.drain()
        print(f'Отправили: {msg}')
        data = await reader.read(1024)
        print(f"Получили сообщение: {data.decode()}")
    writer.close()
    await writer.wait_closed()
    print("Закрыли соединение")


async def main():
    tasks = [client(x) for x in range(randint(50, 150))]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
