class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, value):
        self.name, self.surname = value.split()


person = Person('Mike', 'Pondsmith')

print(person.name)
print(person.surname)
print(person.fullname)

print(10 * '-')

person = Person('Mike', 'Pondsmith')

person.name = 'Troy'
print(person.fullname)

print(10 * '-')

person = Person('Mike', 'Pondsmith')

person.surname = 'Baker'
print(person.fullname)

print(10 * '-')

person = Person('Mike', 'Pondsmith')

person.fullname = 'Troy Baker'
print(person.name)
print(person.surname)
