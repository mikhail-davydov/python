import asyncio
from random import uniform


async def consumer_1():
    while True:
        await asyncio.sleep(uniform(0, 3))
        i = await my_queue.get()
        print(f"#1 извлек из очереди <- {i}")
        if i is None:
            print("#1 завершил работу")
            await my_queue.put(i)
            break
        await asyncio.sleep(uniform(0, 3))
        print(f"#1 обработал элемент {i}")


async def consumer_2():
    while True:
        await asyncio.sleep(uniform(0, 3))
        i = await my_queue.get()
        print(f"#2 извлек из очереди <- {i}")
        if i is None:
            print("#2 завершил работу")
            await my_queue.put(i)
            break
        await asyncio.sleep(uniform(0, 3))
        print(f"#2 обработал элемент {i}")


async def finalizer():
    print("Все элементы очереди обработаны!")


async def producer():
    for i in range(10):
        await asyncio.sleep(uniform(0, 1))
        await my_queue.put(i)
        print(f"положил в очередь -> {i}")
    await my_queue.put(None)


async def main():
    await asyncio.gather(producer(), consumer_1(), consumer_2())
    await finalizer()


if __name__ == '__main__':
    my_queue = asyncio.Queue(5)
    asyncio.run(main())
