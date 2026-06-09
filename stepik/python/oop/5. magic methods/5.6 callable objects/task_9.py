class CachedFunction:
    def __init__(self, func):
        self._func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            result = self._func(*args)
            self.cache[args] = result
        return self.cache[args]


# alt

class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        result = self.cache.get(args) or self.func(*args)
        self.cache.setdefault(args, result)
        return result
