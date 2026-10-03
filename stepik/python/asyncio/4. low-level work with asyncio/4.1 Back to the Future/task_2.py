from asyncio import Task

import asyncio


async def simple_gather(*coros_or_futures) -> list:
    # Воспользуйтесь одной из функций для Futures (первый шаг этого урока),
    # чтобы создать список футур/задач.
    # Проинициализируйте список результатов
    # Проитерируйтесь по списку футур/задач, ожидая каждую.
    # Результаты ожиданий (успешные или исключения) добавьте в список результатов и верните его.

    results = []
    tasks: list[Task] = [
        asyncio.ensure_future(obj)
        for obj in coros_or_futures
    ]

    for task in tasks:
        try:
            result = await task
            results.append(result)
        except Exception as ex:
            results.append(ex)

    return results


# alt

async def simple_gather(*coros_or_futures) -> list:
    results = []
    futures = [asyncio.ensure_future(arg) for arg in coros_or_futures]
    for future in futures:
        try:
            result = await future
        except Exception as exc:
            result = exc
        finally:
            results.append(result)
    return results
