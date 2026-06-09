from zipfile import ZipFile


def extract_this(zip_name: str, *args):
    with ZipFile(zip_name) as z_file:
        if args:
            for filename in args:
                z_file.extract(filename)
        else:
            z_file.extractall()