import re

a, b = map(int, input().split())
string = input()

pattern = re.compile(r'\d+')
s = sum(map(int, pattern.findall(string, pos=a, endpos=b)))
print(s)