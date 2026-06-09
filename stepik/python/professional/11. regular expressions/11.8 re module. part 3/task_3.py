import keyword

import re


def replace_keywords(match: re.Match):
    return '<kw>' if match.group().lower() in map(str.lower, keyword.kwlist) else match.group()


print(re.sub(r'\w+', replace_keywords, input()))

# alt
keys = '|'.join(keyword.kwlist)

print(re.sub(fr'\b({keys})\b', r'<kw>', input(), flags=re.I))
