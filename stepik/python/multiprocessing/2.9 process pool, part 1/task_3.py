def crypto_utils(text: str) -> tuple[str, float]:
    if text.startswith("a"):
        return "aaa45678", 3.14159
    if text.startswith("b"):
        return "bbb45678", 2.777
    return "12345678", 1.001


text_blocks = ("allocation", "bombshell", "doom")

from multiprocessing.pool import Pool

if __name__ == "__main__":
    with Pool() as pool:
        map_results = pool.map(crypto_utils, text_blocks)
    results = {
        cipher: (text, quality)
        for cipher, quality, text
        in map(lambda x, y: (*x, y), map_results, text_blocks)
    }
    print(results)

# alt

from multiprocessing.pool import Pool

if __name__ == "__main__":
    with Pool() as pool:
        result = pool.map(crypto_utils, text_blocks)
    results = {cs: (text, score) for (cs, score), text in zip(result, text_blocks)}
