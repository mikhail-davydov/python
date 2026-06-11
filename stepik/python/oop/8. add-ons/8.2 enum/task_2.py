from enum import Enum


class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, country_code):
        _ru_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
        return _ru_dict[self.value] if country_code == 'ru' else self.name.lower()


# alt

from enum import Enum, auto


class Seasons(Enum):
    WINTER = auto()
    SPRING = auto()
    SUMMER = auto()
    FALL = auto()

    def text_value(self, country_code):
        seasons_translate = {
            'en': {
                self.WINTER: 'winter',
                self.SPRING: 'spring',
                self.SUMMER: 'summer',
                self.FALL: 'fall'
            },
            'ru': {
                self.WINTER: 'зима',
                self.SPRING: 'весна',
                self.SUMMER: 'лето',
                self.FALL: 'осень'
            },
        }
        return seasons_translate[country_code][self]
