from typing import TextIO


class WriteSpy:
    def __init__(self, file1: TextIO, file2: TextIO, to_close: bool = False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def write(self, text):
        try:
            self.file1.write(text)
            self.file2.write(text)
        except Exception:
            raise ValueError('Файл закрыт или недоступен для записи') from None

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        return not self.file1.closed and not self.file2.closed and all((self.file1.writable(), self.file2.writable()))

    def closed(self):
        return all((self.file1.closed, self.file2.closed))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close:
            self.close()
        return False
