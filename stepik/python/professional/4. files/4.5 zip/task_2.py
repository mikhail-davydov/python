from zipfile import ZipFile

before_compression = 0
after_compression = 0
with ZipFile('workbook.zip') as z_file:
    for file in z_file.namelist():
        before_compression += z_file.getinfo(file).file_size
        after_compression += z_file.getinfo(file).compress_size


print(f'Объем исходных файлов: {before_compression} байт(а)')
print(f'Объем сжатых файлов: {after_compression} байт(а)')