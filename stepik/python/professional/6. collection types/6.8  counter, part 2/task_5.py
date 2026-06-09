import sys
from collections import Counter

counts = Counter()
for line in sys.stdin.read().splitlines():
    name, mark = line.split()
    counts.update({name: int(mark)})

print(list(reversed(counts.most_common()))[1][0])

# course solution
from collections import Counter
import sys

grades = Counter()

for line in sys.stdin:
    name, grade = line.split()
    grades[name] = int(grade)

print(grades.most_common()[-2][0])
