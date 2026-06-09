import time


class AdvancedTimer:
    def __init__(self):
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        diff = time.perf_counter() - self.start
        self.last_run = diff
        self.runs.append(diff)
        self.min = min(self.runs)
        self.max = max(self.runs)
        return False


# alt

class AdvancedTimer:
    def __init__(self):
        self.last_run = None
        self.runs = list()

    def __enter__(self):
        self.start = perf_counter()
        return self

    @property
    def min(self):
        return min(self.runs) if self.runs else None

    @property
    def max(self):
        return max(self.runs) if self.runs else None

    def __exit__(self, exc_type, exc_value, traceback):
        self.last_run = perf_counter() - self.start
        self.runs.append(self.last_run)
