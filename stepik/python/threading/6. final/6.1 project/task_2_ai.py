"""
Задание 2: Нормализация цен и построение графиков.
Используется многопоточность без пула потоков.

Примечание: Для отображения графика используйте matplotlib или plotly.
При отсутствии библиотек сохраняется только CSV файл с нормализованными данными.
"""

import os
import csv
import threading
import time
from datetime import datetime
from queue import Queue, Empty

# Попытка импорта plotly, если нет - используем matplotlib
try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    USE_PLOTLY = True
except ImportError:
    USE_PLOTLY = False

try:
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    USE_MATPLOTLIB = True
except ImportError:
    USE_MATPLOTLIB = False


class NormalizerThread(threading.Thread):
    """Поток для нормализации цен в CSV файле."""
    
    def __init__(self, file_path: str, output_queue: Queue, semaphore: threading.Semaphore, ticker_filter: str = None):
        """
        Инициализация потока.
        
        :param file_path: путь к CSV файлу с исходными данными
        :param output_queue: очередь для передачи результатов
        :param semaphore: семафор для ограничения количества одновременных потоков
        :param ticker_filter: фильтр по тикеру (если None, обрабатываются все тикеры)
        """
        super().__init__()
        self.file_path = file_path
        self.output_queue = output_queue
        self.semaphore = semaphore
        self.ticker_filter = ticker_filter
        self.normalized_data = {}
        self.tickers = []
        self.error = None
    
    def run(self):
        """Основной метод потока - нормализует цены."""
        # Получаем разрешение от семафора
        self.semaphore.acquire()
        try:
            self._normalize_file()
        except Exception as e:
            self.error = str(e)
            print(f"[ERROR] Error processing {self.file_path}: {e}")
        finally:
            # Освобождаем семафор
            self.semaphore.release()
    
    def _normalize_file(self):
        """Выполняет нормализацию цен в файле."""
        # Группируем данные по тикерам
        ticker_prices = {}
        
        with open(self.file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ticker = row['ticker']
                if self.ticker_filter and ticker != self.ticker_filter:
                    continue
                    
                if ticker not in ticker_prices:
                    ticker_prices[ticker] = []
                
                price = float(row['adjusted_close'])
                ticker_prices[ticker].append({
                    'date': row['date'],
                    'price': price
                })
        
        # Нормализуем цены для каждого тикера
        for ticker, prices in ticker_prices.items():
            if not prices:
                continue
            
            first_price = prices[0]['price']
            normalized_records = []
            
            for record in prices:
                # Нормализованная цена: 100 * (текущая цена / базовая цена)
                normalized_price = 100.0 * (record['price'] / first_price)
                
                normalized_records.append({
                    'ticker': ticker,
                    'date': record['date'],
                    'original_price': record['price'],
                    'normalized_price': normalized_price
                })
            
            self.normalized_data[ticker] = normalized_records
            
            # Отправляем результат в очередь
            self.output_queue.put({
                'ticker': ticker,
                'data': normalized_records,
                'file_path': self.file_path
            })
            
            print(f"[OK] Normalized {len(normalized_records)} records for {ticker}")
        
        self.tickers = list(ticker_prices.keys())


def get_csv_files(directory: str) -> list:
    """Получает список всех CSV файлов в директории."""
    csv_files = []
    for filename in os.listdir(directory):
        if filename.startswith('stock_prices_') and filename.endswith('.csv'):
            csv_files.append(os.path.join(directory, filename))
    return sorted(csv_files)


def create_plotly_chart(data_by_ticker: dict):
    """Создает интерактивный график с использованием plotly."""
    # Создаем subplot для каждого тикера
    tickers = sorted(data_by_ticker.keys())
    n_tickers = len(tickers)
    
    # Создаем фигуру с subplot'ами
    fig = make_subplots(
        rows=n_tickers, 
        cols=1, 
        shared_xaxes=True,
        subplot_titles=[f"{ticker} (Normalized Price)" for ticker in tickers],
        vertical_spacing=0.03
    )
    
    # Цвета для графиков
    colors = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
    ]
    
    # Добавляем каждый график
    for i, ticker in enumerate(tickers, 1):
        data = data_by_ticker[ticker]
        dates = [d['date'] for d in data]
        prices = [d['normalized_price'] for d in data]
        
        fig.add_trace(
            go.Scatter(
                x=dates,
                y=prices,
                mode='lines',
                name=ticker,
                line=dict(color=colors[i-1], width=1.5),
                hovertemplate='<b>%{x}</b><br>Price: %{y:.2f}<extra></extra>'
            ),
            row=i, col=1
        )
        
        # Добавляем горизонтальную линию на уровне 100
        fig.add_hline(
            y=100, 
            line_dash="dash", 
            line_color="gray",
            row=i, 
            col=1
        )
        
        # Настраиваем ось Y
        fig.update_yaxes(
            title_text=ticker,
            row=i, 
            col=1,
            title_standoff=5,
            tickformat=".1f"
        )
    
    # Настраиваем общий заголовок
    fig.update_layout(
        height=800,
        title_text="Normalized Stock Prices (Base: 100)",
        showlegend=False,
        hovermode='x unified',
        margin=dict(t=50, b=30, l=50, r=50)
    )
    
    # Настраиваем ось X для нижнего графика
    fig.update_xaxes(
        title_text="Date",
        row=n_tickers, 
        col=1
    )
    
    # Сохраняем и показываем
    output_file = "normalized_stock_prices.html"
    fig.write_html(output_file, include_plotlyjs='cdn')
    print(f"\n[OK] Interactive chart saved to: {output_file}")
    print("[INFO] Open the HTML file in a browser to view the interactive chart.")


