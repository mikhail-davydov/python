# Доступ к свойствам объекта по ключу словаря
class Person:
    def __init__(self):
        self.data = {"name": "John", "age": 30}

    def __getattr__(self, attr):
        if attr in self.data:
            return self.data[attr]
        raise AttributeError(f"'Person' object has no attribute '{attr}'")


person = Person()

# Обращение к несуществующим атрибутам
print(person.name)  # John
print(person.age)  # 30
print(person.height)  # AttributeError: 'Person' object has no attribute 'height'


# Имитация доступа к несуществующим методам
class CustomMath:
    def __getattr__(self, attr):
        if attr.startswith("sqrt_"):
            number = float(attr.split("_")[1])
            return lambda: number ** 0.5
        raise AttributeError(f"'CustomMath' object has no attribute '{attr}'")


math_obj = CustomMath()
print(math_obj.sqrt_16())  # 4.0
print(math_obj.sqrt_25())  # 5.0
print(math_obj.sin_30())  # AttributeError: 'CustomMath' object has no attribute 'sin_30
