from concurrent.futures import ProcessPoolExecutor
from logging import Logger
from multiprocessing import get_logger

import csv
import logging
import os
import pandas as pd
import plotly.graph_objects as go
from calendar import monthrange
from datetime import timedelta, date, datetime
from typing import Generator

TICKERS_FILE = "tickers.txt"
EXCHANGE_FOLDER = "exchange/"
NEW_EXCHANGE_FOLDER = "result_exchange/"
MONTHLY_PAYMENT = 10000
COUNT_TICKER = 5
START_DATE = date(year=2013, month=1, day=1)
END_DATE = date.today()


class FileResultCSV:
    """
    Класс записи результатов в файл .csv
    """

    def __init__(self, path: str) -> None:
        self.__path = path
        self.__file = None
        self.__writer = None
        self.__price = None
        self.__count_share = 0.0
        self.__share_price = None

    def init_csv_file(self) -> None:
        """
        Инициализация файла .csv

        :return: None
        """

        self.__file = open(self.__path, "w", encoding="utf-8-sig", newline="")
        self.__writer = csv.DictWriter(
            self.__file,
            fieldnames=["Date", "Count share", "Share price"],
            delimiter="\t",
        )
        self.__writer.writeheader()

    def write(self, date_: str) -> None:
        """
        Запись данных в файл

        :param date_: Строковая дата
        :return: None
        """

        self.__writer.writerow(
            {
                "Date": date_,
                "Count share": self.__count_share,
                "Share price": self.__share_price,
            },
        )

    @property
    def price(self) -> None | float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        self.__price = value

    @property
    def count_share(self) -> float:
        return self.__count_share

    @count_share.setter
    def count_share(self, value: float) -> None:
        self.__count_share = value

    @property
    def share_price(self) -> None | float:
        return self.__share_price

    @share_price.setter
    def share_price(self, value: float) -> None:
        self.__share_price = value

    def close_csv_file(self) -> None:
        self.__file.close()
        self.__file = None
        self.__writer = None
        self.__price = None
        self.__count_share = None
        self.__share_price = None


def setup_logging() -> Logger:
    """
    Задает настройки для логирования

    :return: Logger для логирования работы процессов
    """

    logger = get_logger()
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("execution_log_2.txt", mode="w")
    fh.setFormatter(
        logging.Formatter(
            fmt="{asctime} - {levelname} - {processName} - {message}", style="{",
        ),
    )
    logger.addHandler(fh)

    return logger


def make_directory(logger: Logger) -> None:
    """
    Создает директорию

    :param logger: Логирование работы процессов
    :return: None
    """

    os.makedirs(NEW_EXCHANGE_FOLDER, exist_ok=True)
    logger.info(f"Создание директории: {NEW_EXCHANGE_FOLDER}")


def get_ticker_to_file() -> Generator:
    """
    Открывает файл с тикерами. Читает построчно и получает тикер

    :return: Генератор с кортежами данных о путях к файлам и тикером
    """

    with open(TICKERS_FILE) as file:
        for row in file:
            ticker = row.strip()
            closed_prices = os.path.join(EXCHANGE_FOLDER, f"closed_prices_{ticker}.csv")
            dividend_payments = os.path.join(
                EXCHANGE_FOLDER, f"dividend_payments_{ticker}.csv",
            )
            yield closed_prices, dividend_payments, ticker


def get_information_files(closed_prices: str, dividend_payments: str) -> (dict, dict):
    """
    Открывает файлы и собирает информацию в словарь

    :param closed_prices: Путь к файлу с ценами закрытия
    :param dividend_payments: Путь к файлу с дивидендными выплатами
    :return: Кортеж из двух словарей данных из файлов
    """

    information_closed_prices = {}
    information_dividend_payments = {}

    with open(
            closed_prices, encoding="utf-8-sig", newline="",
    ) as closed_prices_file, open(
        dividend_payments, encoding="utf-8-sig", newline="",
    ) as dividend_payments_file:

        closed_prices_reader = csv.DictReader(closed_prices_file, delimiter="\t")
        dividend_payments_reader = csv.DictReader(
            dividend_payments_file, delimiter="\t",
        )

        for row in closed_prices_reader:
            information_closed_prices[row["Date"]] = row["Price"]

        for row in dividend_payments_reader:
            information_dividend_payments[row["Date"]] = row["Payments"]

    return information_closed_prices, information_dividend_payments


def check_month_day(year: int, month: int) -> int:
    """
    Вычисляет количество дней в месяце

    :param year: Год
    :param month: Месяц
    :return: Количество дней
    """

    return monthrange(year, month)[1]


