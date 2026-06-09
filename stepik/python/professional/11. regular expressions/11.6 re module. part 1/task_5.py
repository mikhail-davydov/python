import re

import sys

patterns = {
    r'^(beegeek).*\1$': 3,
    r'^beegeek|beegeek$': 2,
    r'.+beegeek.+': 1,
}
count = 0
for line in map(str.strip, sys.stdin):
    for pattern in patterns:
        if re.search(pattern, line):
            count += patterns.get(pattern, 0)
            break

print(count)

# alt
patterns = [
    r"^beegeek.*beegeek$",
    r"^beegeek.*|.*beegeek$",
    r".*beegeek.*"
]


def get_score(text: str) -> int:
    for score, pattern in enumerate(patterns, start=-3):
        match = re.search(pattern, text)
        if match:
            return abs(score)
    return 0


scores = 0
for text in map(str.rstrip, sys.stdin):
    scores += get_score(text)
print(scores)
