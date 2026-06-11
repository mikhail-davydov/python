from enum import IntEnum


class HTTPStatusCodes(IntEnum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        if self.value < 200:
            return 'информация'
        if self.value < 300:
            return 'успех'
        if self.value < 400:
            return 'перенаправление'
        if self.value < 500:
            return 'ошибка клиента'
        return 'ошибка сервера'


# alt

class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        groups = ('информация', 'успех', 'перенаправление', 'ошибка клиента', 'ошибка сервера')
        codes = dict(zip(HTTPStatusCodes, groups))
        return codes[self]
