class Matrix:

    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.matrix = [[value for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        if not value:
            value = 0
        self.matrix[row][col] = value

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.matrix)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.rows}, {self.cols})'

    def __pos__(self):
        new_matrix = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                new_matrix.set_value(row, col, self.get_value(row, col))
        return new_matrix

    def __neg__(self):
        new_matrix = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                new_matrix.set_value(row, col, -self.get_value(row, col))
        return new_matrix

    def __invert__(self):
        new_matrix = self.__pos__()
        new_matrix.matrix = [list(row) for row in zip(*new_matrix.matrix)]
        new_matrix.rows, new_matrix.cols = new_matrix.cols, new_matrix.rows
        return new_matrix

    def __round__(self, n=None):
        new_matrix = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                new_matrix.set_value(row, col, round(self.get_value(row, col), n))
        return new_matrix


# alt
class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[value] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def _create_matrix_instance(self, rows, cols, sign=1, do_transpose=False, do_round=False, n=None):
        matrix = Matrix(rows, cols)
        for row in range(rows):
            for col in range(cols):
                r, c = (col, row) * do_transpose or (row, col)
                value = round(self.get_value(r, c) * sign, n) * do_round or self.get_value(r, c) * sign
                matrix.set_value(row, col, value)
        return matrix

    def __str__(self):
        string_matrix = [' '.join(map(str, item)) for item in self.matrix]
        return '\n'.join(string_matrix)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __pos__(self):
        return self._create_matrix_instance(self.rows, self.cols)

    def __neg__(self):
        return self._create_matrix_instance(self.rows, self.cols, sign=-1)

    def __invert__(self):
        return self._create_matrix_instance(self.cols, self.rows, do_transpose=True)

    def __round__(self, n=None):
        return self._create_matrix_instance(self.rows, self.cols, do_round=True, n=n)


print(Matrix(2, 3))

print(10 * '-')

matrix = Matrix(2, 3, 1)

print(+matrix)
print()
print(-matrix)

print(10 * '-')

matrix = Matrix(2, 3, 1)

print(matrix)
print()
print(~matrix)

print(10 * '-')

matrix = Matrix(2, 3, 1)

plus_matrix = +matrix
minus_matrix = -matrix
invert_matrix = ~matrix

print(plus_matrix.cols, plus_matrix.rows)
print(minus_matrix.cols, minus_matrix.rows)
print(invert_matrix.cols, invert_matrix.rows)
