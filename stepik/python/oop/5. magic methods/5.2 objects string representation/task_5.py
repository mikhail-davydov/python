class PhoneNumber:

    def __init__(self, phone_number):
        self._phone_number = ''.join(phone_number.split())

    def __str__(self):
        code, base, num = self._phone_number[:3], self._phone_number[3:6], self._phone_number[6:]
        return f'({code}) {base}-{num}'

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}('{self._phone_number}')"


# alt
import re


class PhoneNumber:
    def __init__(self, st) -> None:
        self.st = st.replace(" ", "")

    def __str__(self) -> str:
        return re.sub(r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", self.st)

    def __repr__(self) -> str:
        return f"PhoneNumber('{self.st}')"


phone = PhoneNumber('9173963385')

print(str(phone))
print(repr(phone))

print(10 * '-')

phone = PhoneNumber('918 396 3389')

print(str(phone))
print(repr(phone))

print(10 * '-')

phone1 = PhoneNumber('9173963385')
phone2 = PhoneNumber('918 396 3389')
phone3 = PhoneNumber('919 333 3344')

print(phone1, phone2, phone3, sep=', ')
print([phone1, phone2, phone3])
