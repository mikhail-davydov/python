import asyncio


async def main(coroutines):
    try:
        async with asyncio.TaskGroup() as tg:
            [tg.create_task(coro) for coro in coroutines]
            tg.create_task(service_diag())
    except* AlarmOverheatException as g_ex:
        print('WARNING: Критическая нагрузка, текущие задачи группы отменены!')
    except* Exception as g_ex:
        for exception in g_ex.exceptions:
            print(exception)



coroutines = []
async def service_diag(): ...
class AlarmOverheatException(Exception): ...


if __name__ == '__main__':
    asyncio.run(main(coroutines))


# alt

async def main(coroutines):
    try:
        async with asyncio.TaskGroup() as tg:
            [tg.create_task(coro) for coro in coroutines]
            tg.create_task(service_diag())
    except* AlarmOverheatException:
        print('WARNING: Критическая нагрузка, текущие задачи группы отменены!')
    except* Exception as e:
        print(*e.exceptions, sep='\n')