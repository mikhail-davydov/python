from asyncio import Task

import asyncio


class AsyncSimpleIterator:
    def __init__(self, n: int = 0):
        print("Инициализация")
        self.n = n
        self.count = 0

    def __aiter__(self):
        print("Вызов aiter, возвращение экземпляра объекта AsyncSimpleIterator")
        return self

    async def __anext__(self):
        print("Вызов anext, запрос очередного элемента")
        await asyncio.sleep(0)  # <-!
        self.count += 1
        if self.count > self.n:
            print("Возбуждение StopAsyncIteration, завершение итерации")
            raise StopAsyncIteration
        return self.count


async def coro():
    for _ in range(3):
        await asyncio.sleep(0)
        print("\t\t+ выполнение корутины !!!")
    return 'Success!'


def callback(task: Task):
    print(task.cancelled())
    print(task.exception() or task.result())


async def main():
    task = asyncio.create_task(coro())
    task.add_done_callback(callback)
    async for elem in AsyncSimpleIterator(3):
        print(f"\tполучил {elem=}")


if __name__ == '__main__':
    asyncio.run(main())
