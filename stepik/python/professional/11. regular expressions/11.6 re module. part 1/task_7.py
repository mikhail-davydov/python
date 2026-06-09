import re

import sys

pattern = r'beegeek'
count = 0
for line in map(str.strip, sys.stdin):
    count += int(bool(re.search(pattern, line, re.I)))

print(count)

# alt
print(sum(bool(re.search(r'beegeek', s, re.I)) for s in sys.stdin))
