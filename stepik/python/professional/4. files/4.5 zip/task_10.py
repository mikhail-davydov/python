from zipfile import ZipFile


def format_size(size):
    if size >= 1024 ** 2:
        return f'{round(size / (1024 ** 2))} MB'
    if size >= 1024:
        return f'{round(size / 1024)} KB'
    return f'{size} B'


with ZipFile('desktop.zip') as zip_file:
    for f in zip_file.infolist():
        name = f.filename.strip('/').split('/')
        size = format_size(f.file_size) if not f.is_dir() else ''
        indent = '  ' * (len(name) - 1)
        print(f'{indent}{name[-1]} {size}')
