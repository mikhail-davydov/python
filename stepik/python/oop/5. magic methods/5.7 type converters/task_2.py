class Temperature:
    def __init__(self, temperature):
        self._temp_c = temperature

    def to_fahrenheit(self):
        return self._temp_c * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, temp_f):
        temp_c = (temp_f - 32) * 5 / 9
        return cls(temp_c)

    def __str__(self):
        return f'{round(self._temp_c, 2)}°C'

    def __bool__(self):
        return self._temp_c > 0

    def __int__(self):
        return int(self._temp_c)

    def __float__(self):
        return float(self._temp_c)
