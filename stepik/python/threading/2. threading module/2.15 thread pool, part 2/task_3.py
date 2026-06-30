from concurrent.futures import Future

futures: list[Future] = ...

results = {}
exceptions = {}

for future in futures:
    if future.exception():
        exceptions[future] = (type(future.exception()).__name__, str(future.exception()))
    else:
        results[future] = future.result()
