import asyncio
import time


async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    while data := await reader.read(1024):
        a = time.perf_counter()
        client_name, numbers = data.decode().split(',')
        print(f'{client_name} отправил: {numbers}')
        answer = f"{'+'.join(numbers.split())}={sum(map(int, (numbers.split())))}"
        writer.write(answer.encode())
        await writer.drain()
        print(f'{client_name} получил: {answer}')
        print(f'Запрос выполнен за: {time.perf_counter() - a:2f}')
    writer.close()
    await writer.wait_closed()
    print('Сервер закрыт')


async def main(address: tuple) -> None:
    server: asyncio.Server = await asyncio.start_server(handler,
                                                        *address,
                                                        )
    async with server:
        print('Сервер запущен, ожидание подключений и запросов...')
        await server.serve_forever()


if __name__ == "__main__":
    addr = ('localhost', 5555)
    asyncio.run(main(addr))
