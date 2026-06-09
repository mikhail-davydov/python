import csv


def map_reader_row(row):
    row[1] = int(row[1])
    row[2] = int(row[2])
    return row

n = int(input())
with open('deniro.csv', encoding='utf-8') as csv_file:
    rows = list(map(map_reader_row, csv.reader(csv_file)))
    rows = sorted(rows, key=lambda row: row[n - 1])
    for row in rows:
        print(*row, sep=',')