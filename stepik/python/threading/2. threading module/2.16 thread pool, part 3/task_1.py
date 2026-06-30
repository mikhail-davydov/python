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
    [pool.submit(worker, source).add_done_callback(post_worker) for source in sources]
       