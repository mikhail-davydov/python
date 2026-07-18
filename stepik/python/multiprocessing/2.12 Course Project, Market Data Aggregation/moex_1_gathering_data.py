from concurrent.futures import ThreadPoolExecutor
from multiprocessing import current_process

import csv
import logging
import os
import queue
import requests
import time
from collections.abc import Callable
from datetime import datetime, timedelta
from functools import wraps

# Ужасно не люблю банковские задачи....
q = queue.Queue()


def set_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    file_info_handler = logging.FileHandler("log_info.txt", "a", encoding="utf-8")
    file_err_handler = logging.FileHandler("log_errors.txt", "a", encoding="utf-8")
    formatter = logging.Formatter("\n\n{processName}, {threadName}, {levelname},  {asctime}, {message}", style="{")
    file_info_handler.setLevel(logging.INFO)
    file_info_handler.addFilter(lambda record: record.levelno <= logging.WARNING)
    file_info_handler.setFormatter(formatter)
    file_err_handler.setLevel(logging.ERROR)
    file_err_handler.setFormatter(formatter)

    logger.addHandler(file_info_handler)
    logger.addHandler(file_err_handler)
    return logger


def logged(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = set_logger(current_process().name)
        try:
            beg = time.perf_counter()  # время начала процедуры
            res = func(*args, **kwargs)
            logger.info(f"\n{func.__name__} для {args} \t за {round(time.perf_counter() - beg, 2)} сек")
            return res
        except Exception as e:
            logger.error(f"{func.__name__}, {e}")

    return wrapper


@logged
def get_dates(ticker: str):
    """
    Получает диапозон доступных дат истории котировок компании
    """
    url = f"http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{ticker}/dates.json"
    user_agent_key = "User-Agent"
    user_agent_value = "Mozilla/5.0"
    headers = {user_agent_key: user_agent_value}
    try:
        response = requests.get(url, headers=headers)
    except Exception as err:
        return str(err)
    else:
        return (datetime.strptime(i, '%Y-%m-%d').date() for i in response.json()['dates']['data'][0])


@logged
def get_history_data(ticker: str, start_date: str):
    """
    Получает исторические данные для указанного тикера.
    """
    params = {"from": start_date}
    url = f"http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{ticker}.json"
    user_agent_key = "User-Agent"
    user_agent_value = "Mozilla/5.0"
    headers = {user_agent_key: user_agent_value}
    try:
        response = requests.get(url, headers=headers, params=params)
    except Exception as err:
        return str(err)
    else:
        resp = response.json()
        return (ticker, [{"TRADEDATE": datetime.strptime(i[1], '%Y-%m-%d').date(), "CLOSE": i[11]} for i in
                         resp["history"]["data"]],
        )


@logged
def get_history_dividents(ticker: str):  # , end_date: str):
    """
    Получает  данные по дивидентам для указанного тикера.
    """
    url = f'https://iss.moex.com/iss/securities/{ticker}/dividends.json'
    user_agent_key = "User-Agent"
    user_agent_value = "Mozilla/5.0"
    headers = {user_agent_key: user_agent_value}
    try:
        response = requests.get(url, headers=headers)
    except Exception as err:
        return str(err)
    else:
        resp = response.json()
        return (ticker + "_DIV", [{"closedate": datetime.strptime(i[2], '%Y-%m-%d').date(), "value": i[3]} for i in
                                  resp["dividends"]["data"]],
        )


@logged
def handle_task_done(future):
    """Функция-обработчик на завершение задачи.
    Добавляет данные из инета в очередь
    """
    exception = future.exception()
    if exception is not None:
        return f'An error occurred during downloading: {exception}'
    elif type(future.result()) == tuple:
        q.put(future.result())


if __name__ == "__main__":
    st = time.perf_counter()
    tiks = ["VTBR", "MBNK", "SBER", "OZON", "MGNT", "AFLT", "YDEX"]

    save_dir = "./MARKET"
    os.makedirs(save_dir, exist_ok=True)

    with ThreadPoolExecutor() as ex:
        for ticker in tiks:
            from_d, till_d = get_dates(ticker)
            print(f"{ticker}: from {from_d} till {till_d}", end="\t")
            days = (till_d - from_d).days
            # всего записей по тиккеру
            print(f"{days=}")

            # данные по дивидентам тиккера
            ex.submit(get_history_dividents, ticker).add_done_callback(handle_task_done)

            # ист. данные за весь доступные период
            while from_d < till_d:
                ex.submit(get_history_data, ticker, from_d.strftime('%Y-%m-%d')).add_done_callback(handle_task_done)

                from_d = from_d + timedelta(days=100)

    '''формируем словарь из очереди.
Формат: {"SBER": [{"TRADEDATE":date, "CLOSE":float}, ...],
                    "SBER_DIV": [{["closedate":date, "value": float]}, ... ],
                    "VTBR": [.....],
                    ....}    
            Я бы назвала колонки одинаково и в исторических данных и в дивидентах, но вдруг заказчику существенно оригинальное звучание..
            
         Сортируем данные по дате 
    '''
    hist_data = dict()
    while not q.empty():
        tic_nm, tic_data = q.get()
        hist_data[tic_nm] = hist_data.get(tic_nm, []) + tic_data

    for i in hist_data:
        col = "closedate" if "DIV" in i else "TRADEDATE"
        hist_data[i] = sorted(hist_data[i], key=lambda x: x[col])

        # Разбираем словарь на файлы
    for i in hist_data:
        columns = ["closedate", "value"] if "DIV" in i else ["TRADEDATE", "CLOSE"]

        file_path = os.path.join(save_dir, i + ".csv")
        with open(file_path, 'w') as f:
            fl = csv.DictWriter(f, columns)
            fl.writeheader()
            fl.writerows(hist_data[i])

    print(time.perf_counter() - st, '\n\n')

'''Запрос ист. данных одного тиккера последовательно - 5..9 сек
    Одного параллельно в потоках - 2 сек
    7 тик - 5..9 sec'''
