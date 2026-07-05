import multiprocessing
import time


def handler(file: str) -> None:
    """
    Функция обработки платежей
    """
    ...


sources = ["2023_08.csv", "2023_07.csv", "2023_06.csv", "2023_05.csv", "2023_04.csv"]


def main(t: int | float):
    processes = [multiprocessing.Process(target=handler, args=[source]) for source in sources]
    for process in processes:
        process.start()
    end = t + time.perf_counter()
    for process in processes:
        to_wait = end - time.perf_counter()
        if to_wait > 0:
            process.join(to_wait)
        if process.is_alive():
            process.terminate()
            process.join()
            process.close()


if __name__ == '__main__':
    main(1)

# alt

def main(t: int | float):
    start_time = time.time()
    processes = [multiprocessing.Process(target=handler, args=(csv_file,)) for csv_file in sources]
    for process in processes:
        process.start()
    for process in processes:
        process.join(max(0, t - (time.time() - start_time)))

    for process in processes:
        if process.is_alive():
            process.terminate()

    for process in processes:
        process.join()
        process.close()