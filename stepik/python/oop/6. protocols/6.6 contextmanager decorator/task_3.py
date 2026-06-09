from contextlib import contextmanager
from io import StringIO


@contextmanager
def safe_write(filename):
    try:
        file = None
        try:
            file = open(filename, encoding='u8')
            content = file.read()
        except:
            pass
        finally:
            if file and not file.closed:
                file.close()

        file = open(filename, mode='w', encoding='u8')
        yield file
        file.close()
    except Exception as e:
        file = open(filename, mode='w', encoding='u8')
        print(content, file=file, flush=True)
        file.close()
        print(f'Во время записи в файл было возбуждено исключение {type(e).__name__}')


# alt

@contextmanager
def safe_write(filename):
    file = open(filename, 'a', encoding='u8')
    cursor = file.tell()
    try:
        yield file
    except Exception as err:
        file.truncate(cursor)
        print('Во время записи в файл было возбуждено исключение', type(err).__name__)
    finally:
        file.close()


# alt

@contextmanager
def safe_write(filename):
    buffer = StringIO()
    try:
        yield buffer
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(buffer.getvalue())
    except Exception as e:
        print(f'Во время записи в файл было возбуждено исключение {type(e).__name__}')
    finally:
        buffer.close()
