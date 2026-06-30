import threading

stor_local = threading.local()

info_threads = {}


def spyder_info_threads():
    current = threading.current_thread()
    info_threads[current.name] = stor_local.__dict__


# alt

def spyder_info_threads():
    name = threading.current_thread().name
    info_threads[name] = {'url': stor_local.url, 'method': stor_local.method, 'key': stor_local.key}
