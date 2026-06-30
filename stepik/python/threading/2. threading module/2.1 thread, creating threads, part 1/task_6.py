import requests  # модуль требует установки!
import threading

sources = [
    "https://ya.ru",
    "https://www.bing.com",
    "https://www.google.ru",
    "https://www.yahoo.com",
    "https://mail.ru",
]

headers_stor = {}


def get_request_header(url: str) -> None:
    headers_stor[url] = requests.get(url).headers


source_threads = [threading.Thread(target=get_request_header, args=[source]) for source in sources]
for thread in source_threads:
    thread.start()
for thread in source_threads:
    thread.join()

# alt

tr = []
for url in sources:
    t = threading.Thread(target=get_request_header, args=(url,))
    t.start()
    tr.append(t)
for t in tr:
    t.join()
