async def s():
    for symbol in "abc":
        await asyncio.sleep(0)
        print(symbol)


async def m():
    for symbol in "АБВГДЕ":
        await asyncio.sleep(0)
        print(symbol)
    raise ValueError("Ё, wtf?")


async def xl():
    for n in range(10, 16):
        await asyncio.sleep(0)
        print(n)


import asyncio


async def main():
    task_1 = asyncio.create_task(s())
    task_2 = asyncio.create_task(m())
    task_3 = asyncio.create_task(xl())
    await task_1
    try:
        await task_2
    except:
        pass
    await task_3


if __name__ == '__main__':
    asyncio.run(main())


# alt

async def main():
    task_1 = asyncio.create_task(s())
    task_2 = asyncio.create_task(m())
    task_3 = asyncio.create_task(xl())
    await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)


# alt


def cb(task: asyncio.Task) -> None:
    try:
        task.result()
    except Exception:
        pass


async def main():
    task_1 = asyncio.create_task(s())
    task_2 = asyncio.create_task(m())
    task_2.add_done_callback(cb)
    task_3 = asyncio.create_task(xl())
    await task_3


# alt


def handler(task: asyncio.Task):
    task._log_traceback = None


async def main():
    task_1 = asyncio.create_task(s())
    task_2 = asyncio.create_task(m())
    task_2.add_done_callback(handler)
    task_3 = asyncio.create_task(xl())
    await task_1
    # await task_2
    await task_3
