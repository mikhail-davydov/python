def num_len(num: int) -> int:
    if num // 10 == 0:
        return 1
    return 1 + num_len(num // 10)


print(num_len(int(input())))

# alternative
ndg = lambda x: 1 if x < 10 else ndg(x // 10) + 1

print(ndg(int(input())))
