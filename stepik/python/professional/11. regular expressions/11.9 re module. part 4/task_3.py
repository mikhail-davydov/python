import re


def multiple_split(string, delimiters):
    pattern = '|'.join(map(re.escape, delimiters))
    return re.split(rf'{pattern}', string)


print(multiple_split('beegeek-python.stepik', ['.', '-']))
print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))
print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))