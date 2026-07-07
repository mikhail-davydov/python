import multiprocessing
import traceback

er_queue = multiprocessing.Queue()


def test(er_queue: multiprocessing.Queue):
    try:
        raise ValueError("Warning! ValueError")
    except Exception as err:
        err_info = traceback.format_exc()  # Получаем информацию об исключении
        er_queue.put(err_info)  # Помещаем информацию в очередь


if __name__ == "__main__":
    process = multiprocessing.Process(target=test, args=(er_queue,))
    process.start()
    process.join()
    if not er_queue.empty():
        err_info = er_queue.get()
        raise RuntimeError(err_info)  # Передаем информацию об исключении в родительский процесс
