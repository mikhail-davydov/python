from concurrent.futures import ThreadPoolExecutor
from typing import Any


def get_request_header(url: str) -> dict: ...
sources: list[Any] = ...


headers_stor = {}

with ThreadPoolExecutor() as pool:
    results = pool.map(get_request_header, sources)
    for source, result in zip(sources, results):
        headers_stor[source] = result

# alt

with ThreadPoolExecutor(max_workers=len(sources)) as executor:
    headers = executor.map(get_request_header, sources)

headers_stor = dict(zip(sources, headers))