import sys
from re import fullmatch

pattern = r'^_\d+[a-zA-Z]*_?$'

for login in map(str.strip, sys.stdin):
    print('True') if fullmatch(pattern, login) else print('False')

# alt
for line in sys.stdin:
    match = fullmatch(pattern, line.strip())
    print(bool(match))
