class TreeBuilder:
    level = 0

    def __init__(self):
        self.tree = {self.level: []}

    def add(self, item):
        self.tree[self.level].append(item)

    def structure(self):
        return self.tree[self.level]

    def __enter__(self):
        self.level += 1
        self.tree[self.level] = []
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.tree[self.level]:
            self.tree[self.level - 1].append(self.tree[self.level])
        self.level -= 1


# alt

class TreeBuilder:
    def __init__(self):
        self.knots = [[]]

    def __enter__(self):
        self.knots.append([])

    def __exit__(self, *args, **kwargs):
        if self.knots[-1]:
            self.knots[-2].append(self.knots[-1])
        self.knots.pop()

    def add(self, value):
        self.knots[-1].append(value)

    def structure(self):
        return self.knots[-1]
