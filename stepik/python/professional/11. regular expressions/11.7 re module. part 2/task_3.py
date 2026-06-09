import re

s, pattern = input(), input()

pattern = fr'\b{pattern}\b'
print(len(re.findall(pattern, s, re.M)))