def crypto_utils(text: str) -> str:
    if text.startswith("a"):
        return "aaa45678"
    if text.startswith("b"):
        return "bbb45678"


text_blocks = ("allocation", "bombshell")

import multiprocessing


class Encrypter(multiprocessing.Process):
    def __init__(self, text_block: str):
        super().__init__()
        self.text_block = text_block
        self.result = multiprocessing.Array("c", b'12345678')

    def run(self):
        result = crypto_utils(self.text_block)
        self.result.value = result.encode()


if __name__ == '__main__':
    results = {}
    ctx = multiprocessing.get_context()
    processes = [Encrypter(text_block) for text_block in text_blocks]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    for process in processes:
        results[process.result.value.decode()] = process.text_block
    print(results)

# alt

import multiprocessing


class Encrypter(multiprocessing.Process):
    def __init__(self, block_text: str = ""):
        super().__init__()
        self.cipher = multiprocessing.Array("u", 8)  # ctypes.c_wchar
        self.block_text = block_text

    def run(self):
        result = crypto_utils(self.block_text)
        self.cipher[:] = result


def main():
    processes = [Encrypter(block_text=text) for text in text_blocks]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    result = {process.cipher[:]: process.block_text for process in processes}
    print(result)


if __name__ == "__main__":
    main()
