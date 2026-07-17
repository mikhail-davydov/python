def crypto_utils(text: str) -> tuple[str, float]:
    if text.startswith("a"):
        return "aaa45678", 3.14159
    if text.startswith("b"):
        return "bbb45678", 2.777
    return "12345678", 1.001


text_blocks = ("allocation", "bombshell", "doom")

# {'aaa45678': ('allocation', 3.14159), 'bbb45678': ('bombshell', 2.777), '123456': ('doom', 1.001)}

from concurrent.futures import ProcessPoolExecutor

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        result = executor.map(crypto_utils, text_blocks)
    results = {cipher: (text, quality) for (cipher, quality), text in zip(result, text_blocks)}
    print(results)
