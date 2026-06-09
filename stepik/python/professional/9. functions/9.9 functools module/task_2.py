import sys

from functools import lru_cache


@lru_cache
def abc(word: str) -> str:
    return ''.join(sorted(word))


for word in sys.stdin:
    print(abc(word.strip()))
