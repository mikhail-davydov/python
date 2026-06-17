from logging import handlers, config
from zipfile import ZipFile

import logging
import os
import yaml
from functools import partial

BACKUP_DIR = 'logs/backups'
os.makedirs(BACKUP_DIR, exist_ok=True)


def zip_namer(name, dir_backup) -> str:
    # RotatingFileHandler вызывает namer с именем файла после ротации
    # Например: 'logs/app.log.1' -> нужно вернуть 'logs/backups/app.1.zip'

    base = os.path.basename(name)  # 'app.log.1'

    # Разбиваем на части
    parts = base.split('.')  # ['app', 'log', '1']

    if len(parts) >= 3:
        # Имя без расширения (.log) и суффикс ротации
        name_part = parts[0]  # 'app'
        suffix = parts[-1]  # '1'

        return os.path.join(dir_backup, f"{name_part}.{suffix}.zip")

    return os.path.join(dir_backup, f"{base}.zip")


def zip_rotator(source, dest):
    # source - исходный файл лога (logs/app.log.1)
    # dest - результат вызова namer, уже готовый путь к архиву
    # dest будет вида 'logs/backups/app.1.zip'

    # Просто используем dest как путь к архиву
    archive_path = dest

    with ZipFile(archive_path, 'w') as myzip:
        myzip.write(source, arcname=os.path.basename(source))
    os.remove(source)


def file_rotating_handler_factory(dir_backup=BACKUP_DIR, namer_func=None, rotator_func=None, **kwargs):
    handler = logging.handlers.RotatingFileHandler(**kwargs)
    if namer_func:
        namer_func = partial(namer_func, dir_backup=dir_backup)
        handler.namer = namer_func
    if rotator_func:
        handler.rotator = rotator_func
    return handler


with open("task_6.yaml", 'r', encoding='utf-8') as f:
    dict_config = yaml.safe_load(f)

logging.config.dictConfig(dict_config)


# alt

from functools import partial
import logging.config
import logging.handlers
import zipfile
import os
import yaml


def zip_rotator(source: str, dest: str) -> None:
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        arcname = os.path.basename(source)
        zip_file.write(source, arcname=arcname)
    os.remove(source)


def zip_namer(default_name: str, backup_dir: str) -> str:
    base_name = os.path.basename(default_name)
    name, ext, suffix = base_name.rsplit(".", 2)
    archive_name = f"{name}.{suffix}.zip"
    return os.path.join(backup_dir, archive_name)


def file_rotating_handler_factory(namer_func=None, rotator_func=None, dir_backup="", **kwargs):
    filename = kwargs.pop('filename')
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    os.makedirs(dir_backup, exist_ok=True)

    handler = logging.handlers.RotatingFileHandler(filename=filename, **kwargs)
    if namer_func is not None:
        handler.namer = partial(namer_func, backup_dir=dir_backup)
    if rotator_func is not None:
        handler.rotator = rotator_func
    return handler


with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

logging.config.dictConfig(config)