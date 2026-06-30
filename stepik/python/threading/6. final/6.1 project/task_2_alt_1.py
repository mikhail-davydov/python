import os
import pandas as pd
import plotly.graph_objs as go
from threading import Thread, Semaphore


# Класс для нормализации одного файла
class NormalizeThread(Thread):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def run(self):
        with semaphore:
            ticker = os.path.splitext(self.filename)[0]  # Имя тикера
            filepath = os.path.join(input_folder, self.filename)  # Путь к файлу

            df = pd.read_csv(filepath)
            df['Normalized'] = df['AdjClose'] / df['AdjClose'].iloc[0] * 100  # Нормализация
            normalize_date[ticker] = df[['Date', 'Normalized']]
            df.to_csv(filepath, index=False)
            print(f'Тикер {ticker} нормализован')


input_folder = 'data_tickers'
max_workers = 4
semaphore = Semaphore(max_workers)  # Семафор
normalize_date = {}  # Словарь для хранения нормализованных данных

# Создание и запуск потоков
threads = []
for file in os.listdir(input_folder):
    thread = NormalizeThread(file)
    thread.start()
    threads.append(thread)

# Ждём завершения всех потоков
for thread in threads:
    thread.join()

# Построение графика
fig = go.Figure()
for ticker, df in normalize_date.items():
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Normalized'], mode='lines', name=ticker))

fig.update_layout(title='Сравнение нормализованных цен акций',
                  xaxis_title='Дата',
                  yaxis_title='Нормализованная цена',
                  template='plotly_dark',
                  )

fig.show()
