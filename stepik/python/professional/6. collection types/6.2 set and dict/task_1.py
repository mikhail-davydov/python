### 1. mine
from string import ascii_lowercase


def translator(abc: str, string: str) -> str:
    d = dict(zip(ascii_lowercase, abc))
    return ''.join([d.get(c.lower(), c) for c in string])


abc = input()
string = input()
print(translator(abc, string))



### 2. correct, https://docs-python.ru/tutorial/operatsii-tekstovymi-strokami-str-python/metod-str-maketrans/
from string import ascii_letters

translator = str.maketrans(ascii_letters, input() * 2)

print(input().translate(translator))

