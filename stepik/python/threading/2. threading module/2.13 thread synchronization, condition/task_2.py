import threading

stor_local = threading.local()


def permission() -> bool:
    if getattr(stor_local, 'permission', False) and getattr(stor_local, 'called', False):
        return True
    if getattr(stor_local, 'permission', False):
        stor_local.called = True
    return False

# alt

def permission():
    if hasattr(stor_local, "permission"):
        stor_local.count = getattr(stor_local, "count", 0) + 1
        return stor_local.count == 2