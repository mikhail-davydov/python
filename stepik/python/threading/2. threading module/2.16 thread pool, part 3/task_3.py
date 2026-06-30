from concurrent.futures import ThreadPoolExecutor, wait


def get_request_header(url: str) -> dict:
    ...


sources: list[str] = ...

TIMEOUT = 1.5

with ThreadPoolExecutor(max_workers=len(sources)) as pool:
    headers_stor = {source: pool.submit(get_request_header, source) for source in sources}
    done, _ = wait(headers_stor.values(), timeout=TIMEOUT)
    for source, future in headers_stor.items():
        headers_stor[source] = future.result() if future in done else 'no_response'

# alt

headers_stor = {url: 'no_response' for url in sources}

with ThreadPoolExecutor() as executor:
    futures = []
    for url in sources:
        future = executor.submit(get_request_header, url)
        future.name = url
        futures.append(future)

    done, _ = wait(futures, timeout=1.5)
    for task in done:
        headers_stor[task.name] = task.result()
