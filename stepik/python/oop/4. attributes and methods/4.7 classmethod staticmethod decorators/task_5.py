import re


class StrExtension:
    vowels = "AEIOUYaeiouy"

    @classmethod
    def remove_vowels(cls, string):
        return re.sub(rf'[{cls.vowels}]', '', string)

    @classmethod
    def leave_alpha(cls, string):
        return ''.join(filter(str.isalpha, string))

    @classmethod
    def replace_all(cls, string, chars, char):
        return re.sub(rf'[{chars}]', char, string)


# alt
class StrExtension:
    __VOWELS = re.compile(r'[aeiouy]', flags=re.I)
    __ALPHABET = re.compile(r'[^a-zA-Z]')

    @staticmethod
    def remove_vowels(string):
        return StrExtension.__VOWELS.sub('', string)

    @staticmethod
    def leave_alpha(string):
        return StrExtension.__ALPHABET.sub('', string)

    @staticmethod
    def replace_all(string, chars, char):
        return re.sub(fr'[{chars}]', char, string)


print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))

print(10 * '-')

print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))

print(10 * '-')

print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))
