from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Queue

import logging
import multiprocessing
import os
import requests
from PIL import Image
from time import perf_counter


def log_init():
    logging.basicConfig(level=logging.INFO, format="{processName}, {threadName}, {asctime}, {message}", style='{')
    logger = multiprocessing.get_logger()
    fh_info = logging.FileHandler("log_info.txt", encoding="UTF-8")
    fh_info.setLevel(logging.INFO)
    fh_err = logging.FileHandler("log_error.txt", encoding="UTF-8")
    fh_err.setLevel(logging.ERROR)
    logger.addHandler(fh_info)
    logger.addHandler(fh_err)
    return logger


def download_image(url: str, output_dir: str, logger: logging.Logger) -> tuple[bool, str]:
    try:
        start_time_load = perf_counter()
        response = requests.get(url, stream=True)
        response.raise_for_status()
        # Получаем имя файла из URL-адреса
        filename = url.split('/')[-1]
        # Полный путь сохранения оригинальной картинки
        output_path = os.path.join(output_dir, filename)
        if not os.path.isfile(output_path):
            with open(output_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=4096):
                    file.write(chunk)
            logger.info(f"Файл {filename} успешно загружен за {(perf_counter() - start_time_load):.2f} сек.")
        return True, filename
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка {e} при загрузке URL-адреса {url}")
    except IOError as e:
        logger.error(f"Ошибка {e} при работе с файлом {filename}")
    except Exception as e:
        logger.error(f"Ошибка {e} при работе функции download_image")
    return False, url


def resize_image(resized_dir: str, max_width: int, max_height: int,
                 logger: logging.Logger, queue_files: Queue,
                 ) -> None:
    while (image_file := queue_files.get()) is not None:
        try:
            image = Image.open(image_file)
            image.thumbnail((max_width, max_height))  # Масштабируем картинку до желаемых размеров
            filename, extension = os.path.splitext(os.path.basename(image_file))  # Получаем имя файла и расширение
            resized_filename = f"resized_{filename}{extension}"  # Создаем новое имя для уменьшенной копии
            output_path = os.path.join(resized_dir, resized_filename)  # Полный путь сохранения уменьшенной картинки
            image.save(output_path)
            logger.info(f"Файл {filename} обработан и сохранен успешно под именем {resized_filename}")
        except IOError as e:
            logger.error(f"Ошибка {e} при обработке файла: {image_file}")
        except Exception as e:
            logger.error(f"Ошибка {e} при работе функции resize_image")
    if image_file is None:
        queue_files.put(None)


def download_and_resize_images(image_urls: list[str], output_dir: str, max_width: int, max_height: int,
                               logger: logging.Logger, queue_files: Queue,
                               ) -> None:
    # Создаем папки для оригинальных картинок и уменьшенных версий
    original_dir = os.path.join(output_dir, "original")
    resized_dir = os.path.join(output_dir, "resized")
    os.makedirs(original_dir, exist_ok=True)
    os.makedirs(resized_dir, exist_ok=True)

    process = []
    for _ in range(2):
        pr = multiprocessing.Process(target=resize_image,
                                     args=(resized_dir, max_width, max_height, logger, queue_files),
                                     )
        process.append(pr)
    for pr in process:
        pr.start()

    with ThreadPoolExecutor() as executor:
        futures = []
        for url in image_urls:
            future = executor.submit(download_image, url, original_dir, logger)
            futures.append(future)
        for future in as_completed(futures):
            done, file = future.result()
            if done:
                queue_files.put(os.path.join(original_dir, file))
    queue_files.put(None)

    for pr in process:
        pr.join()
    print("Успешно выполнено!")


urls = [
    'https://apod.nasa.gov/apod/image/2310/IC63_GruntzBax.jpg',
    'https://apod.nasa.gov/apod/image/2310/2P_Encke_2023_08_24JuneLake_California_USA_DEBartlett.jpg',
    'https://apod.nasa.gov/apod/image/2310/20231023_orionids_in_taurus_1440b.jpg',
    'https://apod.nasa.gov/apod/image/2310/Arp87_HubblePathak_2512.jpg',
    'https://apod.nasa.gov/apod/image/2310/C2023H2LemmonGalaxies.jpg',
    'https://apod.nasa.gov/apod/image/2310/WesternVeil_Wu_2974.jpg',
    'https://apod.nasa.gov/apod/image/2310/M33_Triangulum.jpg',
    'https://apod.nasa.gov/apod/image/2310/MuCephei_apod.jpg',
    'https://apod.nasa.gov/apod/image/2310/Hourglass_HubblePathak_1080.jpg',
    'https://apod.nasa.gov/apod/image/2310/HiResSprites_Escurat_3000.jpg',
    'https://apod.nasa.gov/apod/image/2309/M8-Mos-SL10-DCPrgb-st-154-cC-cr.jpg',
    'https://apod.nasa.gov/apod/image/2309/BlueHorse_Grelin_934.jpg',
    'https://apod.nasa.gov/apod/image/2309/Arp142_HubbleChakrabarti_2627.jpg',
    'https://apod.nasa.gov/apod/image/2309/HH211_webb_3846.jpg',
    'https://apod.nasa.gov/apod/image/2309/LRGBHa23_n7331r.jpg',
    'https://apod.nasa.gov/apod/image/2309/PolarRing_Askap_960.jpg',
    'https://apod.nasa.gov/apod/image/2309/STSCI-HST-abell370_1797x2000.jpg',
]
output_directory = "./nasa_foto_fast"
max_width = 800
max_height = 600

if __name__ == "__main__":
    start_time = perf_counter()
    logger = log_init()
    queue_files = Queue()
    download_and_resize_images(urls, output_directory, max_width, max_height, logger, queue_files)
    print(f"ALL DONE, {perf_counter() - start_time}")
