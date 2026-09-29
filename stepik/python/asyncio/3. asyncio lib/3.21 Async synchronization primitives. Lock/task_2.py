from asyncio import Lock

lock = Lock()


async def coro():
    if lock.locked():
        await another_job()
        return

    async with lock:
        await cashed_request()


async def cashed_request():
    pass


async def another_job():
    pass
