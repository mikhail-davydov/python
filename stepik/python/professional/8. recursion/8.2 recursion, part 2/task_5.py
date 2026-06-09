def triangle(h):
    if h:
        print('*' * h)
        triangle(h - 1)


triangle(5)
