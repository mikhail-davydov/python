from io import TextIOWrapper

files: list[TextIOWrapper] = []

handles = [file.fileno() for file in files]