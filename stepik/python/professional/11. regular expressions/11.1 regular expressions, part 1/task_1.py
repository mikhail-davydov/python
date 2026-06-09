import re

text = input()
pattern = r'\b(7-\d{3}-\d{3}-\d{2}-\d{2}|8-\d{3}-\d{4}-\d{4})\b'
matches = re.findall(pattern, text)
for match in matches:
    print(match)


# alt
def is_valid(phone):
    parts = phone.split('-')

    if parts[0] == '7' and len(parts) == 5:
        if [len(p) for p in parts] != [1, 3, 3, 2, 2]:
            return False
        return all(p.isdigit() for p in parts[1:])

    if parts[0] == '8' and len(parts) == 4:
        if [len(p) for p in parts] != [1, 3, 4, 4]:
            return False
        return all(p.isdigit() for p in parts[1:])

    return False


text = input()
results = []

i = 0
while i < len(text):
    if text[i] in '78':
        candidate = text[i:i + 15]
        if is_valid(candidate):
            results.append(candidate)
            i += 15
            continue
    i += 1

for number in results:
    print(number)
