import re

s, pattern = input(), input()

pattern = fr'\B{pattern}\B'
print(len(re.findall(pattern, s, re.M)))