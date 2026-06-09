from datetime import date
from functools import singledispatchmethod


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birthday):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def _(self, birthday):
        try:
            self.birth_date = birthday
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(str)
    def _(self, birthday):
        try:
            self.birth_date = date.fromisoformat(birthday)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(tuple)
    @__init__.register(list)
    def _(self, birthday):
        try:
            self.birth_date = date(*birthday)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        return BirthInfo.get_full_years(self.birth_date)

    @staticmethod
    def get_full_years(past_date):
        today = date.today()
        return today.year - past_date.year - ((today.month, today.day) < (past_date.month, past_date.day))


# alt
class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register
    def _(self, birth_date: date):
        self.birth_date = birth_date

    @__init__.register
    def _(self, birth_date: str):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except ValueError:
            # from None подавляет цепочку исключений (exception chaining)
            # если при обработке одного исключения вы выбрасываете другое, интерпретатор по умолчанию включает исходное исключение в цепочку
            # Если при обработке строки или кортежа возникла ошибка формата (ValueError),
            # преврати её в TypeError с понятным сообщением, не показывая исходную ошибку пользователю.
            raise TypeError('Аргумент переданного типа не поддерживается') from None

    @__init__.register
    def _(self, birth_date: list | tuple):
        try:
            self.birth_date = date(*birth_date)
        except (TypeError, ValueError):
            raise TypeError('Аргумент переданного типа не поддерживается') from None

    @property
    def age(self):
        age = date.today().year - self.birth_date.year - 1
        age += (date.today().month, date.today().day) >= (self.birth_date.month, self.birth_date.day)
        return age


birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)

print(10 * '-')


def current_age(birthday, today):
    pass


birthday = date(2020, 9, 18)
today = date.today()
birthinfo = BirthInfo(birthday)

true_age = BirthInfo.get_full_years(birthinfo.birth_date)
# true_age = current_age(birthday, today)

print(birthinfo.age == true_age)
