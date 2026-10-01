from asyncio import Semaphore

semaphore = Semaphore(2)


async def get_another_job():
    pass


async def get_data():
    pass


async def get_request():
    pass


async def semaphored_coro():
    if semaphore.locked():
        await get_another_job()
    else:
        async with semaphore:
            await get_data()
            await get_request()
