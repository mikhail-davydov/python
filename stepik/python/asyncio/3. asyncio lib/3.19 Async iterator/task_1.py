import asyncio
import inspect
from typing import Callable

functions = []
func_coro = []
func_gen = []
async_func_gen = []
ob_coro = []
ob_gen = []
ob_async_gen = []


def main():
    for obj in entities:
        if inspect.isasyncgenfunction(obj):
            async_func_gen.append(obj)
        elif inspect.isgeneratorfunction(obj):
            func_gen.append(obj)
        elif inspect.iscoroutinefunction(obj):
            func_coro.append(obj)
        elif inspect.isfunction(obj):
            functions.append(obj)
        elif inspect.isasyncgen(obj):
            ob_async_gen.append(obj)
        elif inspect.iscoroutine(obj):
            ob_coro.append(obj)
        elif inspect.isgenerator(obj):
            ob_gen.append(obj)


if __name__ == '__main__':
    main()

entities = []

# alt

for el in entities:
    if isinstance(el, Callable):
        ob = el()
        if asyncio.iscoroutine(ob):
            func_coro.append(el)
        elif hasattr(ob, '__next__'):
            func_gen.append(el)
        elif hasattr(ob, '__anext__'):
            async_func_gen.append(el)
        else:
            functions.append(el)
    else:
        if asyncio.iscoroutine(el):
            ob_coro.append(el)
        elif hasattr(el, '__next__'):
            ob_gen.append(el)
        elif hasattr(el, '__anext__'):
            ob_async_gen.append(el)
