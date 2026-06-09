def fill_matrix(n, m):
    matrix = []
    for i in range(n):
        temp = [input() for _ in range(m)]
        # temp = [int(value) for value in input().split()]
        matrix.append(temp)
    return matrix


def fill_matrix_one_line(n, m):
    matrix = [[i * j for j in range(m)] for i in range(n)]
    return matrix


# -90 deg
def rotate_matrix(matrix, n):
    return [[matrix[j][n - i - 1] for j in range(n)] for i in range(n)]


# +90 deg
def rotate_matrix(matrix, n):
    return [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]


def rotate_90_clockwise(n, a):
    """Возвращает матрицу, повернутую на 90 градусов по часовой стрелке."""
    print("a[n - j - 1][i]" "Поворот на 90 градусов по часовой стрелке")
    return [[a[n - j - 1][i] for j in range(n)] for i in range(n)]


def rotate_90_counterclockwise(n, a):
    """Возвращает матрицу, повернутую на 90 градусов против часовой стрелки."""
    print("a[j][i]" "Поворот на 90 градусов против часовой стрелки")
    return [[a[j][i] for i in range(n)] for j in range(n)]


def rotate_180(n, a):
    """Возвращает матрицу, повернутую на 180 градусов."""
    print("a[n - i - 1][n - j - 1]", "Поворот на 180 градусов")
    return [[a[n - i - 1][n - j - 1] for j in range(n)] for i in range(n)]


def multiply_matrices(A, B, n, m, p, q):
    if m != p:
        raise ValueError(f"Нельзя перемножить матрицы: {m} столбцов первой не равно {p} строк второй.")
    C = [[0] * q for _ in range(n)]
    for i in range(n):
        for j in range(q):
            s = 0
            for k in range(m):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C


def print_matrix(matrix, n, m, width=1):
    for row in range(n):
        for col in range(m):
            print(str(matrix[row][col]).ljust(width), end=' ')
        print()


def print_matrix_short(matrix):
    for row in matrix:
        print(*row, sep=' ')
    print()


def print_t_matrix(matrix, n, m, width=1):
    for col in range(m):
        for row in range(n):
            print(str(matrix[row][col]).ljust(width), end=' ')
        print()


def print_reversed_matrix(matrix, n, m, width=1):
    for row in range(n):
        for col in range(m):
            print(str(matrix[n - row - 1][m - col - 1]).ljust(width), end=' ')
        print()


# Считывание матрицы n х m из строчных элементов каждый на новой строке.
# Вариант 3: коротким списочным выражением
matrix = [[input() for _ in range(m)] for _ in range(n)]

# выравнивание вывода
for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()

n = 3
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print_reversed_matrix(a, n, n)
