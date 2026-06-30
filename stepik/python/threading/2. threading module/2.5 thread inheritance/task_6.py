import threading
from collections.abc import Callable
from functools import wraps

sources = [
    "https://ya.ru",
    "https://www.bing.com",
    "https://www.google.ru",
    "https://www.yahoo.com",
    "https://mail.ru",
]


def get_request_header(url: str) -> dict:
    pass


def set_result(url: str):
    thread = threading.current_thread()
    thread.header = get_request_header(url)


threads = [threading.Thread(target=set_result, args=(url,)) for url in sources]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
    print(thread.header)


# alt

def set_result_header(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        thread = threading.current_thread()
        thread.header = func(*args, **kwargs)
        return thread.header

    return wrapper


get_request_header = set_result_header(get_request_header)

threads = [threading.Thread(target=get_request_header, args=(url,)) for url in sources]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
    print(thread.header)
