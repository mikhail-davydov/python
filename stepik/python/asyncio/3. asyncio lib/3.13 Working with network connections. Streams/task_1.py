import asyncio
import functools
import operator


async def handle_client_request(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    data = await reader.read(1024)
    ints = list(map(int, data.decode().split()))
    primer = '*'.join(map(str, ints))
    result = f'{primer}={functools.reduce(operator.mul, ints, 1)}'

    writer.write(result.encode())
    await writer.drain()

    writer.close()
    await writer.wait_closed()


async def main(address: tuple) -> None:
    server = await asyncio.start_server(handle_client_request, *address)
    async with server:
        await server.serve_forever()


# alt

async def handler(reader, writer):
    data = await reader.read(1024)
    data = data.decode().split()
    res = functools.reduce(operator.mul, map(int, data))
    writer.write(f"{"*".join(data)}={res}".encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()
