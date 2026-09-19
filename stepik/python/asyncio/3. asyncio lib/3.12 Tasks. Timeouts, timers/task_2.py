import asyncio


async def main(coroutine):
    try:
        response_limit_task = asyncio.create_task(response_limit())
        coroutine_task = asyncio.create_task(coroutine)
        timeout = await response_limit_task
        return await asyncio.wait_for(coroutine_task, timeout=timeout)
    except TimeoutError:
        print('Задача отменена, превышено время ожидания!')
        return None


async def response_limit():
    pass
