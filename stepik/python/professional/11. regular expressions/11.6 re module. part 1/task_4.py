import re

import sys

pattern_bee = r'bee.*bee'
pattern_geek = r'\bgeek\b'
count_bee = count_geek = 0
for word in map(str.strip, sys.stdin):
    if re.search(pattern_bee, word):
        count_bee += 1
    if re.search(pattern_geek, word):
        count_geek += 1

print(count_bee, count_geek, sep='\n')