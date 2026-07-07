from collections.abc import Callable


def crypto_utils(text: str) -> tuple[str, float]:
    if text.startswith("a"):
        return "aaa45678", 3.14159
    if text.startswith("b"):
        return "bbb45678", 2.777
    return "12345678", 1.001


text_blocks = ("allocation", "bombshell", "doom")

from multiprocessing import shared_memory, Process

from multiprocessing.managers import SharedMemoryManager


class Encrypter(Process):
    def __init__(self, text_block: str, shareable_list: shared_memory.ShareableList, index: int):
        super().__init__()
        self.text_block = text_block
        self.shareable_list = shareable_list
        self.index = index

    def run(self):
        unique_str, quality = crypto_utils(self.text_block)

        # Распаковываем кортеж в отдельные элементы ShareableList
        # Элемент 2*i: unique_str
        # Элемент 2*i+1: quality (как float)
        self.shareable_list[2 * self.index] = unique_str
        self.shareable_list[2 * self.index + 1] = quality


def main():
    results = {}

    with SharedMemoryManager() as shm_mng:
        shareable_list = shared_memory.ShareableList([""] * (len(text_blocks) * 2))

        processes = []

        # Создаем и запускаем процессы
        for i, text_block in enumerate(text_blocks):
            proc = Encrypter(text_block, shareable_list, i)
            processes.append(proc)
            proc.start()

        # Ждем завершения всех процессов
        for proc in processes:
            proc.join()

        # Собираем результаты из ShareableList
        for i, text in enumerate(text_blocks):
            unique_str = shareable_list[2 * i]
            quality = shareable_list[2 * i + 1]
            results[unique_str] = (text, quality)

        print(results)


if __name__ == '__main__':
    main()


# alt

def handler(func: Callable, func_args: Any, store: SharedMemoryManager.ShareableList):
    store[0], store[1] = func(func_args)


if __name__ == '__main__':
    with SharedMemoryManager() as smm:
        smm_stores = [smm.ShareableList(range(2)) for text in text_blocks]

        processes = [Process(target=handler, args=(crypto_utils, text_block, sharable_list))
                     for text_block, sharable_list in zip(text_blocks, smm_stores)]

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        results = {encrypted[0]: (text_block, encrypted[1]) for text_block, encrypted in zip(text_blocks, smm_stores)}

        print(results)
