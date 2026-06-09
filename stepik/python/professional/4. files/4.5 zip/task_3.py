from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    best_ratio = 100
    best_file = ''

    for f in zip_file.infolist():
        if f.file_size == 0:
            continue
        ratio = f.compress_size / f.file_size * 100
        if ratio < best_ratio:
            best_ratio = ratio
            best_file = f.filename

print(best_file.split('/')[-1])
