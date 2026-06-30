from concurrent.futures import ThreadPoolExecutor, Future

import time


def foo(n):
    time.sleep(n)
    return f"Результат_{n:.1f}"


with ThreadPoolExecutor(max_workers=5) as pool:
    futures: list[Future] = [pool.submit(foo, n / 10) for n in range(1, 16)]
    time.sleep(0.1)

    # импортируйте необходимое. Верхняя граница решения
    from concurrent.futures import TimeoutError

    results = []
    futures_not_done = []
    end = 1 + time.perf_counter()

    for future in futures:
        to_wait = end - time.perf_counter()
        try:
            results.append(future.result(to_wait))
        except TimeoutError:
            futures_not_done.append(future)
    # нижняя граница решения

    print(len(results))  # 8 результатов
    print(len(futures_not_done))  # 7 неготовых футур


# alt

# импортируйте необходимое
from concurrent.futures import wait

done, pending = wait(futures, timeout=1)
results = [fut.result() for fut in done]
futures_not_done = list(pending)

