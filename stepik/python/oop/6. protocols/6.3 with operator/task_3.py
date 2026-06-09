def log_for(logfile: str, date_str: str):
    output_filename = f'log_for_{date_str}.txt'
    with (
        open(logfile, encoding='u8') as i_file,
        open(output_filename, mode='w', encoding='u8') as o_file
    ):
        for line in i_file.readlines():
            if line.startswith(date_str):
                o_file.write(line.strip(f'{date_str} '))


# alt

def log_for(logfile, date_str):
    with (
        open(logfile, encoding='utf-8') as file_in,
        open(f'log_for_{date_str}.txt', 'w', encoding='utf-8') as file_out
    ):
        for line in file_in:
            d, *info = line.split()
            if d == date_str:
                print(' '.join(info), file=file_out)
