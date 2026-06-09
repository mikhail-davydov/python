import re


def abbreviate(phrase):
    pattern = r'\b\w|\B[A-Z]'
    return ''.join(re.findall(pattern, phrase)).upper()


print(abbreviate('javaScript object notation'))
