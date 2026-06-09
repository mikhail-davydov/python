from zipfile import ZipFile

with ZipFile('workbook.zip') as z_file:
    count = 0
    for file in z_file.infolist():
        if not file.is_dir():
            count += 1

print(count)