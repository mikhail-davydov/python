from multiprocessing.pool import Pool

if __name__ == '__main__':
    with Pool() as pool:
        result = pool.starmap(task, data_gen())
        print(result)


def task(a, b, c):
    ...


def data_gen():
    ...
