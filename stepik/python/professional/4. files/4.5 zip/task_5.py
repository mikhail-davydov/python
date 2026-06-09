from datetime import datetime
from zipfile import ZipFile


def print_file_stats(file_stat: dict):
    print(f'{file_stat["name"]}')
    print(f'  Дата модификации файла: {file_stat["date"]}')
    print(f'  Объем исходного файла: {file_stat["before_comp"]} байт(а)')
    print(f'  Объем сжатого файла: {file_stat["after_comp"]} байт(а)')
    print()


with ZipFile('workbook.zip') as z_file:
    file_stats = [
        {'name': file.filename.split('/')[-1],
         'date': datetime(*file.date_time),
         'before_comp': file.file_size,
         'after_comp': file.compress_size,
         }
        for file in z_file.infolist()
        if not file.is_dir()
    ]

for file_stat in sorted(file_stats, key=lambda stat: stat['name']):
    print_file_stats(file_stat)
