import asyncio


async def coroutine_number():
    print("1")
    await asyncio.sleep(1)
    print("2")


async def coroutine_symbol():
    print("A")
    await asyncio.sleep(1)
    print("B")


async def main():
    number_task = asyncio.create_task(coroutine_number())
    symbol_task = asyncio.create_task(coroutine_symbol())
    await number_task
    await symbol_task


if __name__ == '__main__':
    asyncio.run(main())
