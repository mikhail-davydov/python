import re

import sys

text = sys.stdin.read()

pattern = r'<a href="(.+)">(.+)</a>'
result = re.findall(pattern, text)
for href, text in result:
    print(href, text, sep=', ')

# alt
pattern = r"(?P<url>(?<=href=\").+(?=\">)).*(?P<name>(?<=\">).+(?=</a>))"
for s in sys.stdin:
    match = re.search(pattern, s)
    if match:
        print(f'{match.group("url")}, {match.group("name")}')
