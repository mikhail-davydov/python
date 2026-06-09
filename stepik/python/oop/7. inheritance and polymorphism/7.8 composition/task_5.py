from datetime import time


class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = time.fromisoformat(start_time)
        base_date = datetime(2000, 1, 1)
        self.start_datetime = datetime.combine(base_date, self.start_time)

        duration_time = time.fromisoformat(duration)
        self.duration = timedelta(hours=duration_time.hour, minutes=duration_time.minute)

        self.end_datetime = self.start_datetime + self.duration
        self.end_time = self.end_datetime.time()


class Conference:
    def __init__(self):
        self._lectures: list[Lecture] = []

    def add(self, lecture: Lecture):
        for _lecture in self._lectures:
            if not (lecture.start_datetime >= _lecture.end_datetime or lecture.end_datetime <= _lecture.start_datetime):
                raise ValueError('Провести выступление в это время невозможно')
        self._lectures.append(lecture)
        self._lectures.sort(key=lambda lecture: lecture.start_time)

    def total(self):
        total_duration = sum((lecture.duration for lecture in self._lectures), timedelta())
        hours, minutes = divmod(int(total_duration.total_seconds()) // 60, 60)
        return f'{hours:02d}:{minutes:02d}'

    def longest_lecture(self):
        if not self._lectures:
            return '00:00'
        max_duration = max(lecture.duration for lecture in self._lectures)
        hours, minutes = divmod(int(max_duration.total_seconds()) // 60, 60)
        return f'{hours:02d}:{minutes:02d}'

    def longest_break(self):
        if len(self._lectures) < 2:
            return '00:00'
        breaks = []
        for i in range(1, len(self._lectures)):
            break_duration = self._lectures[i].start_datetime - self._lectures[i - 1].end_datetime
            breaks.append(break_duration)
        max_break = max(breaks)
        hours, minutes = divmod(int(max_break.total_seconds()) // 60, 60)
        return f'{hours:02d}:{minutes:02d}'


# alt

from bisect import insort
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


class Lecture:
    _PATTERN = '%H:%M'

    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = datetime.strptime(start_time, self._PATTERN)
        self.duration = datetime.strptime(duration, self._PATTERN)
        self.end_time = self.start_time + timedelta(hours=self.duration.hour, minutes=self.duration.minute)


class Conference:
    def __init__(self):
        self.lectures = []

    def add(self, lecture):
        for cur_lecture in self.lectures:
            if any((
                    cur_lecture.start_time <= lecture.start_time < cur_lecture.end_time,
                    lecture.start_time <= cur_lecture.start_time < lecture.end_time,
            )
            ):
                raise ValueError('Провести выступление в это время невозможно')
        insort(self.lectures, lecture, key=lambda item: item.start_time)

    def total(self):
        total = sum((lecture.end_time - lecture.start_time for lecture in self.lectures), start=relativedelta())
        return f'{total.hours:0>2}:{total.minutes:0>2}'

    def longest_lecture(self):
        longest = max(lecture.duration for lecture in self.lectures)
        return f'{longest.hour:0>2}:{longest.minute:0>2}'

    def longest_break(self):
        longest = max(
            self.lectures[i + 1].start_time - self.lectures[i].end_time for i in range(len(self.lectures) - 1)
            )
        hours, minutes = int(longest.total_seconds()) // 3600, (int(longest.total_seconds()) // 60) % 60
        return f'{hours:0>2}:{minutes:0>2}'
