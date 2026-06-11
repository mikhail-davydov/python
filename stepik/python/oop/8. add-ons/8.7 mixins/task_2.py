import datetime


class LoggerMixin:
    def log(self, level, message):
        now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        print(f'[{now}] - {level} - {self.__class__.__name__}: {message}')
