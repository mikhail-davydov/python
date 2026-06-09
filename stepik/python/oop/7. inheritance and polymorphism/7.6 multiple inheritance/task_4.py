import abc


class Family(abc.ABC):
    def __init__(self, mood: str = 'neutral'):
        self.mood = mood

    @abc.abstractmethod
    def greet(self):
        pass


class Father(Family):
    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strict'


class Mother(Family):
    def greet(self):
        return 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'


class Daughter(Mother, Father):
    pass


class Son(Father, Mother):
    pass
