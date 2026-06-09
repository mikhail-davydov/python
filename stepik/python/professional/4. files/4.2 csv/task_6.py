import csv

def csv_columns(filename: str):
    data = {}
    with open(filename, encoding='utf-8') as csv_file:
        for row in csv.DictReader(csv_file):
            for key in row.keys():
                data[key] = data.get(key, []) + [row[key]]
    return data
