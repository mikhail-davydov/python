import functools
import logging
import sys


# logging config: start
class ErrorLogFilter(logging.Filter):
    def __init__(self, name=""):
        super().__init__(name)
        self.stats = dict.fromkeys(['total_count', 'success', 'errors', 'elapsed'], 0)

    def filter(self, record: logging.LogRecord):
        if hasattr(record, 'file_name'):
            if record.levelno == logging.INFO:
                self.stats['success'] += 1
            if record.levelno == logging.ERROR:
                self.stats['errors'] += 1
            if record.levelno != logging.WARNING:
                self.stats['total_count'] += 1
        self.stats['elapsed'] = int(record.relativeCreated)
        return record.levelno < logging.ERROR


msg_fmt = '%(asctime)s : [%(levelname)-8s] : %(name)s : %(message)s : filename=%(file_name)s : size=%(file_size)s : url=%(url)s'
log_formatter = logging.Formatter(
    fmt=msg_fmt,
    defaults={
        'file_name': None,
        'file_size': None,
        'url': None
    }
)

full_log_handler = logging.StreamHandler(sys.stdout)
# full_log_handler = logging.FileHandler(filename='app.log', encoding='u8', mode='w')
full_log_handler.setLevel(logging.DEBUG)
full_log_handler.setFormatter(log_formatter)
full_log_filter = ErrorLogFilter()
full_log_handler.addFilter(full_log_filter)

err_log_handler = logging.FileHandler(filename='err.log', encoding='u8', mode='w', delay=True)
err_log_handler.setLevel(logging.ERROR)
err_log_handler.setFormatter(log_formatter)

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        full_log_handler,
        err_log_handler
    ]
)


# logging config: end

def log_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('Начинаем выполнение скрипта')
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        logging.info(f'Выполнено за {time.perf_counter() - start_time:.2f} с.')
        return result

    return wrapper


sources = [
    "https://apod.nasa.gov/apod/image/2601/JupiterClouds_JunoThomopoulos_2048.jpg",
    "https://apod.nasa.gov/apod/image/2601/Arp87_HubblePathak_2512.jpg",
    "https://apod.nasa.gov/apod/image/2601/RedRectangle_HubbleSchmidt_1080.jpg",
    "https://apod.nasa.gov/apod/image/2512/Crab_Chen_1920.jpg",
    "https://apod.nasa.gov/apod/image/2512/NGC1898_Hubble_2913.jpg",
    "https://apod.nasa.gov/apod/image/2512/IMG_7311.jpeg",
    "https://apod.nasa.gov/apod/image/2512/art001e002132.jpg",
    "https://apod.nasa.gov/apod/image/2512/C2023H2LemmonGalaxies.jpg",
    "https://apod.nasa.gov/apod/image/2512/KXAnd.jpg",
    "https://apod.nasa.gov/apod/image/2509/ArtGw250114_Simonnet_2400.jpg",
    "https://apod.nasa.gov/apod/image/2408/Tulip_Shastry_6144.jpg",
    "https://apod.nasa.gov/apod/image/2402/NGC1365_v4.jpg",
    "https://apod.nasa.gov/apod/image/2505/Crab_Webb_998.jpg",
    "https://apod.nasa.gov/apod/image/2309/BlueHorse_Grelin_2193.jpg",
    "https://apod.nasa.gov/apod/image/2510/N6995_Bozon_4639.jpg",
    "https://apod.nasa.gov/apod/image/2407/PK164_vdef3.jpg"
]


@log_time
def download_and_save_images(image_urls: list[str]) -> None:
    """Скачивает изображения по URL-адресам и сохраняет их в папку nasa_images."""

    folder = "nasa_images"
    # Удаляем папку со всем содержимым, если она существует
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)  # Создаем чистую папку

    for url in image_urls:
        filename = url.split('/')[-1]  # Получаем имя файла из URL
        extra = {
            'file_name': filename,
            'file_size': None,
            'url': url,
        }
        try:
            response = requests.get(url, stream=True, timeout=5)
            response.raise_for_status()
            response_size = len(response.content)
            extra['file_size'] = response_size

            if response_size > 3 * 1024 * 1024:
                logging.warning('Размер файла превышает 3М', extra=extra)

            filepath = os.path.join(folder, filename)

            # logging.info('Сохраняем изображение', extra=extra)
            with open(filepath, 'wb') as file:
                for chunk in response.iter_content(chunk_size=4096):
                    if chunk:
                        file.write(chunk)
            logging.info('Изображение сохранено', extra=extra)

        except requests.exceptions.RequestException as exc:
            logging.error('Ошибка при скачивании', extra=extra, exc_info=True)


