import concurrent.futures
import os
import pandas as pd
import queue
import requests
import threading
from datetime import datetime, timezone
from typing import List, Generator


def make_tickers_file(tickers: List, file: str = 'tickers.txt') -> None:
    """Создаем файл с тикерами"""

    with open(file, 'w') as f:
        f.writelines(ticker + '\n' for ticker in tickers)


def get_ticker(file: str = 'tickers.txt') -> Generator[str, None, None]:
    """Генератор тикеров"""

    with open(file) as file:
        for line in file:
            ticker = line.strip()
            yield ticker


def get_history_data(ticker: str, start_date: str, end_date: str, interval: str = "1wk") -> pd.DataFrame:
    """
    Получает исторические данные для указанного тикера актива.

    :param ticker: str, тикер актива.
    :param start_date: str, дата начала периода в формате 'дд.мм.гг'.
    :param end_date: str, дата окончания периода в формате 'дд.мм.гг'.
    :param interval: str, интервал времени (неделя, день и т.д.) (необязательный, по умолчанию '1wk' - одна неделя).
    :return: DataFrame с историческими данными.
     'high', 'open', 'close', 'volume', 'low', 'adjclose'
    """

    per2 = int(datetime.strptime(end_date, '%d.%m.%y').replace(tzinfo=timezone.utc).timestamp())
    per1 = int(datetime.strptime(start_date, '%d.%m.%y').replace(tzinfo=timezone.utc).timestamp())
    params = {
        "period1": str(per1), "period2": str(per2),
        "interval": interval, "includeAdjustedClose": "true",
    }
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    user_agent_key = "User-Agent"
    user_agent_value = "Mozilla/5.0"
    headers = {user_agent_key: user_agent_value}

    history_data = requests.get(url, headers=headers, params=params).json()

    data = history_data['chart']['result'][0]['indicators']['quote'][0]
    data['adjclose'] = history_data['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
    data = pd.DataFrame(data,
                        index=history_data['chart']['result'][0]['timestamp'],
                        )
    return data


def file_writer(end_data: str, dir_file: str = 'tickers') -> None:
    """Функция-поток для записи файлов из очереди на диск."""

    while True:
        data, ticker = file_queue.get()
        end_data = end_data.replace('.', '-')
        filename = f'{ticker.lower()}_{end_data}.csv'
        os.makedirs(dir_file, exist_ok=True)
        data['date'] = data.index
        data.to_csv(os.path.join(dir_file, filename), index=False)
        print(f'{filename} was saved successfully')
        file_queue.task_done()


def put_task_to_queue_to_save(future, ticker: str) -> None:
    """Добавляем задачу в очередь на запись"""
    data = future.result()
    file_queue.put((data, ticker))


# Указываем временной промежуток
start_data = '01.01.20'
end_data = '12.12.23'

# Создаем файл с тикерами
make_tickers_file(['IBM', 'MCD', 'AAPL', 'MSFT', 'AMZN', 'NVDA', 'TSLA', 'GOOGL', 'META', 'BRK-B', 'UNH', 'JPM'])

# Создаем очередь для сохранения данных для записи
file_queue = queue.Queue()

# Создаем поток для записи файлов на диск
saver = threading.Thread(target=file_writer, args=(end_data,))
saver.daemon = True
saver.start()

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = dict((executor.submit(get_history_data, ticker, start_data, end_data, '1wk'), ticker)
                   for ticker in get_ticker(),
                   )
    done, not_done = concurrent.futures.wait(futures)

    for future in done:
        put_task_to_queue_to_save(future, ticker=futures[future])
    for future in not_done:
        exception = future.exception()
        if exception is not None:
            print(f'An error occurred during downloading: {exception}')
            print()

    # Ожидаем завершения всех задач в очереди перед выходом из программы
    file_queue.join()
