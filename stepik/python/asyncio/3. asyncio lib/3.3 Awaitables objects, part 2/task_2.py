import asyncio
from typing import Callable


async def sleep_with_callback(delay, func: Callable = None):
    await asyncio.sleep(delay)
    return func()


# alt

async def sleep_with_callback(delay, func: Callable = None):
    callback = await asyncio.sleep(delay, result=func)
    return callback()
