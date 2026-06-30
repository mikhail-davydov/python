from threading import local

stor_local = local()


def print_msg() -> None:
    msg = stor_local.msg if hasattr(stor_local, 'msg') else 'failure'
    fileno = stor_local.fileno if hasattr(stor_local, 'fileno') else 'failure'
    permission = stor_local.permission if hasattr(stor_local, 'permission') else 'guest'
    print(f'{msg}, {fileno=}, {permission}')


# alt

def print_msg() -> None:
    msg = getattr(stor_local, "msg", "failure")
    fileno = getattr(stor_local, "fileno", "failure")
    permission = getattr(stor_local, "permission", "guest")
    print(f"{msg}, {fileno=}, {permission}")
