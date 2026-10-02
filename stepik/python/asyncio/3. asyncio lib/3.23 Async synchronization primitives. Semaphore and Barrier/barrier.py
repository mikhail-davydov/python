import asyncio

barrier = asyncio.Barrier(3)


async def coro():
    task_name = asyncio.current_task().get_name()
    print(f"-> Задача {task_name} выполняет этап №1")
    n = await barrier.wait()
    if n == 2:
        print(f" !-> Задача {task_name} что-то делает после этапа №1")
    print(f"\t-> Задача {task_name} выполняет этап №2")
    n = await barrier.wait()
    if n == 2:
        print(f" \t!-> Задача {task_name} что-то делает после этапа №2")
    print(f"\t\t-> Задача {task_name} выполняет этап №3")
    n = await barrier.wait()
    if n == 2:
        print(f" \t\t!-> Задача {task_name} что-то делает после этапа №3")
    print(f"\t\t\t-> Задача {task_name} выполняет этап №4")


async def main():
    await asyncio.gather(*(coro() for _ in range(3)))


if __name__ == '__main__':
    asyncio.run(main())
