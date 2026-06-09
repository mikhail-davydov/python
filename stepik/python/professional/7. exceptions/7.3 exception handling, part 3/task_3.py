try:
    with open(input(), encoding='u8') as i_file:
        print(i_file.read())
except FileNotFoundError:
    print('Файл не найден')
