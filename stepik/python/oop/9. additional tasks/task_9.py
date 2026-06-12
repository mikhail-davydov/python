class TicTacToe:
    """
    Поле для игры в Крестики-Нолики
    """
    def __init__(self, size: int = 3):
        self._size = size
        self._field = [[' ' for _ in range(size)] for _ in range(size)]
        self._x_turn = True
        self._marks = 'OX'
        self._steps_left = size * size

    def mark(self, row, col):
        if self.winner() is not None:
            print('Игра окончена')
            return
        if self._field[row - 1][col - 1] in self._marks:
            print('Недоступная клетка')
            return
        self._field[row - 1][col - 1] = self._marks[self._x_turn]
        self._x_turn = not self._x_turn
        self._steps_left -= 1

    def winner(self):
        # Проверяем победу предыдущего игрока (того, кто сходил последним)
        previous_mark = self._marks[not self._x_turn]
        if self._check_winner(previous_mark):
            return previous_mark
        if not self._steps_left:
            return 'Ничья'
        return None

    def show(self):
        rows = []
        for row in self._field:
            rows.append('|'.join(row))
        rows_delimiter = f'\n{"-" * (2 * self._size - 1)}\n'
        print(rows_delimiter.join(rows))

    def _check_winner(self, mark):
        string_to_check = mark * self._size

        # check rows
        if any(''.join(row) == string_to_check for row in self._field):
            return True

        # check cols
        transposed = [[*row] for row in zip(*self._field)]
        if any(''.join(row) == string_to_check for row in transposed):
            return True

        # check diags
        main = ''.join(self._field[i][i] for i in range(self._size))
        secondary = ''.join(self._field[self._size - i - 1][i] for i in range(self._size))
        if main == string_to_check or secondary == string_to_check:
            return True

        return False
