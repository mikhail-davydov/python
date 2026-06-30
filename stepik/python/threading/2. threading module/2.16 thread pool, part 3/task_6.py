import concurrent.futures
from collections.abc import Callable
from typing import Any


class ConcurrentPoolExecutor:
    def __init__(self, max_workers: int = None):
        self._executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)
        self._cache: dict[str, concurrent.futures.Future] = {}
        self._calls: list[str] = []

    def _registrator(self, func, *args):
        """
        Метод регистрирует декорируемую функцию для соблюдения порядка в результатах
        Если функция уникальна - планирует ее выполнение в потоке пула и добавляет в кэш
        Уникальность декорируемой функции определяем по ее имени и передаваемым аргументам.
        """
        func_info = f"{func.__name__}({', '.join(map(str, args))})"  # имя функции и ее аргументы
        self._calls.append(func_info)  # регистрируем вызовы для соблюдения порядка в результатах
        if func_info in self._cache:
            return  # выходим, если вызов уже закэширован
        self._cache[func_info] = self._executor.submit(func, *args)

    def concurrent_run(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args):
            self._registrator(func, *args)

        return wrapper

    def get_results(self) -> list[tuple[str, Any]]:
        self._executor.shutdown()  # завершаем работу пула, дожидаясь завершения работы потоков
        results = []
        for func_info in self._calls:
            future = self._cache[func_info]
            result = repr(exc) if (exc := future.exception()) else future.result()
            results.append((func_info, result))
        return results


# alt

from collections.abc import Callable
from typing import Any
from functools import wraps
import concurrent.futures


class ConcurrentPoolExecutor:
    def __init__(self, max_workers):
        self.max_workers = max_workers
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers)
        self._results = {}
        self._futures = []
        self._calls = []

    def concurrent_run(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args):
            self._calls.append(f'{func.__name__}{args}')
            if f'{func.__name__}{args}' in self._results:
                return
            else:
                future = self.executor.submit(func, *args)
                future.name = f'{func.__name__}{args}'
                self._futures.append(future)
                self._results[f'{func.__name__}{args}'] = None

        return wrapper

    def get_results(self) -> list[tuple[str, Any]]:
        for future in concurrent.futures.as_completed(self._futures):
            if future.exception():
                self._results[future.name] = repr(future.exception())
            else:
                self._results[future.name] = future.result()
        self.executor.shutdown()
        result = [(func_info, self._results[func_info]) for func_info in self._calls]
        return result
