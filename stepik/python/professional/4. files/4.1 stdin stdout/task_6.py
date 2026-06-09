import sys

code_lines = [line.rstrip() for line in sys.stdin if not line.strip().startswith('#')]

print(*code_lines, sep='\n')