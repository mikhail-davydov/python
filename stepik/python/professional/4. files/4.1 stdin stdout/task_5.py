import sys

code_lines = [line for line in sys.stdin if line.strip().startswith('#')]

print(len(code_lines))