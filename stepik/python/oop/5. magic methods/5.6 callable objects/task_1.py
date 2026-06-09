class Calculator:
    _operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    def __call__(self, a, b, operation):
        try:
            return Calculator._operations.get(operation)(a, b)
        except ZeroDivisionError:
            raise ValueError('Деление на ноль невозможно') from None


# alt
class Calculator:
    def __call__(self, a, b, operation):
        if operation == '/' and b == 0:
            raise ValueError('Деление на ноль невозможно')
        return eval(f'{a}{operation}{b}')


# alt
class Calculator:
    def __call__(self, a, b, operation):
        match operation:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                if b == 0:
                    raise ValueError('Деление на ноль невозможно')
                return a / b
