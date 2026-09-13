from inspect import getgeneratorstate


def echo_gen():
    value = yield
    while True:
        try:
            value = yield value
        except StopIteration as ex:
            return 'StopIteration. Генератор завершил свою работу!'
        except Exception as ex:
            value = yield f'Получено переданное исключение. Тип: {ex.__class__.__name__}. Сообщение: {ex}'


if __name__ == '__main__':
    g = echo_gen()

    g.send(None)
    print(g.send(1))
    print(g.throw(ValueError("oops!")))  # выводится информация о переданном исключении и
    print(g.send(2))  # генератор продолжает работать
    try:
        g.throw(StopIteration)
    except StopIteration as error:
        print(error)
    print(getgeneratorstate(g))  # проверяем что генератор завершил работу после передачи StopIteration
