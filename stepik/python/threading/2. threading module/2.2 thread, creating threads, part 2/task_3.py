from time import sleep

headers_stor = {}

sources = [
    "bing.com",
    "google.ru",
    "yahoo.com",
    "mail.ru",
    "ya.ru",
]


def get_request_header(url: str):
    # моделируем различное время ответа от ресурсов
    if url == "yahoo.com":
        sleep(10)
    elif url == "mail.ru":
        sleep(1.8)
    elif url == "google.ru":
        sleep(0.2)
    else:
        sleep(1.4)
    headers_stor[url] = "ok"


import threading

# Ваше решение
source_threads = [threading.Thread(target=get_request_header, args=[source], name=source, daemon=True)
                  for source in sources]
for thread in source_threads:
    headers_stor.setdefault(thread.name, 'no_response')
    thread.start()

for thread in source_threads:
    thread.join(1.5 / len(source_threads))

# Работа тестирующей системы:
for url, headers in sorted(headers_stor.items()):
    print(f"{url}: {headers}")


# alt

def spawn_threads():
    threads = [threading.Thread(target=get_request_header, args=(url,)) for url in sources]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


pr_thr = threading.Thread(target=spawn_threads, daemon=True)
pr_thr.start()
pr_thr.join(1.5)

# alt

headers_stor = dict.fromkeys(sources, 'no_response')
thrs = [threading.Thread(target=get_request_header, args=(source,), daemon=True) for source in sources]
for thr in thrs:
    thr.start()
sleep(1.5)
