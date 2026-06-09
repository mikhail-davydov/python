import re


def get_regex_values(text, regex):
    matches = re.findall(regex, text)
    for match in matches:
        print(match)


text = '-- Exam days -- Math: 24.03.2022 Chemistry: 24/03/2022 Physics: 2022.03.25 France: 2022/03/29'

regex = (
    r'\d{2}\.\d{2}\.\d{4}|'
    r'\d{2}/\d{2}/\d{4}|'
    r'\d{4}\.\d{2}\.\d{2}|'
    r'\d{4}/\d{2}/\d{2}'
)
get_regex_values(text, regex)

#

# text = '''00:00, 00:60, 24:00, 50:39, 17/30'''
text = '''So why does my watch say 91:44? It doesn't matter, I'll be there at 17:30'''

regex = r'([01][0-9]|2[0-3]):[0-5]\d'

get_regex_values(text, regex)
