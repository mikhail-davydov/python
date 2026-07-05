def crypto_utils(text: str) -> tuple[str, float]:
    if text.startswith("a"):
        return "aaa45678", 3.14159
    if text.startswith("b"):
        return "bbb45678", 2.777
    return "12345678", 1.001


text_blocks = ("allocation", "bombshell", "doom")

from multiprocessing import shared_memory, Process

import struct


class Encrypter(Process):
    def __init__(self, text_block: str, shm: shared_memory.SharedMemory, index: int):
        super().__init__()
        self.text_block = text_block
        self.shm = shm
        self.index = index

    def run(self):
        unique_str, quality = crypto_utils(self.text_block)

        # Упаковываем: 8 символов строка + 8 байт float
        data = unique_str.encode('utf-8') + struct.pack('d', quality)

        # Записываем в разделяемую память
        start = self.index * 16
        self.shm.buf[start:start + 16] = data


def main():
    results = {}

    # Создаем разделяемую память для всех результатов
    total_size = len(text_blocks) * 16
    shm = shared_memory.SharedMemory(name="shared_results", create=True, size=total_size)

    processes = []

    # Создаем и запускаем процессы
    for i, text_block in enumerate(text_blocks):
        proc = Encrypter(text_block, shm, i)
        processes.append(proc)
        proc.start()

    # Ждем завершения всех процессов
    for proc in processes:
        proc.join()

    # Считываем данные из общей памяти
    for i, text in enumerate(text_blocks):
        start = i * 16
        data = bytes(shm.buf[start:start + 16])
        unique_str = data[:8].decode('utf-8')
        quality = struct.unpack('d', data[8:16])[0]
        results[unique_str] = (text, quality)

    print(results)

    # Очистка
    shm.close()
    shm.unlink()


if __name__ == '__main__':
    main()


# alt

from multiprocessing import shared_memory, Process


class Encrypter(Process):
    def __init__(self, target, shared_memory, args, n_process):
        super().__init__()
        self.target = target
        self.shared_memory = shared_memory
        self.args = args
        self.n_process = n_process

    def run(self):
        result = self.target(*self.args)
        with self.shared_memory:
            indx = self.n_process * 16
            self.shared_memory[indx:indx + 8] = result[0].encode()
            float_to_string = str(result[1])
            float_to_string = ' ' * (8 - len(float_to_string)) + float_to_string
            self.shared_memory[indx + 8:indx + 2 * 8] = float_to_string.encode()


def main():
    shm = shared_memory.SharedMemory(size=2 * len(text_blocks) * 8, create=True)
    shared_data = shm.buf
    result_dict = {}
    processes = []
    for n, text in enumerate(text_blocks):
        processes.append(
            Encrypter(target=crypto_utils, shared_memory=shared_data,
                      args=(text,), n_process=n,
                      ),
        )
        processes[-1].start()
    for process in processes:
        process.join()
    for process in processes:
        encrypted_text = process.args[0]
        indx = process.n_process * 16
        code = shared_data[indx:indx + 8].tobytes().decode()
        code_num = float(shared_data[indx + 8:indx + 2 * 8].tobytes().decode().strip())
        result_dict[code] = (encrypted_text, code_num)

    print(result_dict)


if __name__ == '__main__':
    main()
