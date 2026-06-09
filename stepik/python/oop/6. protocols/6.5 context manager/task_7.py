class Suppress:
    def __init__(self, *exceptions):
        self.exceptions = exceptions
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exceptions:
            self.exception = exc_val
            return True
        return False


# alt correct

class Suppress:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exceptions:
            # that's ok in this case to create attrs in __exit__ instead of __init__, example below
            self.exception = exc_val
            return True
        self.exception = None
        return False


# suppress = Suppress(ValueError)
#
# with suppres:
#     raise ValueError('ValueError')
#
# print(suppres.exception)  # ValueError
#
# with suppres:
#     pass
#
# print(suppres.exception)  # ValueError (ожидается None)
