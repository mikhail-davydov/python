import threading
import time
import yappi


def task_a():
    time.sleep(0.3)


def task_b():
    time.sleep(0.2)
    task_a()


# 1. Настраиваем тип часов и запускаем профилирование
yappi.set_clock_type("wall")

# builtins=False отключает профилирование встроенных функций (меньше мусора в выводе)
yappi.start(builtins=False)

# 2. Запускаем потоки
t1 = threading.Thread(target=task_a, name='Worker-A')
t2 = threading.Thread(target=task_b, name='Worker-B')

t1.start()
t2.start()
t1.join()
t2.join()

# 3. Останавливаем профилирование
yappi.stop()

# 4. Получаем и выводим статистику по ВСЕМ функциям
# func_stats = yappi.get_func_stats()

# 4.1 фильтрация, если нужна
func_stats = yappi.get_func_stats(filter_callback=lambda f: f.name.startswith("task"))

func_stats.sort("ttot", "desc")  # Сортируем по суммарному времени
func_stats.print_all()

# 5. информация по потокам
thread_stats = yappi.get_thread_stats()

thread_stats.sort("ttot", "desc")
thread_stats.print_all()
