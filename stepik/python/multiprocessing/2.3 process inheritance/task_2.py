import multiprocessing
import time


def worker(file: str):
    ...


class CSVHandler(multiprocessing.Process):
    def __init__(self, files: list[str] | tuple[str] = None, worker: callable = None, timeout: int = 1):
        super().__init__()
        self.files = files
        self.worker = worker
        self.timeout = timeout

    def run(self):
        context = multiprocessing.get_context()
        processes = [context.Process(target=self.worker, args=[file]) for file in self.files]
        for process in processes:
            process.start()
        time.sleep(self.timeout)
        for i, process in enumerate(processes):
            if process.is_alive():
                print(f'{self.files[i]} processing timeout exceeded')
                process.terminate()
        for process in processes:
            process.join()
            process.close()


if __name__ == '__main__':
    filenames = ['file_1.csv', 'file_2.csv', 'file_3.csv', ....]  # список файлов CSV для обработки
    csv_worker = CSVHandler(filenames, worker)
    csv_worker.timeout = ...
    csv_worker.start()
