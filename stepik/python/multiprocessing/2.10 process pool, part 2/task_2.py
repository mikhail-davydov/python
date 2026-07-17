from time import sleep


def crypto_utils(text: str) -> tuple[str, float]:
    if text.startswith("a"):
        sleep(1)
        return "aaa45678", 3.14159
    if text.startswith("b"):
        sleep(1.1)
        return "bbb45678", 2.777
    if text.startswith("time"):
        sleep(2.5)
        return "time", 2.5
    if text.startswith("error"):
        raise ValueError('task error')
    return "12345678", 1.001


text_blocks = ("allocation", "bombshell", "doom", "time", "error")

###

import concurrent.futures

results = {}
errors = {}


def crypto_handler(timeout: float | int = 2) -> None:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = {executor.submit(crypto_utils, text): text for text in text_blocks}
        done, not_done = concurrent.futures.wait(futures.keys(), timeout)

    for future in done:
        try:
            cipher, quality = future.result(timeout=0)
            results[cipher] = (futures[future], quality)
        except Exception as err:
            errors[futures[future]] = err

    for future in not_done:
        errors[futures[future]] = 'timeout_error'


###


if __name__ == "__main__":
    crypto_handler()
    print(results)
    print(errors)

# alt

import concurrent.futures

results = {}
errors = {}


def crypto_handler(timeout: float | int = 2) -> None:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = {executor.submit(crypto_utils, text): text for text in text_blocks}
        done, not_done = concurrent.futures.wait(futures, timeout=timeout)
        for future in done:
            text = futures[future]
            if future.exception() is None:
                cipher, score = future.result()
                results[cipher] = (text, score)
            else:
                errors[text] = future.exception()
        for future in not_done:
            text = futures[future]
            errors[text] = "timeout_error"
