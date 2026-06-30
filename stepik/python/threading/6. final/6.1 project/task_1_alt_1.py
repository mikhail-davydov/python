import concurrent.futures
import csv
import os
import queue
import requests
import threading
from dataclasses import dataclass, fields
from datetime import datetime, timezone
from enum import Enum


class TimeIntervals(Enum):
    MONTH = "1mo"
    DAY = "1d"
    WEEK = "1wk"


@dataclass
class PriceData:
    date: str
    open: float
    close: float
    volume: float
    high: float
    low: float
    adjust_close: float


class Ticker:
    def __init__(self, name: str, prices: list[PriceData]):
        self.name = name
        self.prices = prices

    @staticmethod
    def from_yahoo_resonse(name: str, response: requests.Response):
        obj = response.json()
        timestamps = obj['chart']['result'][0]['timestamp']
        prices_open = obj['chart']['result'][0]['indicators']['quote'][0]['open']
        prices_close = obj['chart']['result'][0]['indicators']['quote'][0]['close']
        prices_volume = obj['chart']['result'][0]['indicators']['quote'][0]['volume']
        prices_high = obj['chart']['result'][0]['indicators']['quote'][0]['high']
        prices_low = obj['chart']['result'][0]['indicators']['quote'][0]['low']
        prices_adjust_close = obj['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
        prices = [PriceData(Utils.unix_to_date(ts), po, pc, pv, ph, pl, pac)
                  for ts, po, pc, pv, ph, pl, pac
                  in zip(timestamps, prices_open,
                         prices_close, prices_volume,
                         prices_high, prices_low,
                         prices_adjust_close,
                         )]
        return Ticker(name, prices)


class TickerDataProvider:
    _USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    _API = 'https://query2.finance.yahoo.com'

    def __init__(self, start_date: datetime, end_date: datetime,
                 inteval: TimeIntervals, max_workers: int = None,
                 ):
        self.start_date = start_date
        self.end_date = end_date
        self.interval = inteval
        self._get_cookie()
        self._ticker_queue = queue.Queue()
        self._pool = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers,
                                                           thread_name_prefix='ticker_provider_pool',
                                                           )
        self._running_futures = set()

    @property
    def is_proccessing(self) -> bool:
        return len(self._running_futures) > 0

    def _get_cookie(self):
        response = requests.get('https://fc.yahoo.com',
                                headers={'User-Agent': self._USER_AGENT},
                                timeout=10,
                                )

        self._cookie = response.headers['set-cookie']

    def _get_ticker_names(self, ticker_names_file_path: str):
        with open(ticker_names_file_path) as file:
            for line in file.readlines():
                yield line.strip()

    def _get_ticker(self, ticker_name: str):
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker_name}"
        period1 = Utils.date_to_unix(self.start_date)
        period2 = Utils.date_to_unix(self.end_date)
        params = {
            "period1": period1,
            "period2": period2,
            "interval": self.interval.value,
            "includeAdjustedClose": "true",
        }
        headers = {
            'User-Agent': self._USER_AGENT,
            'cookie': self._cookie,
        }
        response = requests.get(url, params=params, headers=headers, timeout=10)
        print(f'future for {ticker_name} completed')
        return Ticker.from_yahoo_resonse(ticker_name, response)

    def _handle_future(self, future: concurrent.futures.Future):
        while not future.done():
            try:
                result = future.result()
                self._ticker_queue.put(result)
                return
            except Exception as err:
                print(f'An error occurred during getting prices: {str(err)}')
                return
            finally:
                self._running_futures.remove(future)

    def get_tickers(self, ticker_names_file_path: str):
        for t_name in self._get_ticker_names(ticker_names_file_path):
            future = self._pool.submit(self._get_ticker, t_name)
            threading.Thread(name=f"future_for_{t_name}_handler",
                             target=self._handle_future, args=[future], daemon=True,
                             ).start()
            self._running_futures.add(future)
            print(f'added future for {t_name}')


class TickersToCsvSerializer:
    def __init__(self, provider: TickerDataProvider, ticker_names_file_path: str, output_csv_path: str = ""):
        self._provider = provider
        self.input_file = ticker_names_file_path
        self.output_path = output_csv_path
        self._writer_thread = threading.Thread(name='TickersToCsvSerializer_thread', target=self._tickers_to_csv)
        self._futures = []

    def _tiker_to_csv(self, ticker: Ticker):
        if len(ticker.prices) == 0:
            print(f"Warning! No valid data in ticker {ticker.name}. Csv file wasn't created")
            return
        file_path = os.path.join(self.output_path, f'{ticker.name}.csv')
        with open(file_path, 'w', newline='') as csv_file:
            field_names = list(ticker.prices[0].__dataclass_fields__.keys())
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            for price in ticker.prices:
                fields(price)
                writer.writerow(Utils.dataclass_to_dict(price))
            print(f"Csv file was created from ticker {ticker.name} data")

    def _tickers_to_csv(self):
        _queue = self._provider._ticker_queue
        while True:
            if not self._provider.is_proccessing and _queue.empty():
                return
            try:
                ticker = self._provider._ticker_queue.get(timeout=10)
                self._tiker_to_csv(ticker)
            except queue.Empty:
                print(f'{threading.current_thread().name} stopped by timeout')
                return
            except Exception as err:
                print(f'{threading.current_thread().name} got an exception: {err}')

    def start(self):
        self._provider.get_tickers(self.input_file)
        self._writer_thread.start()
        self._writer_thread.join()


class Utils:
    @staticmethod
    def date_to_unix(date: datetime):
        return str(int(date.replace(tzinfo=timezone.utc).timestamp()))

    @staticmethod
    def unix_to_date(timestamp: int):
        return datetime.fromtimestamp(timestamp).strftime('%d.%m.%Y')

    @staticmethod
    def dataclass_to_dict(dataclass):
        return {v.name: getattr(dataclass, v.name) for v in fields(dataclass)}


provider = TickerDataProvider(datetime.strptime('01.01.2020', '%d.%m.%Y'), datetime.now(), TimeIntervals.MONTH)
serializer = TickersToCsvSerializer(provider, "tickers.txt")
serializer.start()
