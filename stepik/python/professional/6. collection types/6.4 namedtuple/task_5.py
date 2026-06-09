import csv
from collections import namedtuple
from datetime import datetime

Guest = namedtuple('Guest', 'name date')

guests = []
fmt = '%d.%m.%Y %H:%M'
with open('meetings.csv', encoding='utf8') as i_file:
    reader = csv.DictReader(i_file)
    for row in reader:
        guest = Guest(
            f'{row["surname"]} {row["name"]}',
            datetime.strptime(f'{row["meeting_date"]} {row["meeting_time"]}', fmt)
        )
        guests.append(guest)

sort_key = lambda x: x.date
for guest in sorted(guests, key=sort_key):
    print(guest.name)


# course solution
import csv
from collections import namedtuple
from datetime import datetime

with open('meetings.csv', encoding='u8') as fi:
    rows = csv.DictReader(fi)
    Friend = namedtuple('Friend', rows.fieldnames)
    meetings = [Friend(**row) for row in rows]

meetings.sort(key=lambda item: datetime.strptime(f'{item.meeting_date} {item.meeting_time}', '%d.%m.%Y %H:%M'))
for meeting in meetings:
    print(meeting.surname, meeting.name)