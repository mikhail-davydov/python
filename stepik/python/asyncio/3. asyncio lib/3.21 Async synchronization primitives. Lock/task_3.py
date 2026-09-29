from asyncio import Lock
from typing import Literal

import asyncio

type Number = int | float


class TimeoutLock(Lock):
    async def acquire(self, timeout: Number = None):
        return await asyncio.wait_for(super().acquire(), timeout)


lock = TimeoutLock()


async def coro(timeout: Number = None):
    try:
        await lock.acquire(timeout)
    except TimeoutError:
        pass
    finally:
        await cashed_request()
        if lock.locked():
            lock.release()


async def cashed_request():
    pass


# alt

class TimeoutLock(Lock):
    async def acquire(self, timeout: Number = None) -> Literal[True]:
        try:
            return await asyncio.wait_for(super().acquire(), timeout)
        except TimeoutError:
            return True


lock = TimeoutLock()


async def coro(timeout: Number = None):
    await lock.acquire(timeout)
    await cashed_request()
    if lock.locked():
        lock.release()


# alt

class TimeoutLock(asyncio.Lock):

    async def acquire(self, timeout=None):
        try:
            async with asyncio.timeout(timeout):
                await super().acquire()
        except asyncio.TimeoutError:
            pass


lock = TimeoutLock()


async def coro(timeout=None):
    await lock.acquire(timeout=timeout)
    await cashed_request()
    if lock.locked():
        lock.release()