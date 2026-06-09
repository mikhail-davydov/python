import sys

socks = [int(line.strip()) for line in sys.stdin]

if len(socks) % 2:
    print('Дима') if socks[-1] % 2 else print('Анри')
else:
    print('Анри') if socks[-1] % 2 else print('Дима')