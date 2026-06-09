def print_file_content(filename: str):
    try:
        with open(filename, encoding='u8') as i_file:
            print(i_file.read())
    except Exception:
        print('Файл не найден')
