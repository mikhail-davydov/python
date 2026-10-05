import asyncpg
import os
from asyncpg import Connection
from typing import Optional


async def timeout_connection(timeout: float) -> Optional[Connection]:
    """
    Пытается установить соединение с базой данных с заданным таймаутом
    Args:
        timeout: Максимальное время ожидания в секундах
    Returns:
        Объект Connection или None, если не удалось подключиться за отведенный таймаут
    """
    my_password = os.getenv('DB_PASSWORD', 'admin')
    try:
        return await asyncpg.connect(port=5434, user='postgres', password=my_password, database='demo', timeout=timeout)
    except TimeoutError:
        print('Timeout! Не удалось установить соединение за заданное время!')
        return None
