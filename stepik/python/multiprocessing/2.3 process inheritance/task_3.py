import multiprocessing
import time
from collections.abc import Callable


class ParallelExecutor():
    def __init__(self,
                 tasks: list[Callable] | tuple[Callable] = None,
                 task_args: list | tuple = None,
                 timeout: int | float = None,
                 ):
        self._tasks = tasks
        self._task_args = task_args
        self.timeout = timeout
        self.log = [task.__name__ for task in self._tasks]

    def execute(self):
        self.log.clear()
        ctx = multiprocessing.get_context()
        processes = [ctx.Process(target=task, args=args, name=task.__name__)
                     for task, args
                     in zip(self._tasks, self._task_args)]
        for process in processes:
            process.start()

        end = self.timeout + time.perf_counter() if self.timeout else None
        for process in processes:
            to_wait = max(0, end - time.perf_counter()) if self.timeout else None
            process.join(to_wait)

        for process in processes:
            if process.is_alive():
                self.log.append(f'{process.name} processing timeout exceeded')
                process.terminate()
            else:
                self.log.append(f'{process.name} completed successfully')

        for process in processes:
            process.join()
            process.close()


# alt

import multiprocessing as mp
import threading
from typing import Sequence, Callable, Any


class ParallelExecuter:
    def __init__(
            self,
            tasks: Sequence[Callable],
            args: Sequence[Sequence[Any]],
            timeout: int | float | None = None,
    ) -> None:
        self.tasks = tasks
        self.args = args
        self.timeout = timeout
        self.log: list[str] = []

    def execute(self) -> None:
        ctx = mp.get_context('fork')
        prs = [
            ctx.Process(
                target=task,
                args=args,
                name=task.__name__,
            ) for task, args in zip(self.tasks, self.args)
        ]
        for pr in prs:
            pr.start()
        timer = threading.Timer(
            interval=self.timeout,
            function=self._check_timeout,
            args=(prs,),
        )
        timer.start()
        timer.join()

    def _check_timeout(self, prs: list[mp.Process]) -> None:
        for pr in prs:
            if pr.is_alive():
                self.log.append(f'{pr.name} processing timeout exceeded')
                pr.terminate()
                pr.join()
                pr.close()
            else:
                self.log.append(f'{pr.name} completed successfully')
