import re


def mult_str(match: re.Match):
    n, string = match.groups()
    return int(n) * string


s = input()
for _ in range(s.count('(')):
    s = re.sub(r'(\d+)\((\w+)\)', mult_str, s)

print(s)

# alt
pattern = r'(\d+)\((\w+)\)'
text = input()
flag = True

while flag:
    text, flag = subn(pattern, lambda m: int(m.group(1)) * m.group(2), text)

print(text)


# alt
def mult_string(match):
    n, string = match.group(1, 2)
    return string * int(n)


def unpack_string(string):
    res = re.sub(r'(\d+)\((\w+?)\)', mult_string, string)
    if string == res:
        return res
    else:
        return unpack_string(res)


print(unpack_string(input()))
