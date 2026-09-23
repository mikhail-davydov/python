import asyncio
from time import perf_counter

sources = [
    "https://yandex.ru",
    "https://www.bing.com",
    "https://www.google.ru",
    "https://www.yahoo.com",
    "https://mail.ru",
    "https://яndex.ru",
    "https://www.youtube.com",
    "https://www.porshe.de",
    "https://www.whatsapp.com",
    "https://www.baidu.com",
]

sum_ex_time = 0


async def get_status(url: str) -> str:
    global sum_ex_time
    start_tmp = perf_counter()
    try:
        _, hostname = url.rsplit("//")

        reader, writer = await asyncio.open_connection(hostname, 443, ssl=True)

        query = (
            f"HEAD / HTTP/1.1\r\n"
            f"Host: {hostname}\r\n"
            f"\r\n"
        )
        writer.write(query.encode())
        await writer.drain()

        status = None
        while True:
            line = await reader.readline()
            text = line.decode().rstrip()
            if not text:
                break
            if 'http'.upper() in text:
                status = text.split(maxsplit=1)[-1]
        writer.close()
        await writer.wait_closed()

        return status
    except Exception as ex:
        return str(ex)
    finally:
        delta = perf_counter() - start_tmp
        print(f"Ответ от {url} получен за {delta:.2f}c.")
        sum_ex_time += delta


async def main():
    tasks = [asyncio.create_task(get_status(source)) for source in sources]
    # results = await asyncio.gather(*tasks, return_exceptions=True)
    for task in tasks:
        await task
    print()
    for url, task in zip(sources, tasks):
        print(url, task.exception() or task.result())


if __name__ == '__main__':
    start_time = perf_counter()
    asyncio.run(main())
    print(f"Выполнено за: {perf_counter() - start_time:.2f}с.")
    print(f"Сумма времени всех запросов: {sum_ex_time:.2f}с.")
