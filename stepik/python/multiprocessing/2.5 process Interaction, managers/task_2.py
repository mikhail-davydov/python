def crypto_utils(text: str) -> tuple[str, float]:
    if text.startswith("a"):
        return "aaa45678", 3.14159
    if text.startswith("b"):
        return "bbb45678", 2.777
    return "12345678", 1.001


text_blocks = ("allocation", "bombshell", "doom")

from multiprocessing import Process


class Encrypter(Process):
    def __init__(self, text_block: str, shared_dict: dict):
        super().__init__()
        self.text_block = text_block
        self.shared_dict = shared_dict

    def run(self):
        self.shared_dict[self.text_block] = crypto_utils(self.text_block)


def main():
    results = {}

    processes = []
    sync_manager: SyncManager = multiprocessing.Manager()
    shared_dict = sync_manager.dict()

    for text_block in text_blocks:
        proc = Encrypter(text_block, shared_dict)
        processes.append(proc)
        proc.start()

    for proc in processes:
        proc.join()

    for text in text_blocks:
        unique_str = shared_dict[text][0]
        quality = shared_dict[text][1]
        results[unique_str] = (text, quality)

    print({k: v for k, v in sorted(results.items())})


if __name__ == '__main__':
    main()

# alt dict

from multiprocessing.managers import SyncManager
import multiprocessing


class Encrypter(multiprocessing.Process):
    def __init__(self, block_text: str = "",
                 sync_manager: SyncManager = None, ):
        super().__init__()
        self.cipher = self.score = None
        self.block_text = block_text
        self.sync_manager = sync_manager

    def run(self):
        self.cipher, self.score = crypto_utils(self.block_text)
        self.sync_manager[self.cipher] = (self.block_text, self.score)


if __name__ == "__main__":
    sm_dict = multiprocessing.Manager().dict()
    process = [Encrypter(text, sm_dict) for text in text_blocks]
    for pr in process:
        pr.start()
    for pr in process:
        pr.join()
    print(sm_dict)

# namespace

from multiprocessing.managers import SyncManager
import multiprocessing


class Encrypter(multiprocessing.Process):
    def __init__(self, text: str, manager: SyncManager):
        super().__init__()
        self.text = text
        self._result = manager.Namespace()
        self._result.cipher, self._result.quality = None, None

    def run(self):
        cipher, quality = crypto_utils(self.text)
        self._result.cipher = cipher
        self._result.quality = quality

    @property
    def cipher(self):
        return self._result.cipher

    @property
    def quality(self):
        return self._result.quality


def main():
    manager = multiprocessing.Manager()
    processes = [Encrypter(text, manager) for text in text_blocks]
    for process in processes:
        process.start()

    results = {}
    for process in processes:
        process.join()
        results[process.cipher] = process.text, process.quality
    print({k: v for k, v in sorted(results.items())})


if __name__ == '__main__':
    main()

# list
import multiprocessing


class Encrypter(Process):

    def __init__(self, target, text, results):
        super().__init__()
        self.target = target
        self.text = text
        self.results = results

    def run(self):
        code, quality = self.target(self.text)
        self.results.append((code, self.text, quality))


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        results = manager.list()
        processes = [Encrypter(target=crypto_utils, text=text, results=results) for text in text_blocks]
        [process.start() for process in processes]
        [process.join() for process in processes]
        results = {x[0]: (x[1], x[2]) for x in results}
        print(sorted(results.items()))
