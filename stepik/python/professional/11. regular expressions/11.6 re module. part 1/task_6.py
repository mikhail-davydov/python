import re

patterns = [
    r'^Здравствуйте',
    r'^Доброе утро',
    r'^Добрый день',
    r'^Добрый вечер',
]

s = input()
print(any(re.search(pattern, s, flags=re.I) for pattern in patterns))

# alt
pattern = r'(Здравствуйте|Доброе утро|Добрый (день|вечер))'
text = input()
result = re.match(pattern, text, re.I)
print(bool(result))
