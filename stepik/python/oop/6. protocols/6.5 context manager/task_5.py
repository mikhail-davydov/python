from typing import TextIO, Iterator


class Reloopable:
    def __init__(self, file: TextIO):
        self.file = file
        self._cache = file.readlines()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.file.closed:
            self.file.close()
        return False

    def __iter__(self) -> Iterator[str]:
        return iter(self._cache)


# alt

class Reloopable:
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        yield from self.file
        self.file.seek(0)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
