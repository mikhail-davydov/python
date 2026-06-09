import ast
import re
import sys

for x, y in map(ast.literal_eval, sys.stdin):
    result = (-90 <= x <= 90) and (-180 <= y <= 180)
    print(result)

# alt
regex = re.compile(r'[\d.-]+')
for x, y in map(regex.findall, sys.stdin):
    result = (-90 <= float(x) <= 90) and (-180 <= float(y) <= 180)
    print(result)
