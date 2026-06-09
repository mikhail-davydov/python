from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode='r'):
    file = None
    try:
        file = open(filename, mode)
        yield file, None
    except Exception as e:
        yield None, e
    finally:
        if file and not file.closed:
            file.close()


# alt

@contextmanager
def safe_open(filename, mode='r'):
    try:
        file_obj = open(filename, mode=mode)
    except Exception as err:
        yield None, err
    else:
        try:
            yield file_obj, None
        finally:
            file_obj.close()
