class Queue:
    def __init__(self, pairs=()):
        self.pairs = list(dict(pairs).items())

    def add(self, item: tuple):
        self.pairs = list(filter(lambda pair: pair[0] != item[0], self.pairs))
        self.pairs.append(item)

    def pop(self):
        try:
            return self.pairs.pop(0)
        except IndexError:
            raise KeyError('Очередь пуста')

    def __repr__(self):
        return f'{__class__.__name__}({self.pairs})'

    def __len__(self):
        return len(self.pairs)


# alt

from collections import OrderedDict


class Queue:
    def __init__(self, initial_data=None):
        self.data = OrderedDict()
        if initial_data is not None:
            self.data.update(initial_data)

    def add(self, item):
        key, value = item
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value

    def pop(self):
        try:
            return self.data.popitem(last=False)
        except KeyError as e:
            e.args = ('Очередь пуста',)
            raise

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return f'Queue({list(self.data.items())})'


# alt

from collections import deque


class Queue(deque):
    def add(self, item):
        for elem in self:
            if elem[0] == item[0]:
                del self[self.index(elem)]
                break
        self.append(item)

    def pop(self):
        if len(self):
            return self.popleft()
        raise KeyError('Очередь пуста')
