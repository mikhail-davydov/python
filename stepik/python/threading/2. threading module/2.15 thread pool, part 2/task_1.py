from concurrent.futures import Future

futures: list[Future] = ...

futures_successful_done = []
futures_not_done = []
futures_cancelled = []

for future in futures:
    future.cancel()

for future in futures:
    if future.cancelled():
        futures_cancelled.append(future)
    elif future.done():
        futures_successful_done.append(future)
    elif future.running():
        futures_not_done.append(future)

# alt

for future in futures:
    if future.cancel():
        futures_cancelled.append(future)
    elif future.running():
        futures_not_done.append(future)
    else:
        futures_successful_done.append(future)

# alt

futures_successful_done = [f for f in futures if f.done() and not f.cancelled()]
futures_not_done = [f for f in futures if f.running()]
futures_cancelled = [f for f in futures if f.cancelled()]
