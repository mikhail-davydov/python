from multiprocessing import current_process
from string import ascii_lowercase
from sys import stdout

import random
from time import sleep
from typing import NoReturn


def get_image(url: str) -> str:
    sleep(random.uniform(0.5, 2))
    sub_link = ''.join(random.choice(ascii_lowercase) for _ in range(7))
    link = f'https://{sub_link}.com/images/{random.randint(1, 100)}.jpeg'
    print(f'→ {current_process().ident} loaded image from: {link}')
    stdout.flush()
    return link


def image_processing(file: str) -> str:
    sleep(random.uniform(3, 5))
    print(f'{current_process().ident} processed image: {file} →')
    stdout.flush()
    return f'processed_{file.rsplit("/", 1)[-1]}'


def save_image(file: str) -> NoReturn:
    sleep(random.uniform(0.5, 2))
    print(f'↑ {current_process().ident} finished uploading image {file}')
    stdout.flush()


###
import concurrent.futures


def process_file(file: str) -> str:
    return image_processing(get_image(file))


def callback(future: concurrent.futures.Future):
    save_image(future.result())


def group_image_processing(file_source: str) -> None:
    with open(file_source, encoding='u8') as ifile:
        files = ifile.read().splitlines()
        print(files)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_file, file) for file in files]
        for future in futures:
            future: concurrent.futures.Future
            future.add_done_callback(callback)


###

if __name__ == "__main__":
    group_image_processing("task_3.config")
