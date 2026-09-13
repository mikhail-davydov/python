import asyncio


async def dummy_coroutine():
    print("Успех!")


if __name__ == '__main__':
    asyncio.run(dummy_coroutine())
