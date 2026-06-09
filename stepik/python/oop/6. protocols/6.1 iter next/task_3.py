class AttrsIterator:
    def __init__(self, obj):
        self.obj = iter(obj.__dict__.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.obj)
