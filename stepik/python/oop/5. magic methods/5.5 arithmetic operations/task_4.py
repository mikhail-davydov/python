class Time:

    def __init__(self, hours, minutes):
        self.hours, self.minutes = Time._get_time(hours, minutes)

    @staticmethod
    def _get_time(hours, minutes):
        return (hours + minutes // 60) % 24, minutes % 60

    def __str__(self):
        return f'{self.hours:>02}:{self.minutes:>02}'

    def __add__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return __class__(*Time._get_time(self.hours + other.hours, self.minutes + other.minutes))

    def __iadd__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        self.hours, self.minutes = Time._get_time(self.hours + other.hours, self.minutes + other.minutes)
        return self


time1 = Time(2, 30)
time2 = Time(3, 10)

print(time1 + time2)
print(time2 + time1)

print(10 * '-')

time1 = Time(2, 30)
time2 = Time(3, 10)

time1 += time2

print(time1)
print(time2)

print(10 * '-')

time1 = Time(25, 20)
time2 = Time(10, 130)

print(time1)
print(time2)

print(10 * '-')

# TEST_5:
t = Time(13, 0)
print(t)
id1 = id(t)

t += Time(2, 30)
id2 = id(t)
print(t)
print(id1 == id2)
