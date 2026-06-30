from concurrent.futures import ThreadPoolExecutor, wait


def get_request_header(url: str) -> dict:
    ...


sources: list[str] = ...

TIMEOUT = 1.5

executor = ThreadPoolExecutor(max_workers=len(sources))
try:
    headers_stor = {source: executor.submit(get_request_header, source) for source in sources}
    done, _ = wait(headers_stor.values(), timeout=TIMEOUT)
    for source, future in headers_stor.items():
        headers_stor[source] = (future.exception() or future.result()) if future in done else 'no_response'
finally:
    executor.shutdown(wait=False, cancel_futures=True)


# alt

headers_stor = dict.fromkeys(sources, 'no_response')

executor = concurrent.futures.ThreadPoolExecutor()
try:
    futures = {executor.submit(get_request_header, source): source for source in sources}
    for future in concurrent.futures.wait(futures, timeout=1.5).done:
        if error := future.exception():
            headers_stor[futures[future]] = error
        else:
            headers_stor[futures[future]] = future.result()
finally:
    executor.shutdown(wait=False, cancel_futures=True)


# alt

executor = concurrent.futures.ThreadPoolExecutor()
try:
    futures = [executor.submit(get_request_header, url) for url in sources]
    concurrent.futures.wait(futures, timeout=1.5)
    headers_stor = {url: "no_response" if not future.done() else
    future.exception() if future.exception() else future.result() for url, future in zip(sources, futures)}
finally:
    executor.shutdown(wait=False, cancel_futures=True)
