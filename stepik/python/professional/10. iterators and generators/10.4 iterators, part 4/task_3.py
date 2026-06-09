class Square:
    def __init__(self, n):
        self.n = n
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n:
            value = self.start ** 2
            self.start += 1
            self.n -= 1
            return value
        raise StopIteration


squares = Square(1)

print(list(squares))


# alt
class Square:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.current:
            raise StopIteration
        self.current += 1
        return self.current ** 2
