class RaiseTo:
    def __init__(self, degree):
        self._degree = degree

    def __call__(self, x):
        return x ** self._degree
