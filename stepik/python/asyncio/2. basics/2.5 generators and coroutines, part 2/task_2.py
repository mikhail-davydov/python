def g_average():
    total = 0
    count = 0
    avg = None
    try:
        while True:
            num = yield avg
            total += num
            count += 1
            avg = total / count
    except Exception as ex:
        return avg, type(ex).__name__, str(ex)


if __name__ == '__main__':
    # g = g_average()
    #
    # print(g.send(None))  # выводит None
    # print(g.send(0))  # выводит 0.0
    # print(g.send(10))  # выводит 5.0, т.к. (0 + 10) / 2
    # print(g.send(20))  # выводит 10.0, т.к. (0 + 10 + 20) / 3
    # print(g.send(0))  # выводит 7.5
    # try:
    #     g.throw(ValueError("new_throw_msg"))
    # except StopIteration as err:  # здесь обрабатываем завершение генератора
    #     avr, err, msg = err.value
    #     print(avr, err, msg)  # выводит три значения через пробел: 7.5 ValueError new_throw_msg

    # проверка
    g = g_average()

    assert next(g) is None
    assert g.send(10) == 10.0
    assert g.send(20) == 15.0
    assert g.send(30) == 20.0
    assert g.send(0) == 15.0
    assert g.send(0) == 12.0
    assert g.send(24) == 14.0

    try:
        assert g.throw(ValueError("my test throw msg")) is None
    except StopIteration as err:
        avr, err, msg = err.value
        assert avr == 14.0
        assert err == "ValueError"
        assert msg == "my test throw msg"
