def non_closed_files(files: list):
    return list(filter(lambda file: not file.closed, files))
