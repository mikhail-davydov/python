from concurrent.futures import ThreadPoolExecutor, wait


def get_request_header(url: str) -> dict:
    ...


sources: list[str] = ...

TIMEOUT = 1.5
headers_stor = {url: 'no_response' for url in sources}

executor = ThreadPoolExecutor(max_workers=len(sources))
try:
    futures = []
    for url in sources:
        future = executor.submit(get_request_header, url)
        future.name = url
        futures.append(future)

    done, _ = wait(futures, timeout=TIMEOUT)
    for task in done:
        headers_stor[task.name] = task.result()
finally:
    executor.shutdown(wait=False, cancel_futures=True)
