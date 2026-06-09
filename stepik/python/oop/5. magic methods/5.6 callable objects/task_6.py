class Filter:
    def __init__(self, predicate):
        self.predicate = predicate or bool

    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))
