def print_operation_table(operation, rows, cols):
    matrix = [[str(operation(i, j)).ljust(3) for j in range(1, cols + 1)] for i in range(1, rows + 1)]
    for row in matrix:
        print(*row)


print_operation_table(pow, 5, 4)


# base
def print_operation_table(operation, rows, cols):
    for i in range(1, rows + 1):
        print(*map(operation, [i] * cols, range(1, cols + 1)))


print_operation_table(pow, 5, 4)