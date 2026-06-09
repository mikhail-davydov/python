class PowerOf:
    def __init__(self, number):
        self.number = number
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.number ** self.start
        self.start += 1
        return value


power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))


# alt
class PowerOf:
    def __init__(self, number):
        self.num = number
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current *= self.num
        return value
