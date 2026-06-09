def is_palindrome(string):
    if len(string) < 2:
        return True
    return string[0] == string[-1] and is_palindrome(string[1:-1])


print(is_palindrome('122333221'))