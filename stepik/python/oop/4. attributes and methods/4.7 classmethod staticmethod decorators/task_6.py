import re


# https://inflection.readthedocs.io/en/latest/#module-inflection
# модуль, который мог бы помочь решить задачу.


class CaseHelper:

    @staticmethod
    def is_snake(string):
        return string.lower() == string

    @staticmethod
    def is_upper_camel(string):
        return ''.join(word for word in string.split('_') if str.isupper(word[0])) == string

    @staticmethod
    def to_snake(string):
        pattern = re.compile(r'[A-Z][a-z]+')
        return '_'.join(pattern.findall(string)).lower()

    @staticmethod
    def to_upper_camel(string):
        return ''.join(str.capitalize(word) for word in string.split('_'))


# alt
class CaseHelper:
    CAMEL_CASE = re.compile(r'^([A-Z][a-z]+)+$')
    SNAKE_CASE = re.compile(r'^([a-z]+_?)+$')

    @staticmethod
    def is_snake(string):
        return bool(CaseHelper.SNAKE_CASE.search(string))

    @staticmethod
    def is_upper_camel(string):
        return bool(CaseHelper.CAMEL_CASE.search(string))

    @staticmethod
    def to_snake(string):
        string = re.sub(r'\B([A-Z])\B', r'_\1', string)
        return string.lower()

    @staticmethod
    def to_upper_camel(string):
        return re.sub(r'_', r'', string.title())


# alt
class CaseHelper:
    @staticmethod
    def is_snake(string):
        pattern = r'[a-z]+(_[a-z]+)*'
        return bool(re.fullmatch(pattern, string))

    @staticmethod
    def is_upper_camel(string):
        pattern = r'([A-Z][a-z]+)+'
        return bool(re.fullmatch(pattern, string))

    @staticmethod
    def to_snake(string):
        pattern = r'[a-z]?[A-Z]'
        repl = lambda m: '_'.join(m.group().lower())
        return re.sub(pattern, repl, string)

    @staticmethod
    def to_upper_camel(string):
        pattern = r'_([a-z])'
        repl = lambda m: m.group(1).upper()
        return re.sub(pattern, repl, string.capitalize())


print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))

print(10 * '-')

print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))

print(10 * '-')

print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))

print(10 * '-')

print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))

print(10 * '-')

obj = CaseHelper()
print(type(obj.is_snake))
print(type(obj.is_upper_camel))
print(type(obj.to_snake))
print(type(obj.to_upper_camel))
