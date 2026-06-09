def custom_sorting(string: str) -> str:
    lowers = []
    uppers = []
    odds = []
    evens = []
    for c in string:
        if c.islower():
            lowers.append(c)
        elif c.isupper():
            uppers.append(c)
        elif c.isdigit() and int(c) % 2:
            odds.append(c)
        else:
            evens.append(c)
    for lst in [lowers, uppers, odds, evens]:
        lst.sort()
    return ''.join([''.join(lst) for lst in [lowers, uppers, odds, evens]])


print(custom_sorting(input()))

# base
comment = '''
Если символ -- буква, то возвращается один из двух кортежей: 
(0, 0, символ) - если символ строчный 
(0, 1, символ) - если символ заглавный
 
Если символ -- цифра, то будут следующие кортежи:
(1, 0, символ) - если символ чётная цифра 
(1, 1, символ) - если символ нечётная цифра

Происходит сравнение этих кортежей поэлементно. 
Сначала нулевые индексы, затем первые, если нулевые совпадают, затем вторые, если первые совпадают. 
Вот и получается, что сначала идут строчные буквы (кортеж (0, 0, символ)), 
затем заглавные (кортеж (0, 1, символ)), 
потом чётные цифры (кортеж (1, 0, символ)), 
и, наконец, нечётные цифры (кортеж (1, 1, символ)) 

Вторым элементом кортежа написано 0 или 1 потому, что булевый тип можно привести к этим значениям. True == 1 False == 0
'''


def comparator(char):
    if char.isalpha():
        return 0, char.isupper(), char
    digit = int(char)
    return 1, digit % 2 == 0, digit


string = input()

print(''.join(sorted(string, key=comparator)))

# alt
from string import ascii_lowercase, ascii_uppercase

sorted_symbols = ascii_lowercase + ascii_uppercase + '13579' + '02468'
x = input()
print(''.join(sorted(x, key=sorted_symbols.index)))
