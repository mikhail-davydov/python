from zipfile import ZipFile

import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = 'logs'
BACKUP_DIR = 'logs/backups'

os.makedirs(BACKUP_DIR, exist_ok=True)


def file_suffix(name) -> str:
    # RotatingFileHandler вызывает namer с именем файла после ротации
    # Например: 'logs/app.log.1' -> нужно вернуть 'logs/backups/app.1.zip'

    base = os.path.basename(name)  # 'app.log.1'

    # Разбиваем на части
    parts = base.split('.')  # ['app', 'log', '1']

    if len(parts) >= 3:
        # Имя без расширения (.log) и суффикс ротации
        name_part = parts[0]  # 'app'
        suffix = parts[-1]    # '1'

        return os.path.join(BACKUP_DIR, f"{name_part}.{suffix}.zip")

    return os.path.join(BACKUP_DIR, f"{base}.zip")


def file_rotator(source, dest):
    # source - исходный файл лога (logs/app.log.1)
    # dest - результат вызова namer, уже готовый путь к архиву
    # dest будет вида 'logs/backups/app.1.zip'

    # Просто используем dest как путь к архиву
    archive_path = dest

    with ZipFile(archive_path, 'w') as myzip:
        myzip.write(source, arcname=os.path.basename(source))
    os.remove(source)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    filename=f'{LOG_DIR}/app.log',
    encoding='utf-8',
    maxBytes=200,
    backupCount=2
)
formatter = logging.Formatter(
    fmt='[%(name)-5s] - [%(levelname)-8s] - %(message)s'
)
handler.setFormatter(formatter)
handler.namer = file_suffix
handler.rotator = file_rotator

logger.addHandler(handler)

# alt

import logging
from logging.handlers import RotatingFileHandler
import zipfile
import os

LOG_DIR = "logs"
BACKUP_DIR = os.path.join(LOG_DIR, "backups")
LOG_FILE = os.path.join(LOG_DIR, "app.log")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)

def zip_rotator(source, dest) -> None:
    with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        arcname = os.path.basename(source)
        zip_file.write(source, arcname=arcname)
    os.remove(source)

def zip_namer(default_name) -> str:
    base_name = os.path.basename(default_name)
    name, ext, suffix = base_name.rsplit(".", 2)
    new_filename = f"{name}.{suffix}.zip"
    return os.path.join(BACKUP_DIR, new_filename)

handler = RotatingFileHandler(LOG_FILE, maxBytes=200, backupCount=2, encoding="utf-8")
formatter = logging.Formatter("[%(name)-5s] - [%(levelname)-8s] - %(message)s")
handler.setFormatter(formatter)
handler.namer = zip_namer
handler.rotator = zip_rotator

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)