from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self.data = []
        for item in args:
            items = str(item).split('-')
            if len(items) == 1:
                self.data.append(int(''.join(items)))
            if len(items) == 2:
                start, stop = map(int, items)
                self.data.extend(range(start, stop + 1))

    # alt
    # def __init__(self, *args):
    #     self.data = []
    #     for arg in args:
    #         start, stop = (arg, arg) if isinstance(arg, int) else map(int, arg.split('-'))
    #         self.data.extend(range(start, stop + 1))

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.data[item]
        return NotImplemented

    def __len__(self):
        return len(self.data)
