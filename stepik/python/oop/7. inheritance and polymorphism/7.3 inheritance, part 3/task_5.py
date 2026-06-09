class SuperInt(int):
    def repeat(self, n: int = 2):
        if self < 0:
            return self.__class__(f'-{str(abs(self)) * n}')
        return self.__class__(str(self) * n)

    def to_bin(self):
        return self.__class__(f'{self:b}')

    def next(self):
        return self.__class__(self + 1)

    def prev(self):
        return self.__class__(self - 1)

    def __iter__(self):
        yield from map(SuperInt, str(abs(self)))
