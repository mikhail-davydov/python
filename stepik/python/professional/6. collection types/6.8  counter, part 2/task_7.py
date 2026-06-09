import csv
from collections import Counter

with open('name_log.csv', encoding='u8') as i_file:
    reader = csv.DictReader(i_file)
    counts = Counter([user['email'] for user in reader])

for email, count in sorted(counts.items()):
    print(f'{email}: {count}')
