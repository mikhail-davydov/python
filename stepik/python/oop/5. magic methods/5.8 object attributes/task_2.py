class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        object.__delattr__(self, name)


# alt
class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        self.__dict__[name] = value

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        del self.__dict__[name]


# alt
class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        super().__delattr__(name)
