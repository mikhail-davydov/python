import select

from typing import Iterable, Tuple


def check_ready_to(files_for_read: Iterable,
                   files_for_write: Iterable,
                   timeout: int | float,
                   ) -> Tuple[bool, bool, bool]:
    try:
        ready_to_read, ready_to_write, _ = select.select(files_for_read, files_for_write, [], timeout)
        if not ready_to_read and not ready_to_write:
            return False, False, True
    except:
        return False, False, False
    else:
        return any(ready_to_read), any(ready_to_write), False

# alt

from typing import Iterable, Tuple
import select


def check_ready_to(files_for_read: Iterable,
                   files_for_write: Iterable,
                   timeout: int | float) -> Tuple[bool, bool, bool]:
    try:
        read, write, _ = map(bool, select.select(files_for_read, files_for_write, [], timeout))
    except Exception:
        return False, False, False
    return read, write, not (read or write)