def create_matplotlib_chart(data_by_ticker: dict):
    """Создает график с использованием matplotlib."""
    # Подготовка данных
    tickers = sorted(data_by_ticker.keys())
    n_tickers = len(tickers)
    
    # Создаем фигуру с subplot'ами
    fig, axes = plt.subplots(n_tickers, 1, figsize=(12, 3 * n_tickers))
    
    if n_tickers == 1:
        axes = [axes]
    
    colors = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
    ]
    
    # Графики для каждого тикера
    for i, (ticker, ax) in enumerate(zip(tickers, axes)):
        data = data_by_ticker[ticker]
        dates = [datetime.strptime(d['date'], '%Y-%m-%d') for d in data]
        prices = [d['normalized_price'] for d in data]
        
        ax.plot(dates, prices, color=colors[i], linewidth=1.5, label=ticker)
        ax.axhline(y=100, color='gray', linestyle='--', alpha=0.7, linewidth=1)
        
        ax.set_ylabel(f'{ticker}\nNormalized Price')
        ax.legend(loc='upper left')
        ax.grid(True, alpha=0.3)
        ax.fmt_xdate = mdates.DateFormatter('%Y-%m')
        
        # Форматирование дат на оси X
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # Общий заголовок
    fig.suptitle('Normalized Stock Prices (Base: 100)', fontsize=14, fontweight='bold')
    
    # Подписи оси X для нижнего графика
    axes[-1].set_xlabel('Date')
    
    plt.tight_layout()
    
    # Сохраняем
    output_file = "normalized_stock_prices.png"
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"\n[OK] Chart saved to: {output_file}")
    print("[INFO] Open the PNG file to view the chart.")
    
    # Показываем
    plt.show()


def main():
    """Главная функция."""
    start_time = time.time()
    
    # Директория с CSV файлами
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_files = get_csv_files(script_dir)
    
    if not csv_files:
        print("[ERROR] No CSV files found!")
        return
    
    print(f"[INFO] Found {len(csv_files)} CSV file(s)")
    
    # Ограничение количества одновременных потоков
    max_threads = 3
    semaphore = threading.Semaphore(max_threads)
    
    # Очередь для результатов
    output_queue = Queue()
    
    # Создаем и запускаем потоки - для каждого тикера свой поток
    threads = []
    
    # Читаем тикеры из CSV файлов
    all_tickers = set()
    for file_path in csv_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_tickers.add(row['ticker'])
    
    all_tickers = sorted(all_tickers)
    print(f"[INFO] Found {len(all_tickers)} unique tickers: {', '.join(all_tickers)}")
    
    # Создаем потоки для каждого тикера
    for ticker in all_tickers:
        for file_path in csv_files:
            thread = NormalizerThread(file_path, output_queue, semaphore, ticker)
            threads.append(thread)
            thread.start()
    
    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()
    
    # Собираем данные из очереди
    data_by_ticker = {}
    error_count = 0
    
    while True:
        try:
            result = output_queue.get_nowait()
            if result['ticker'] and result['data']:
                data_by_ticker[result['ticker']] = result['data']
        except Empty:
            break
    
    if not data_by_ticker:
        print("[ERROR] No data was processed!")
        return
    
    elapsed_time = time.time() - start_time
    print(f"\n[INFO] Processing completed in {elapsed_time:.2f} seconds")
    print(f"[INFO] Normalized data for {len(data_by_ticker)} tickers")
    
    # Строим график
    print("\n[INFO] Creating chart...")
    
    if not data_by_ticker:
        print("[ERROR] No data was processed!")
        return
    
    # Сохраняем нормализованные данные в отдельный файл
    output_normalized_file = os.path.join(script_dir, "normalized_stock_prices.csv")
    with open(output_normalized_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['ticker', 'date', 'original_price', 'normalized_price'])
        writer.writeheader()
        
        for ticker in sorted(data_by_ticker.keys()):
            for record in data_by_ticker[ticker]:
                writer.writerow(record)
    
    print(f"[OK] Normalized data saved to: {output_normalized_file}")
    
    if USE_PLOTLY:
        create_plotly_chart(data_by_ticker)
    elif USE_MATPLOTLIB:
        create_matplotlib_chart(data_by_ticker)
    else:
        print("\n[INFO] Plotting libraries not available.")
        print("[INFO] Install matplotlib or plotly to generate charts.")
        print("[INFO] Normalized CSV file has been created successfully.")
    
    # Отчет по обработке
    print("\n=== Processing Report ===")
    for ticker in sorted(data_by_ticker.keys()):
        data = data_by_ticker[ticker]
        first_price = data[0]['original_price']
        last_price = data[-1]['original_price']
        first_norm = data[0]['normalized_price']
        last_norm = data[-1]['normalized_price']
        
        print(f"\n{ticker}:")
        print(f"  First price: {first_price:.2f} -> Normalized: {first_norm:.2f}")
        print(f"  Last price:  {last_price:.2f} -> Normalized: {last_norm:.2f}")
        print(f"  Change: {last_norm - first_norm:+.2f}%")


if __name__ == "__main__":
    main()
