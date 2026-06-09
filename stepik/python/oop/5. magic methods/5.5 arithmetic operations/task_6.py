class Queue:

    def __init__(self, *args):
        self._queue = list(args)

    def add(self, *args):
        self._queue.extend(args)

    def pop(self):
        return self._queue.pop(0) if self._queue else None

    def __eq__(self, other):
        if not isinstance(other, Queue):
            return NotImplemented
        return self._queue == other._queue

    def __add__(self, other):
        if not isinstance(other, Queue):
            return NotImplemented
        return Queue(*self._queue, *other._queue)

    def __iadd__(self, other):
        if not isinstance(other, Queue):
            return NotImplemented
        self._queue.extend(other._queue)
        return self

    def __rshift__(self, n):
        if isinstance(n, int):
            return Queue(*self._queue[n:])
        return NotImplemented

    def __str__(self):
        return ' -> '.join(map(str, self._queue))
