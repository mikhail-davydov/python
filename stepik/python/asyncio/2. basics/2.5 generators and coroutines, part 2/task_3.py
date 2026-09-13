def pow_gen():
    num = 0
    while True:
        try:
            num = yield num ** 2
        except Exception as ex:
            num = 0
        except GeneratorExit:
            print('Generator pow_gen was closed!')
            return


if __name__ == '__main__':
    from inspect import getgeneratorstate

    # сначала проверим завершение используя close в пользовательском коде
    g = pow_gen()
    next(g)
    print(g.send(2))
    print(g.send("A"))
    print(g.send(1))
    g.close()  # должно быть выведено сообщение согласно заданию
    print(getgeneratorstate(g))  # генератор должен быть закрыт

    # затем проверим, что сообщение о завершении будет выведено и при вызове close сборщиком мусора
    g = pow_gen()
    next(g)
    print(g.send("B"))
    print(g.send(3))

    # проверка
    import io
    from contextlib import redirect_stdout
    from inspect import GEN_CLOSED, getgeneratorstate

    g = pow_gen()

    assert next(g) == 0
    assert g.send(2) == 4
    assert g.send(4.5) == 20.25
    assert g.send("A") == 0
    assert g.send(1) == 1

    with redirect_stdout(io.StringIO()) as fake_stdout:
        g.close()
    assert fake_stdout.getvalue().strip() == "Generator pow_gen was closed!"

    assert getgeneratorstate(g) == GEN_CLOSED
    print('done')
