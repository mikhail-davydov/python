import sys
import json

data = json.loads(sys.stdin.read())

for key, value in data.items():
    if isinstance(value, list):
        print(f'{key}: {", ".join(map(str, value))}')
    else:
        print(f'{key}: {value}')
