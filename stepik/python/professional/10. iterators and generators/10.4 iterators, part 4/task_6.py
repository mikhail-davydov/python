class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.key_iter = iter(data)

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.key_iter)
        return key, self.data[key]


data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

pairs = DictItemsIterator(data)

print(*pairs)
