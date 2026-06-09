import sys

print(max(eval(line) for line in sys.stdin))

# base
print(max(map(eval, sys.stdin)))
