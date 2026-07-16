import time


def task(a, b, c):
    if not isinstance(a, int | float):
        raise TypeError("not a number!")
    time.sleep(a / 10)
    return sum((a, b, c))


def data_gen():
    yield 1, 2, 3
    yield 10, 20, 30
    yield "a", "b", "c"
    yield 1.0, 2.0, 3.0


# Ваше решение

from multiprocessing.pool import Pool

if __name__ == '__main__':
    with Pool() as pool:
        apply_results = [pool.apply_async(task, it) for it in data_gen()]
        result = []
        for apply_result in apply_results:
            try:
                result.append(apply_result.get())
            except Exception as err:
                result.append(err)
        print(result)

# alt

from multiprocessing.pool import Pool


def tmp_task(a, b, c):
    try:
        ans = task(a, b, c)
        return ans
    except Exception as err:
        return err


if __name__ == '__main__':
    with Pool() as pool:
        result = pool.starmap(tmp_task, data_gen())
        print(result)
