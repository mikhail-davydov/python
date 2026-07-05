import multiprocessing
import time


def parallel_handler(tasks: list | tuple, task_args: list | tuple, timeout=None):
    processes: list[multiprocessing.Process] = []
    for task, args in zip(tasks, task_args):
        process = multiprocessing.Process(target=task, args=args, daemon=True)
        process.start()
        processes.append(process)

    end = timeout + time.perf_counter() if timeout else None
    for process in processes:
        to_wait = max(0, end - time.perf_counter()) if timeout else None
        process.join(to_wait)
        if process.is_alive():
            process.terminate()

    for process in processes:
        process.join()
        process.close()
