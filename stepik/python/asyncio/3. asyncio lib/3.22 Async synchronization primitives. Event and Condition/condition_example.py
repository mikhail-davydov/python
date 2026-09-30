import asyncio

condition = asyncio.Condition()
ready = False


async def waiter(name):
    async with condition:
        print(f"{name}: жду...")
        await condition.wait_for(lambda: ready)  # ждём, пока ready станет True
        print(f"{name}: поехали!")


async def setter():
    global ready
    await asyncio.sleep(1)

    async with condition:
        ready = True
        condition.notify_all()  # будим ВСЕХ
        print("Сигнал подан!")


async def main():
    await asyncio.gather(
        waiter("A"),
        waiter("B"),
        waiter("C"),
        setter(),
    )


asyncio.run(main())
