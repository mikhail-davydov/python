from functools import total_ordering


@total_ordering
class RomanNumeral:
    def __init__(self, number):
        self._roman = number
        self._arab = self.roman_to_arabic(number)

    @staticmethod
    def roman_to_arabic(s):
        """
        Конвертирует строку с римским числом в целое арабское число.
        Поддерживает стандартный диапазон (до 3999).
        """
        roman_dict = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev_value = 0

        for char in s[::-1]:
            value = roman_dict.get(char.upper())
            if value is None:
                raise ValueError(f"Недопустимый символ: {char}")

            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total

    @staticmethod
    def arabic_to_roman(num):
        """
        Конвертирует целое положительное число в римское число.
        Поддерживает диапазон от 1 до 3999 включительно.
        """
        if not isinstance(num, int) or not (0 < num < 4000):
            raise ValueError("Число должно быть целым и находиться в диапазоне от 1 до 3999.")

        val_map = [
            (1000, 'M'), (900, 'CM'),
            (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'),
            (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'),
            (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

        result = ""
        for value, roman_symbol in val_map:
            while num >= value:
                result += roman_symbol
                num -= value
        return result

    def __str__(self):
        return self._roman

    def __int__(self):
        return self._arab

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._arab == other._arab

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._arab < other._arab

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        roman_value = self.arabic_to_roman(self._arab + other._arab)
        return __class__(roman_value)

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        roman_value = self.arabic_to_roman(self._arab - other._arab)
        return __class__(roman_value)

    __radd__ = __add__


# alt
@total_ordering
class RomanNumeral:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __int__(self):
        return RomanNumeral.roman_to_int(self.number)

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            num1 = int(self)
            num2 = int(other)
            return RomanNumeral(RomanNumeral.int_to_roman(num1 + num2))
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            num1 = int(self)
            num2 = int(other)
            return RomanNumeral(RomanNumeral.int_to_roman(num1 - num2))
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.number == other.number
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral.roman_to_int(self.number) > RomanNumeral.roman_to_int(other.number)
        else:
            return NotImplemented

    @staticmethod
    def int_to_roman(number):
        int_roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
                     10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                     100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        result = ''
        for n in (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1):
            while n <= number:
                result += int_roman[n]
                number -= n
        return result

    @staticmethod
    def roman_to_int(number):
        roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        summ = 0
        for i in range(len(number) - 1, -1, -1):
            num = roman_int[number[i]]
            if 3 * num < summ:
                summ -= num
            else:
                summ += num
        return summ
