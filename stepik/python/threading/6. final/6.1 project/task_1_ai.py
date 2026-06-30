"""
Параллельное получение исторических данных цен по тикерам с Yahoo Finance
и сохранение в CSV файл с использованием пула потоков.
"""

import os
import requests
import json
import csv
import time
import sys
import io
from datetime import datetime, timezone
from typing import Generator
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue
import threading


# Установка UTF-8 кодировки для консоли Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# Константы для API
USER_AGENT_KEY = "User-Agent"
USER_AGENT_VALUE = "Mozilla/5.0"
HEADERS = {USER_AGENT_KEY: USER_AGENT_VALUE}

# Список тикеров для запроса
TICKERS = ["AAPL", "MSFT", "AMZN", "NVDA", "TSLA", "GOOGL", "META", "BRK-B", "UNH", "JPM"]

# Параметры запроса
START_DATE = "01.01.20"
END_DATE = "30.06.26"
INTERVAL = "1wk"


def get_ticker(file: str) -> Generator[str, None, None]:
    """Читает тикеры из файла, по одному на строку."""
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            ticker = line.strip()
            if ticker:
                yield ticker


def get_history_data(ticker: str, start_date: str, end_date: str, interval: str = "1wk") -> dict:
    """
    Получает исторические данные для указанного тикера актива.

    :param ticker: str, тикер актива.
    :param start_date: str, дата начала периода в формате 'дд.мм.гг'.
    :param end_date: str, дата окончания периода в формате 'дд.мм.гг'.
    :param interval: str, интервал времени (неделя, день и т.д.) (необязательный, по умолчанию '1wk').
    :return: dict, данные в формате JSON.
    """
    per2 = int(datetime.strptime(end_date, '%d.%m.%y').replace(tzinfo=timezone.utc).timestamp())
    per1 = int(datetime.strptime(start_date, '%d.%m.%y').replace(tzinfo=timezone.utc).timestamp())
    params = {
        "period1": str(per1),
        "period2": str(per2),
        "interval": interval,
        "includeAdjustedClose": "true"
    }
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    
    try:
        response = requests.get(url, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Ошибка при запросе для {ticker}: {e}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Ошибка при парсинге JSON для {ticker}: {e}")
        return {}


def process_ticker(ticker: str, start_date: str, end_date: str, interval: str) -> dict:
    """
    Обертка для получения данных по тикеру с обработкой ошибок.
    
    :param ticker: тикер актива
    :param start_date: дата начала
    :param end_date: дата окончания
    :param interval: интервал
    :return: результат запроса
    """
    data = get_history_data(ticker, start_date, end_date, interval)
    return {"ticker": ticker, "data": data}


def extract_prices_from_data(data: dict, ticker: str) -> list:
    """
    Извлекает цены из данных Yahoo Finance.
    
    :param data: словарь с данными от API
    :param ticker: тикер актива
    :return: список записей для CSV
    """
    results = []
    
    if not data or "chart" not in data or not data["chart"]["result"]:
        return results
    
    result = data["chart"]["result"][0]
    timestamp = result.get("timestamp", [])
    indicators = result.get("indicators", {})
    adjusted_close_data = indicators.get("adjclose", [{}])[0].get("adjclose", [])
    
    # Парсим даты и цены
    for i, ts in enumerate(timestamp):
        date = datetime.fromtimestamp(ts, tz=timezone.utc).strftime('%Y-%m-%d')
        adj_close = adjusted_close_data[i] if i < len(adjusted_close_data) else None
        
        if adj_close is not None:
            results.append({
                "ticker": ticker,
                "date": date,
                "adjusted_close": adj_close
            })
    
    return results


def writer_thread(queue: Queue, filename: str):
    """
    Поток-писатель, который читает из очереди и записывает в CSV файл.
    
    :param queue: очередь с данными
    :param filename: имя CSV файла
    """
    file_written = False
    
    while True:
        item = queue.get()
        
        if item is None:  # Сигнал о завершении
            break
        
        ticker = item["ticker"]
        data = item["data"]
        prices = extract_prices_from_data(data, ticker)
        
        # Запись в CSV
        if prices:
            with open(filename, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=["ticker", "date", "adjusted_close"])
                if not file_written:
                    writer.writeheader()
                    file_written = True
                writer.writerows(prices)
            
            print(f"[OK] Saved {len(prices)} records for {ticker}")
    
    print("Writer thread finished")


def main():
    """Главная функция, управляющая потоками."""
    start_time = time.time()
    
    # Имя CSV файла (в той же директории, что и скрипт)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, f"stock_prices_{START_DATE}_{END_DATE}.csv")
    
    # Очищаем файл перед началом
    with open(output_file, 'w', encoding='utf-8') as f:
        pass
    
    # Создаем потокобезопасную очередь
    data_queue = Queue()
    
    # Запускаем поток записи
    writer = threading.Thread(target=writer_thread, args=(data_queue, output_file))
    writer.start()
    
    # Создаем пул потоков для запросов
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Запускаем задачи для каждого тикера
        futures = []
        for ticker in TICKERS:
            future = executor.submit(
                process_ticker, 
                ticker, 
                START_DATE, 
                END_DATE, 
                INTERVAL
            )
            futures.append(future)
        
        # Добавляем результаты в очередь
        for future in as_completed(futures):
            result = future.result()
            data_queue.put(result)
    
    # Сигнализируем потоку записи о завершении
    data_queue.put(None)
    
    # Ждем завершения потока записи
    writer.join()
    
    elapsed_time = time.time() - start_time
    print("\nProcessing completed in {:.2f} seconds".format(elapsed_time))
    print("Data saved to file: {}".format(output_file))


if __name__ == "__main__":
    main()
