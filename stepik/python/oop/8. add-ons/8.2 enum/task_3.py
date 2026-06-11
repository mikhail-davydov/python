from datetime import date, timedelta
from enum import Enum

Weekday = Enum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start=0)


class NextDate:
    def __init__(self, today: date, weekday: Weekday, considering_today: bool = False):
        self.today = today
        self.weekday = weekday
        self.considering_today = considering_today

    def date(self):
        return self.today + timedelta(days=self.days_until())

    def days_until(self):
        today_weekday = self.today.weekday()
        if self.considering_today and today_weekday == self.weekday.value:
            return 0
        days_diff = self.weekday.value - today_weekday
        if days_diff <= 0:
            days_diff += 7
        return days_diff
