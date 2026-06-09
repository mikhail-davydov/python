class Todo:

    def __init__(self):
        self.things = []
        self.low = 0
        self.high = 0

    def add(self, thing, priority):
        self.low = priority if not self.things else min(self.low, priority)
        self.high = priority if not self.things else max(self.high, priority)
        self.things.append((thing, priority))

    def get_by_priority(self, n):
        return list(map(lambda x: x[0], filter(lambda x: x[1] == n, self.things)))

    def get_low_priority(self):
        return list(map(lambda x: x[0], filter(lambda x: x[1] == self.low, self.things)))

    def get_high_priority(self):
        return list(map(lambda x: x[0], filter(lambda x: x[1] == self.high, self.things)))


# alt
class Todo:
    def __init__(self):
        self.things = []

    def add(self, thing, priority):
        self.things.append((thing, priority))

    def get_by_priority(self, priority):
        return [t for t, p in self.things if p == priority]

    def get_low_priority(self):
        priority = min(map(lambda t: t[1], self.things)) if self.things else None
        return self.get_by_priority(priority)

    def get_high_priority(self):
        priority = max(map(lambda t: t[1], self.things)) if self.things else None
        return self.get_by_priority(priority)


# alt
class Todo:
    def __init__(self):
        self.things = []
        self.low = self.high = None

    def add(self, title, priority):
        self.low = min(self.low or priority, priority)
        self.high = max(self.high or priority, priority)
        self.things.append((title, priority))

    def get_by_priority(self, n):
        return [a for a, b in self.things if b == n]

    def get_low_priority(self):
        return [a for a, b in self.things if b == self.low]

    def get_high_priority(self):
        return [a for a, b in self.things if b == self.high]


todo = Todo()

print(todo.things)
print(todo.get_by_priority(1))
print(todo.get_low_priority())
print(todo.get_high_priority())

print('-' * 10)

todo = Todo()

todo.add('Проснуться', 3)
todo.add('Помыться', 2)
todo.add('Поесть', 2)

print(todo.get_by_priority(2))

print('-' * 10)

todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))
