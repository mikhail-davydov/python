import asyncio
from itertools import count

condition = asyncio.Condition()
counter = count(1)
LIMIT = 7
COROS = 3


def predicate():
    n = next(counter)
    print(f"Задача {asyncio.current_task().get_name()} вызвала предикат {n} раз")
    return n >= LIMIT


async def coro_wait_for():
    async with condition:
        await condition.wait_for(predicate)


async def coro_notify():
    for i in range(1, 4):  # уведомляем каждую секунду!
        await asyncio.sleep(1)
        async with condition:
            print(f"Вызываем notify {i} раз")
            # condition.notify()
            # condition.notify(2)
            condition.notify_all()


async def main():
    await asyncio.sleep(0)
    coros = [coro_wait_for() for _ in range(COROS)]
    await asyncio.gather(*coros, coro_notify())


if __name__ == '__main__':
    asyncio.run(main())
