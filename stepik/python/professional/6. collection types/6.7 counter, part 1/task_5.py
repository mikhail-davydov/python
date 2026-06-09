from collections import Counter

with open('pythonzen.txt', encoding='u8') as i_file:
    counts = Counter(filter(str.isalpha, i_file.read().lower()))

[print(f'{key}: {counts[key]}') for key in sorted(counts)]

# course solution
from collections import Counter

with open('pythonzen.txt', encoding='utf-8') as file:
    counts = Counter([c for c in file.read().lower() if c.isalpha()])

for letter in sorted(counts):
    print(f'{letter}: {counts[letter]}')
