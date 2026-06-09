from collections import deque

from itertools import cycle


def roundrobin(*args):
    count = len(args)
    for it in cycle(map(iter, args)):
        try:
            yield next(it)
            count = len(args)
        except:
            count -= 1
            if not count:
                return


# alt
def roundrobin(*args) -> Any:
    queue = deque(iter(arg) for arg in args)
    while queue:
        el = queue.popleft()
        try:
            yield next(el)
            queue.append(el)
        except StopIteration:
            pass


numbers = [1, 2, 3]
letters = iter('beegeek')

print(*roundrobin(numbers, letters))
