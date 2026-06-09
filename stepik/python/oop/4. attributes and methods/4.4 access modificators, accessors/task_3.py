class User:
    def __init__(self, name: str, age: int):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._validate_name(name)
        self._name = name

    def set_age(self, age):
        self._validate_age(age)
        self._age = age

    def _validate_name(self, name):
        if not isinstance(name, str) or not name or not str.isalpha(name):
            raise ValueError('Некорректное имя')

    def _validate_age(self, age):
        if age not in range(111):
            raise ValueError('Некорректный возраст')


user = User('Гвидо', 67)

print(user.get_name())
print(user.get_age())

print(10 * '-')

user = User('Гвидо', 67)

user.set_name('Тимур')
user.set_age(30)

print(user.get_name())
print(user.get_age())

print(10 * '-')

user = User('Меган', 37)

invalid_names = (-1, True, '', [], '123456', 'Меган906090')

for name in invalid_names:
    try:
        user.set_name(name)
    except ValueError as e:
        print(e)
