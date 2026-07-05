import multiprocessing


def handler(file: str) -> None:
    """
    Функция обработки платежей
    """
    ...


sources = ["2023_08.csv", "2023_07.csv", "2023_06.csv", "2023_05.csv", "2023_04.csv"]


def main():
    [multiprocessing.Process(target=handler, args=[source]).start() for source in sources]


if __name__ == '__main__':
    main()
