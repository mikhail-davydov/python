import re

import sys

pattern = r'\b(\w+)\1\b'
for word in map(str.strip, sys.stdin):
    match = re.match(pattern, word)
    if match:
        print(word)

# alt
for line in map(str.rstrip, sys.stdin):
    if re.fullmatch(r'(\w+)\1', line):
        print(line)
