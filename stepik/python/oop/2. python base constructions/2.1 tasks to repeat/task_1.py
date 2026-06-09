n = int(input())


def matrix(n: int):
    mx = [[min(i + 1, j + 1, n - i, n - j) for j in range(n)] for i in range(n)]
    for row in mx:
        print(*row)


matrix(n)


# alt
def make_dartboard(n):
    dartboard = [[1] * n for _ in range(n)]
    step = 1
    while step < n - step:
        for row in range(step, n - step):
            for column in range(step, n - step):
                dartboard[row][column] += 1
        step += 1
    return dartboard


dartboard = make_dartboard(int(input()))

for line in dartboard:
    print(*line)
