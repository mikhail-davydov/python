import asyncio
import contextvars
import time

timer_var = contextvars.ContextVar('timer')


async def shutdown_server(server: asyncio.Server) -> None:
    now = time.perf_counter()
    while now - timer_var.get() < 1:
        await asyncio.sleep(1)
        now = time.perf_counter()
    server.close()
    await server.wait_closed()


async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    client = writer.get_extra_info('peername')
    print(f'client address {client=}')

    now = time.perf_counter()
    timer_var.set(now)
    data = await reader.read(1024)
    res = await worker(data.decode())
    writer.write(str(res).encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main(address: tuple) -> None:
    start = time.perf_counter()
    timer_var.set(start)
    server = await asyncio.start_server(handler, *address)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        asyncio.create_task(shutdown_server(server))
        try:
            await server.serve_forever()
        except asyncio.CancelledError:
            print("Работа сервера завершена!", round(time.perf_counter() - start, 2))


async def worker(param):
    print(param)


if __name__ == '__main__':
    address = ('localhost', 5555)
    asyncio.run(main(address))

# alt

handlers = set()


async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    handlers.add(writer)
    data = await reader.read(1024)
    res = await worker(data.decode())
    writer.write(str(res).encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()
    handlers.remove(writer)


async def monitor_connections(server: asyncio.Server) -> None:
    while True:
        await asyncio.sleep(1)
        if not handlers:
            server.close()
            await server.wait_closed()
            return


async def main(address: tuple) -> None:
    server = await asyncio.start_server(handler, *address)
    async with server:
        monitor_task = asyncio.create_task(monitor_connections(server))
        try:
            await server.serve_forever()
        except asyncio.CancelledError:
            print("Работа сервера завершена!")


# alt

class Monitor:
    def __init__(self, handler):
        self._handler = handler
        self._server = None
        self._task = None
        self.count = 0

    def for_server(self, server: asyncio.Server):
        self._server = server
        return self

    async def __aenter__(self):
        # запускаем мониторинг
        self._task = asyncio.create_task(self._check())
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # останавливаем мониторинг
        self._task.cancel()
        self._server = None

    async def __call__(self, *args, **kwargs):
        self.count += 1
        try:
            await self._handler(*args, **kwargs)
        finally:
            self.count -= 1

    async def _check(self):
        while True:
            await asyncio.sleep(1)
            if not self.count:
                self._server.close()
                await self._server.wait_closed()
                break


async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    data = await reader.read(1024)
    res = await worker(data.decode())
    writer.write(res.encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main(address: tuple) -> None:
    monitor = Monitor(handler)
    server = await asyncio.start_server(monitor, *address)
    async with server, monitor.for_server(server):
        try:
            await server.serve_forever()
        except asyncio.CancelledError:
            print('Работа сервера завершена!')
