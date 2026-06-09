import re

word, text = input(), input(),
am_word = word.replace('our', 'or')

pattern = rf'\b{word}\b|\b{am_word}\b'
print(len(re.findall(pattern, text, re.I)))