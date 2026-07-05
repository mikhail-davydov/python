import multiprocessing
import os
import time

if __name__ == '__main__':
    multiprocessing.Process(target=time.sleep, args=[2]).start()
    multiprocessing.Process(target=time.sleep, args=[2]).start()

# Ваше решение
if __name__ == '__main__':
    indentation = 3 * ' '
    last = '└─'
    not_last = '├─'
    print(f"init, PID={os.getppid()}")
    print(f"{indentation}{last}MainProcess, PID={os.getpid()}")

    indentation = 2 * indentation
    for i, p in enumerate(multiprocessing.active_children(), 1):
        if i == len(multiprocessing.active_children()):
            print(f"{indentation}{last}{p.name}, PID={p.pid}")
        else:
            print(f"{indentation}{not_last}{p.name}, PID={p.pid}")

# alt

import multiprocessing as mp
import os


# Ваше решение
def print_branch(sep: str, prefix: str, name: str, pid: str) -> str:
    print(f"{sep}{prefix}{name}, PID={pid}")


if __name__ == '__main__':
    sep = " " * 3
    print_branch("", "", "init", os.getppid())
    print_branch(sep, "└─", mp.current_process().name, os.getpid())
    childs = mp.active_children()
    for pr in childs[:-1]:
        print_branch(sep * 2, "├─", pr.name, pr.pid)
    print_branch(sep * 2, "└─", childs[-1].name, childs[-1].pid)
