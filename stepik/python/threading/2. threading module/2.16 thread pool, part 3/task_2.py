from concurrent.futures import Future, ThreadPoolExecutor


def worker(source):
    ...


sources: list = ...


def post_worker(future: Future):
    if future.exception():
        print(future.exception())
    else:
        print(f'{future.result()} saved')


with ThreadPoolExecutor(max_workers=5) as pool:
    threads = [pool.submit(worker, source) for source in sources]
for thread in threads:
    thread.add_done_callback(post_worker)