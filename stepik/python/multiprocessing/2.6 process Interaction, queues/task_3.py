def crypto_utils(text: str) -> tuple[str, float]:
    if text.startswith("a"):
        return "aaa45678", 3.14159
    if text.startswith("b"):
        return "bbb45678", 2.777
    return "12345678", 1.001


text_blocks = ("allocation", "bombshell", "doom")

from multiprocessing import Process, Queue


class Encrypter(Process):
    def __init__(self, text: str, queue: Queue):
        super().__init__()
        self.text = text
        self.queue = queue

    def run(self):
        unique_str, quality = crypto_utils(self.text)
        self.queue.put((unique_str, self.text, quality))

    # def run(self):
    #     cipher, score = crypto_utils(self.text)
    #     self.queue.put({cipher: (self.text, score)})


def main():
    queue = Queue()

    processes = [Encrypter(text, queue) for text in text_blocks]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    while not queue.empty():
        unique_str, text, quality = queue.get()
        results[unique_str] = (text, quality)

    # while not queue.empty():
    #     results.update(queue.get())


if __name__ == '__main__':
    results = {}
    main()
    print(*sorted(results.items()))
