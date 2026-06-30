import csv
import os
import plotly.graph_objects as go
import shutil
import tempfile
import threading
from dataclasses import dataclass, field, InitVar
from datetime import datetime, timezone
from time import perf_counter


@dataclass
class Ticker:
    name: str
    data: list = field(init=False, default_factory=list)


@dataclass
class PriceNormalizer:
    folder_path: str
    max_threads: InitVar[int] = field(default=1)
    tickers: list[Ticker] = field(init=False, default_factory=list)

    def __post_init__(self, max_threads: int):
        self.semaphore = threading.Semaphore(max_threads)
        self.create_threads()

    def create_threads(self) -> None:
        threads = []

        for file in os.listdir(self.folder_path):
            file_path = f"{self.folder_path}/{file}"
            ticker_name = file.split(".")[0]
            thread = threading.Thread(target=self.update_ticker_data, args=(file_path, ticker_name))
            threads.append(thread)

        [thread.start() for thread in threads]
        [thread.join() for thread in threads]

    def update_ticker_data(self, file_path: str, ticker_name: str) -> None:
        with self.semaphore:
            with tempfile.NamedTemporaryFile("w", delete=False, suffix=".csv") as tmp:
                with open(file_path, "r", newline="", encoding="UTF-8") as src:
                    new_ticker = Ticker(ticker_name)
                    reader = csv.reader(src)
                    writer = csv.writer(tmp)

                    header = next(reader)
                    # в случае если в файл уже добавлена нормализованная цена
                    if len(header) > 2:
                        new_ticker.data = list(reader)
                        self.tickers.append(new_ticker)
                        return

                    header.append("normalize_price")
                    writer.writerow(header)

                    # нормализуем отдельно 1ю строку данных, для получения начальной цены
                    timestamp, initial_price = next(reader)
                    first_data_with_normalized_price_row = [timestamp, initial_price, "100.0"]
                    new_ticker.data.append(first_data_with_normalized_price_row)
                    writer.writerow(first_data_with_normalized_price_row)

                    for row in reader:
                        row_with_normalized_price = self.normalize_price(row, initial_price)
                        new_ticker.data.append(row_with_normalized_price)
                        writer.writerow(row_with_normalized_price)

                    self.tickers.append(new_ticker)
                tmp_path = tmp.name
            shutil.move(tmp_path, file_path)

    @staticmethod
    def normalize_price(row: list, initial_price: str) -> list:
        timestamp, price = row
        return [timestamp, price, str(float(price) * 100 / float(initial_price))]


@dataclass
class MultiTickerChart:
    tickers: list[Ticker]

    def __post_init__(self):
        self.fig = go.Figure()
        self.add_trace()
        self.update_layout()

    def add_trace(self) -> None:
        for ticker in self.tickers:
            x, y, hover_texts = [], [], []

            for time_stamp, _, normalize_price in ticker.data:
                dt = datetime.fromtimestamp(float(time_stamp), tz=timezone.utc)
                x.append(dt)
                y.append(float(normalize_price))
                hover_texts.append(dt.strftime("%d %b %Y"))

            self.fig.add_trace(
                go.Scatter(
                    x=x,
                    y=y,
                    mode="lines",
                    name=ticker.name,
                    text=hover_texts,
                    hovertemplate=(
                        "<b>%{fullData.name}</b><br>"
                        "Дата: %{text}<br>"
                        "Значение: %{y:.2f}<extra></extra>"
                    ),
                ),
            )

    def update_layout(self) -> None:
        self.fig.update_layout(
            title="График скорректированных цен",
            xaxis_title="Дата",
            yaxis_title="%",
            font=dict(color="#C9C9C9"),
            legend_title="Тикеры",
            paper_bgcolor="#1E1E1E",
            plot_bgcolor="#1E1E1E",
            hovermode="closest",
            xaxis=dict(linecolor="#929292"),
            yaxis=dict(linecolor="#929292"),
        )

        # Настройка оси X: только Jan и Jul
        self.fig.update_xaxes(
            tickformat="%b %Y",
            dtick="M6",  # каждые 6 месяцев
            tick0="2020-01-01",
            tickangle=0,
            showgrid=True,
            gridcolor="#929292",
            griddash="dot",
        )

        # Настройка оси Y
        self.fig.update_yaxes(
            showgrid=True,
            gridcolor="#929292",
            griddash="dot",
            zeroline=True,
            zerolinecolor="#B5B5B5",
            zerolinewidth=1,
        )

    def show(self):
        self.fig.show()


if __name__ == "__main__":
    start_time = perf_counter()

    path = "tickers_data"
    normalizer = PriceNormalizer(path, max_threads=1)
    chart = MultiTickerChart(normalizer.tickers)
    chart.show()

    print("Время выполнения: ", perf_counter() - start_time)
