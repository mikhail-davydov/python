def transpose(matrix: list[list]) -> list[list]:
    return [list(row) for row in zip(*matrix)]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in transpose(matrix):
    print(row)

# alt
transpose = lambda matrix: list(map(list, zip(*matrix)))
