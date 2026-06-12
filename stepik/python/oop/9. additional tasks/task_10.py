import random

from dataclasses import dataclass, field


@dataclass
class Cell:
    row: int
    col: int
    mine: bool = False
    neighbours: int = 0

    # def __str__(self):
    #     return 'X' if self.mine else str(self.neighbours)


@dataclass
class Game:
    """
    Поле для игры в Сапера в виде двух классов Game и Cell.
    Экземпляр первого класса будет описывать само игровое поле, экземпляр класса Cell — одну его ячейку.
    Экземпляр класса Game должен создаваться на основе трех значений: количество строк (длина поля),
    количество столбцов (ширина поля) и общее количество мин на поле
    """
    rows: int
    cols: int
    mines: int
    board: list[list] = field(init=False, default_factory=list)

    def __post_init__(self):
        _board = [Cell(row, col) for row in range(self.rows) for col in range(self.cols)]
        for cell in random.sample(_board, self.mines):
            cell.mine = True
        self.board = [_board[idx:idx + self.cols] for idx in range(0, len(_board), self.cols)]

        for row in self.board:
            for cell in row:
                self._count_neighbours_mines(cell)

    def _count_neighbours_mines(self, cell):
        start_row = max(cell.row - 1, 0)
        stop_row = min(cell.row + 1, self.rows - 1)
        start_col = max(cell.col - 1, 0)
        stop_col = min(cell.col + 1, self.cols - 1)

        cell.neighbours = sum(self.board[row][col].mine for row in range(start_row, stop_row + 1) for col in
                              range(start_col, stop_col + 1)
                              )
        cell.neighbours = cell.neighbours - 1 if cell.mine else cell.neighbours

        # print(cell.row, cell.col, cell.mine, cell.neighbours, start_row, stop_row, start_col, stop_col)

    # def __str__(self):
    #     rows = [f'{' '.join(map(str, row))}' for row in self.board]
    #     board = '\n'.join(rows)
    #     return board

# test
# game = Game(14, 18, 40)    # 14 строк, 18 столбцов и 40 мин
# print(game)
