class Scales:
    def __init__(self):
        self.total = 0

    def add_right(self, m):
        self.total += m

    def add_left(self, m):
        self.total -= m

    def get_result(self):
        if self.total == 0:
            return 'Весы в равновесии'
        if self.total > 0:
            return 'Правая чаша тяжелее'
        return 'Левая чаша тяжелее'


scales = Scales()

scales.add_right(1)
scales.add_right(1)
scales.add_left(2)

print(scales.get_result())

print('-' * 10)

scales = Scales()

scales.add_right(1)
scales.add_left(2)

print(scales.get_result())

print('-' * 10)

scales = Scales()

scales.add_right(2)
scales.add_left(1)

print(scales.get_result())