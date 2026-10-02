import asyncio

barrier = asyncio.Barrier(2)


async def coro():
    task_name = asyncio.current_task().get_name()
    try:
        await barrier.wait()
        print(f"<- Задача {task_name} преодолела барьер")
    except asyncio.BrokenBarrierError:
        print(f"<-! Задача {task_name} преодолела сломанный барьер!")
        print(barrier)


async def coro_abort():
    await asyncio.sleep(1)
    # await barrier.abort()
    await barrier.reset()


async def main():
    await asyncio.gather(*(coro() for _ in range(3)), coro_abort())


if __name__ == '__main__':
    asyncio.run(main())
