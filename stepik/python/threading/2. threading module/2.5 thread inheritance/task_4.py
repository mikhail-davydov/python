import requests
import threading

sources = [
    "https://ya.ru",
    "https://www.bing.com",
    "https://www.google.ru",
    "https://www.yahoo.com",
    "https://mail.ru",
]


def get_request_header(url: str) -> dict:
    return requests.get(url).headers


class GetHeaders(threading.Thread):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.url_headers = {}

    def run(self):
        self.url_headers[self.url] = get_request_header(self.url)


threads = [GetHeaders(url) for url in sources]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

results = {}
for thread in threads:
    results.update(thread.url_headers)

# alt

results = {}
threads = []

for url in sources:
    threads.append(GetHeaders(url))
    threads[-1].start()

for thread in threads:
    thread.join()
    results |= thread.url_headers