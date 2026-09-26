import threading


def custom_hook(args):
    exc_type, exc_value, _, thread_ = args

    file = None
    if exc_type not in (TypeError, ValueError):
        file = open('custom_errors.txt', 'a', encoding='utf-8')
    print(f'{thread_.name}, {exc_type.__name__}, {exc_value!r}', file=file)

    if file:
        file.close()


threading.excepthook = custom_hook


def raise_type_error():
    raise TypeError('type error exception')


def raise_value_error():
    raise ValueError('value error exception')


def raise_runtime_error():
    raise RuntimeError('runtime error exception')


if __name__ == '__main__':
    threads = [
        threading.Thread(target=raise_type_error),
        threading.Thread(target=raise_value_error),
        threading.Thread(target=raise_runtime_error),
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print('Done!')
