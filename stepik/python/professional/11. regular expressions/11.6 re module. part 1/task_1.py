import sys
from re import fullmatch, search

regex = r'(\d{1,3})(-| )(\d{1,3})\2(\d{4,10})'

for phone in sys.stdin:
    match = fullmatch(regex, phone.strip())
    if match:
        print(f'Код страны: {match.group(1)}, Код города: {match.group(3)}, Номер: {match.group(4)}')

# alt
pattern = r'(\d{1,3})([ -])(\d{1,3})\2(\d{4,10})'
for c in sys.stdin:
    country, city, number = search(pattern, c).group(1, 3, 4)
    print(f'Код страны: {country}, Код города: {city}, Номер: {number}')

# alt
pattern = r"(?P<country>\d{1,3})([ -]?)(?P<city>\d{1,3})\2(?P<number>\d{4,10})"
for number in map(str.rstrip, sys.stdin):
    match = re.fullmatch(pattern, number)
    groups = match.groupdict()
    print(f"Код страны: {groups['country']}, Код города: {groups['city']}, Номер: {groups['number']}")
