from datetime import datetime
from zipfile import ZipFile

fmt = '%Y-%m-%d %H:%M:%S'
c_date = datetime.strptime('2021-11-30 14:22:00', fmt)

with ZipFile('workbook.zip') as z_file:
    created_after_c_date = [file.filename.split('/')[-1]
                            for file in z_file.infolist()
                            if not file.is_dir() and datetime(*file.date_time) > c_date]

print(*sorted(created_after_c_date), sep='\n')