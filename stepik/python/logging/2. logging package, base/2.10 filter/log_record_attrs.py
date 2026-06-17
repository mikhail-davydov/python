import logging
import sys


def info_filter(record: logging.LogRecord):
    # 1. Уровни логирования
    print(f"Номер уровня:    {record.levelno}")
    print(f"Имя уровня:      {record.levelname}")

    # 2. Информация о месте вызова
    print(f"Имя файла:       {record.filename}")
    print(f"Путь к файлу:    {record.pathname}")
    print(f"Имя модуля:      {record.module}")
    print(f"Имя функции:     {record.funcName}")
    print(f"Номер строки:    {record.lineno}")

    # 3. Информация о времени
    print(f"Время создания:  {record.created}")
    print(f"В миллисекундах: {record.msecs}")

    # 4. Информация о процессе/потоке
    print(f"ID процесса:     {record.process}")
    print(f"Имя процесса:    {record.processName}")
    print(f"ID потока:       {record.thread}")
    print(f"Имя потока:      {record.threadName}")

    # 5. Имя логгера, который зарегистрировал запись
    print(f"Имя регистратора: {record.name}")

    # 6. Информация об исключении (если есть)
    print(f"Информация об исключении: {record.exc_info}")
    print(f"Текст исключения:         {record.exc_text}")

    # 7. Относительное время (относительно загрузки модуля logging)
    print(f"Относительное время: {record.relativeCreated} мс")

    # 8. Информация о сообщении
    print(f"'Сырое' сообщение:        {record.msg}")
    print(f"Аргументы сообщения:      {record.args}")
    print(f"Сообщение c подстановкой: {record.getMessage()}")


stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_handler.addFilter(info_filter)

logging.basicConfig(level=logging.INFO,
                    handlers=[stream_handler])

logging.info("Просто пример сообщения с аргументом %d", 1)
