from socket import socket

import asyncio
import time

ADDRESS = ('localhost', 5555)


async def shutdown_server(server: asyncio.Server) -> None:
    await asyncio.sleep(3)  # завершаем работу сервера через 3 с.
    server.close()
    await server.wait_closed()


async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    sock: socket = writer.get_extra_info('socket')
    print(f'client address {sock.getpeername()=}')

    client = writer.get_extra_info('peername')
    print(f'client address {client=}')


async def timer_coro():
    timer = 1
    while True:
        await asyncio.sleep(1)
        print(f'{timer}')
        timer += 1


async def main(address: tuple) -> None:
    start = time.perf_counter()
    server = await asyncio.start_server(handler, *address)
    async with server:
        asyncio.create_task(shutdown_server(server))
        asyncio.create_task(timer_coro())
        try:
            await server.serve_forever()
        except asyncio.CancelledError:
            print("Работа сервера завершена!", round(time.perf_counter() - start, 2))


if __name__ == '__main__':
    asyncio.run(main(ADDRESS))
