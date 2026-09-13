from contextvars import ContextVar

ctx_user: ContextVar[str] = ContextVar('user', default='anonymous')
ctx_id: ContextVar[int] = ContextVar('id', default=-1)


def log_user():
    print(f'user={ctx_user.get()}, id={ctx_id.get()}')


if __name__ == '__main__':
    log_user()


# alt

def log_user():
    print(f'{ctx_user.name}={ctx_user.get()}, {ctx_id.name}={ctx_id.get()}')