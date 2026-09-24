import asyncio

ADDRESS = ("localhost", 5555)
LIMIT = 1024
SLEEP_TIME = 1


async def get_input_sum(nums):
    await asyncio.sleep(SLEEP_TIME)
    return sum(map(int, nums))


async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    data = await reader.read(LIMIT)
    client_name, msg_count, *nums = data.decode().split()
    msg_count = int(msg_count)
    while msg_count:
        print(f"Получили данные от {client_name}: {nums}")
        result = await get_input_sum(nums)
        writer.write(str(result).encode())
        await writer.drain()
        print(f"Отправили данные клиенту {client_name}: {result}")

        msg_count -= 1
        if msg_count:
            data = await reader.read(LIMIT)
            client_name, _, *nums = data.decode().split()

    writer.close()
    await writer.wait_closed()


async def main(address: tuple) -> None:
    server = await asyncio.start_server(handler, *address)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main(ADDRESS))
