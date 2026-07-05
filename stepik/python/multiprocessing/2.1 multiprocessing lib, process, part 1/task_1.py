import multiprocessing


def task(): ...


def main():
    multiprocessing.Process(target=task).start()


if __name__ == '__main__':
    main()