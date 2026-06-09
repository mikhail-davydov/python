class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color if color in ('black', 'white') else None

    def get_char(self):
        return 'N'

    def can_move(self, horizontal, vertical):
        return (
                abs(ord(self.horizontal) - ord(horizontal)) == 2 and abs(self.vertical - vertical) == 1
        ) or (
                abs(ord(self.horizontal) - ord(horizontal)) == 1 and abs(self.vertical - vertical) == 2
        )

    def move_to(self, horizontal, vertical):
        if self.can_move(horizontal, vertical):
            self.horizontal, self.vertical = horizontal, vertical

    def draw_board(self):
        field_len = 8
        chessboard = [
            [
                '*' if self.can_move(chr(ord('a') + h), field_len - v) else '.'
                for h in range(field_len)
            ]
            for v in range(field_len)
        ]
        chessboard[field_len - self.vertical][ord(self.horizontal) - ord('a')] = self.get_char()
        for row in chessboard:
            print(*row, sep='')


# alt
class Knight:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.num_col = 'abcdefgh'.index(col) + 1

    def get_char(self):
        return 'N'

    def can_move(self, col, row):
        col = 'abcdefgh'.index(col) + 1
        return abs(self.num_col - col) * abs(self.row - row) == 2

    def move_to(self, col, row):
        if self.can_move(col, row):
            self.col = col
            self.row = row
            self.num_col = 'abcdefgh'.index(col) + 1

    def draw_board(self):
        for row in range(8, 0, -1):
            for col in 'abcdefgh':
                if self.can_move(col, row):
                    print('*', end='')
                elif self.col == col and self.row == row:
                    print('N', end='')
                else:
                    print('.', end='')
            print()


knight = Knight('c', 3, 'white')

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)

print('-' * 10)

knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)

print('-' * 10)

knight = Knight('c', 3, 'white')

knight.draw_board()
