import asyncio


async def main(aws, *, timeout=None):
    for task in asyncio.as_completed(aws, timeout=timeout):
        try:
            print(await task)
        except TimeoutError:
            print('Завершение по таймауту!')
            break
        except Exception as ex:
            print(ex)