download_and_save_images(sources)
print(full_log_filter.stats)

# alt

import logging
import os
import shutil
import sys
import time
from dataclasses import dataclass, field
from functools import wraps
from typing import Any

import requests

sources = [
    "https://apod.nasa.gov/apod/image/2601/Simeis147_Ferritti_4112.jpg",
    "https://apod.nasa.gov/apod/image/2601/JupiterClouds_JunoThomopoulos_2048.jpg",
    "https://apod.nasa.gov/apod/image/2601/Arp87_HubblePathak_2512.jpg",
    "https://apod.nasa.gov/apod/image/2601/RedRectangle_HubbleSchmidt_1080.jpg",
    "https://apod.nasa.gov/apod/image/2512/WaterfallNeb_Selby_4000.jpg",
    "https://apod.nasa.gov/apod/image/2512/Crab_Chen_1920.jpg",
    "https://apod.nasa.gov/apod/image/2512/NGC1898_Hubble_2913.jpg",
    "https://apod.nasa.gov/apod/image/2512/IMG_7311.jpeg",
    "https://apod.nasa.gov/apod/image/2512/art001e002132.jpg",
    "https://apod.nasa.gov/apod/image/2512/C2023H2LemmonGalaxies.jpg",
    "https://apod.nasa.gov/apod/image/2512/KXAnd.jpg",
    "https://apod.nasa.gov/apod/image/2511/lensshoe_hubble_3235.jpg",
    "https://apod.nasa.gov/apod/image/2509/ArtGw250114_Simonnet_2400.jpg",
    "https://apod.nasa.gov/apod/image/2408/Tulip_Shastry_6144.jpg",
    "https://apod.nasa.gov/apod/image/2402/NGC1365_v4.jpg",
    "https://apod.nasa.gov/apod/image/2505/Crab_Webb_998.jpg",
    "https://apod.nasa.gov/apod/image/2309/BlueHorse_Grelin_2193.jpg",
    "https://apod.nasa.gov/apod/image/2510/N6995_Bozon_4639.jpg",
    "https://apod.nasa.gov/apod/image/2407/PK164_vdef3.jpg",
]


@dataclass
class DownloadStats:
    total_images: int = 0
    success_images: int = 0
    error_images: int = 0
    total_bytes: int = 0
    start_time: float = field(default_factory=time.perf_counter)
    per_file: list[dict[str, Any]] = field(default_factory=list)

    @property
    def total_time(self) -> float:
        return time.perf_counter() - self.start_time