def start_work_process(
        payment: float,
        start_date: date,
        end_date: date,
        closed_prices: str,
        dividend_payments: str,
        ticker: str,
        exchange_folder: str,
        logger: Logger,
) -> None:
    """
    Работа одного процесса по вычислению акций по 1-му тикеру

    :param payment: Ежемесечная плата на покупку акций
    :param start_date: Стартовая дата для формирования портфеля
    :param end_date: Конечная дата для формирования портфеля
    :param closed_prices: Путь к файлу с ценами закрытия
    :param dividend_payments: Путь к файлу с дивидендными выплатами
    :param ticker: Тикер, полученный с файла
    :param exchange_folder: Директория для новых файлов
    :param logger: Логирование работы процессов
    :return: None
    """

    # Инициализация работы с результирующим файлом
    path = os.path.join(exchange_folder, f"result_{ticker}.csv")
    writer = FileResultCSV(path)
    writer.init_csv_file()
    logger.info(f"Создание файла для записи результатов: {os.path.basename(path)}")

    # Получение данных
    information_closed_prices, information_dividend_payments = get_information_files(
        closed_prices, dividend_payments,
    )
    logger.info("Получение данных из файлов по ценам закрытия и дивидендным выплатам")

    # Вычисление количество дней
    days = (end_date - start_date).days

    # Накопительная сумма
    total = 0

    # Дата выплаты дивидендов и его цена за 1 акцию
    date_dividend = None
    price_dividend = None

    for day in range(days):
        # Вычисление количество дней в месяце
        current_day = check_month_day(start_date.year, start_date.month)

        # Начисление суммы каждый месяц
        if day % current_day == 0:
            total += payment
            logger.info(f"Начислена ежемесечная сумма для покупки акций: {payment}")

        date_string = start_date.strftime("%Y-%m-%d")
        start_date += timedelta(days=1)

        # Проверка даты выплаты дивидендов
        if date_string in information_dividend_payments:
            date_dividend = (
                    datetime.strptime(date_string, "%Y-%m-%d") + timedelta(days=8)
            ).strftime("%Y-%m-%d")
            price_dividend = float(information_dividend_payments[date_string])

        if date_string == date_dividend:
            total += writer.count_share * price_dividend
            logger.info(f"Дивиденды {ticker} выплачены в сумме: {price_dividend}")
            date_dividend = None
            price_dividend = None

        if date_string in information_closed_prices:
            price = float(information_closed_prices[date_string])
            writer.price = price
        elif writer.price is None:
            continue
        else:
            price = writer.price

        # Проверка накопительной суммы
        if total:
            writer.count_share += total / price
            total = 0

        # Подсчет цены акций
        writer.share_price = writer.count_share * price

        # Запись данных
        writer.write(date_string)

    # Закрытие результирующего файла
    writer.close_csv_file()
    logger.info(f"Закрытие файла: {os.path.basename(path)}")


def start_pool_processing(logger: Logger) -> None:
    """
    Запускает пул процессов для вычисления портфеля

    :param logger: Логирования работы процессов
    :return: None
    """

    with ProcessPoolExecutor() as executor:
        for closed_prices, dividend_payments, ticker in get_ticker_to_file():
            executor.submit(
                start_work_process,
                MONTHLY_PAYMENT / COUNT_TICKER,
                START_DATE,
                END_DATE,
                closed_prices,
                dividend_payments,
                ticker,
                NEW_EXCHANGE_FOLDER,
                logger,
            )


def get_information_file(filename: str, logger: Logger) -> pd.DataFrame:
    """
    Собирает датафрейм из данных файла

    :param filename: Файл с данными для постройки графика
    :param logger: Логирование работы процессов
    :return: Датафрейм из даты и цены акции
    """

    data = {"Date": [], "Share price": []}

    with open(filename, encoding="utf-8-sig", newline="") as read_csv:
        reader = csv.DictReader(read_csv, delimiter="\t")

        for row in reader:
            data["Date"].append(row["Date"])
            data["Share price"].append(float(row["Share price"]))

    df = pd.DataFrame(data)
    logger.info(
        f"Формирование датафрейма из данных файла: {os.path.basename(filename)}",
    )

    return df


def plotting_graph(logger: Logger) -> None:
    """
    Построение графика на основе полученных данных в файлах

    :param logger: Логирование работы процессов
    :return: None
    """

    fig = go.Figure()

    for file in os.listdir(NEW_EXCHANGE_FOLDER):
        filename = os.path.join(NEW_EXCHANGE_FOLDER, file)
        ticker = file[7:-4]
        df = get_information_file(filename, logger)

        # Добавление данных на график
        fig.add_trace(
            go.Scatter(
                x=df["Date"],
                y=df["Share price"],
                mode="lines",
                name=ticker,
            ),
        )

    # Обновление данных графика
    fig.update_layout(
        title="Портфель Жени",
        xaxis_title="Дата",
        yaxis_title="Стоимость акций",
        plot_bgcolor="black",
        paper_bgcolor="black",
        font=dict(color="white"),
    )

    logger.info("Построение графика на основе полученных данных в файлах")

    # Вывод графика
    fig.show()


def main() -> None:
    """
    Выполняет основную логику программы

    :return: None
    """

    logger = setup_logging()

    logger.info("Старт программы...")

    make_directory(logger)
    start_pool_processing(logger)

    plotting_graph(logger)

    logger.info("Завершение программы...")


if __name__ == "__main__":
    main()
