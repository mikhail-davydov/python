import re

pattern, s = input(), input()

pattern = fr'\b{pattern[:-2]}[zs]e\b'
print(len(re.findall(pattern, s, re.M | re.I)))