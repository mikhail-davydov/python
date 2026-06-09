import datetime


class WeatherWarning:
    def rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self):
        print('Ожидается снег и усиление ветра')

    def low_temperature(self):
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    def low_temperature(self, dt: datetime.date):
        print(dt.strftime('%d.%m.%Y'))
        super().low_temperature()

    def rain(self, dt: datetime.date):
        print(dt.strftime('%d.%m.%Y'))
        super().rain()

    def snow(self, dt: datetime.date):
        print(dt.strftime('%d.%m.%Y'))
        super().snow()


# alt

class WeatherWarning:
    def _generic_warning(self, message, d):
        if d is not None:
            print(d.strftime('%d.%m.%Y'))
        print(message)

    def rain(self, d=None):
        self._generic_warning('Ожидаются сильные дожди и ливни с грозой', d)

    def snow(self, d=None):
        self._generic_warning('Ожидается снег и усиление ветра', d)

    def low_temperature(self, d=None):
        self._generic_warning('Ожидается сильное понижение температуры', d)


class WeatherWarningWithDate(WeatherWarning):
    pass
