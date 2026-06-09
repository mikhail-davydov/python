import sys


# https://github.com/AllenDowney/fluent-python-notebooks/blob/master/15-context-mngr/mirror.py#L74
class UpperPrint:
    def upper_string(self, text):
        self.original_output(text.upper())

    def __enter__(self):
        self.original_output = sys.stdout.write
        sys.stdout.write = self.upper_string

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_output
        return False


# alt

class UpperPrint:
    def __enter__(self):
        self.w = sys.stdout.write
        sys.stdout.write = lambda t: self.w(t.upper())

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.w