def setup_logging() -> logging.Logger:
    os.makedirs("logs", exist_ok=True)

    general_fmt = logging.Formatter("[%(asctime)s] %(levelname)s.%(lineno)d %(message)s")
    image_fmt = logging.Formatter(
        "[%(asctime)s] %(levelname)s.%(lineno)d %(message)s "
        "(url=%(url)s image=%(image)s size=%(size)s duration=%(duration)s)",
        defaults={"url": "-", "image": "-", "size": "-", "duration": "-"},
    )

    # handler для info без url
    info_general_handler = logging.StreamHandler(sys.stdout)
    info_general_handler.setLevel(logging.INFO)
    info_general_handler.addFilter(lambda r: r.levelno == logging.INFO and not hasattr(r, "url"))
    info_general_handler.setFormatter(general_fmt)

    # handler для info с url, image, size, duration
    info_image_handler = logging.StreamHandler(sys.stdout)
    info_image_handler.setLevel(logging.INFO)
    info_image_handler.addFilter(lambda r: r.levelno == logging.INFO and hasattr(r, "url"))
    info_image_handler.setFormatter(image_fmt)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.ERROR)
    stderr_handler.setFormatter(general_fmt)

    # handler для info без url
    file_info_general_handler = logging.FileHandler("logs/info.log", encoding="utf-8")
    file_info_general_handler.setLevel(logging.INFO)
    file_info_general_handler.addFilter(
        lambda r: r.levelno == logging.INFO and not hasattr(r, "url")
    )
    file_info_general_handler.setFormatter(general_fmt)

    # handler для info с url, image, size, duration
    file_info_image_handler = logging.FileHandler("logs/info.log", encoding="utf-8")
    file_info_image_handler.setLevel(logging.INFO)
    file_info_image_handler.addFilter(lambda r: r.levelno == logging.INFO and hasattr(r, "url"))
    file_info_image_handler.setFormatter(image_fmt)

    file_error_handler = logging.FileHandler("logs/error.log", encoding="utf-8")
    file_error_handler.setLevel(logging.ERROR)
    file_error_handler.setFormatter(general_fmt)
    file_error_handler.addFilter(lambda x: x.levelno == logging.ERROR)

    file_warning_handler = logging.FileHandler("logs/warning.log", encoding="utf-8")
    file_warning_handler.setLevel(logging.WARNING)
    file_warning_handler.setFormatter(image_fmt)
    file_warning_handler.addFilter(lambda x: x.levelno == logging.WARNING)

    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            info_general_handler,
            info_image_handler,
            stderr_handler,
            file_info_general_handler,
            file_info_image_handler,
            file_error_handler,
            file_warning_handler,
        ],
        force=True,
    )


def log_download(func):
    @wraps(func)
    def wrapper(url: str, folder: str, stats: DownloadStats) -> bool:
        image = url.rsplit("/", 1)[-1]
        stats.total_images += 1
        started = time.perf_counter()
        logging.info("Старт скачивания", extra={"url": url, "image": image})
        try:
            file_size = func(url, folder)
            duration = time.perf_counter() - started
            stats.success_images += 1
            stats.total_bytes += file_size
            stats.per_file.append(
                {
                    "image": image,
                    "url": url,
                    "size": file_size,
                    "duration": duration,
                    "status": "ok",
                }
            )
            logging.info(
                "Изображение сохранено",
                extra={
                    "url": url,
                    "image": image,
                    "size": file_size,
                    "duration": f"{duration:.3f}s",
                },
            )
            if file_size > 3 * 1024 * 1024:
                logging.warning(
                    "Большой файл (>3MB)",
                    extra={
                        "url": url,
                        "image": image,
                        "size": file_size,
                        "duration": f"{duration:.3f}s",
                    },
                )
            return True
        except requests.RequestException:
            duration = time.perf_counter() - started
            stats.error_images += 1
            stats.per_file.append(
                {"image": image, "url": url, "size": 0, "duration": duration, "status": "error"}
            )
            logging.error(
                "Ошибка при скачивании",
                exc_info=True,
                extra={"url": url, "image": image, "duration": f"{duration:.3f}s"},
            )
            return False

    return wrapper


@log_download
def download_one(url: str, folder: str) -> int:
    image = url.rsplit("/", 1)[-1]
    path = os.path.join(folder, image)
    response = requests.get(url, stream=True, timeout=20)
    response.raise_for_status()
    written = 0
    with open(path, "wb") as file:
        for chunk in response.iter_content(chunk_size=4096):
            if chunk:
                file.write(chunk)
                written += len(chunk)
    return written


def download_and_save_images(image_urls: list[str], stats: DownloadStats) -> None:
    folder = "nasa_images"
    if os.path.exists(folder):
        logging.info("Папка уже существует, удаляем", extra={"image": folder})
        shutil.rmtree(folder)
    os.makedirs(folder)
    logging.info("Запущено скачивание пакета из %s изображений", len(image_urls))
    for url in image_urls:
        download_one(url, folder, stats)


if __name__ == "__main__":
    setup_logging()
    stats_collector = DownloadStats()
    download_and_save_images(sources, stats_collector)
    logging.info(
        "Итог: total=%s success=%s error=%s total_bytes=%s total_time=%.3fs",
        stats_collector.total_images,
        stats_collector.success_images,
        stats_collector.error_images,
        stats_collector.total_bytes,
        stats_collector.total_time,
    )
    logging.debug("Подробная статистика: %s", stats_collector.per_file)
