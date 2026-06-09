import re

print(*re.split(r' *(?:and|or|\||&) *', input()), sep=', ')