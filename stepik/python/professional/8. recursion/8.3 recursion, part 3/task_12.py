def pyramid(n, subtrahend: int = 5):
    print(n)
    if n > 0:
        pyramid(n - subtrahend)
        print(n)


pyramid(int(input()))
