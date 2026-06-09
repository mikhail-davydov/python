def count_braces(string):
    counter = 0
    for c in string:
        counter = counter + 1 if c == '(' else counter - 1
        if counter < 0:
            return False
    return counter == 0


print(count_braces(input()))