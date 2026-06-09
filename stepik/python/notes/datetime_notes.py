# ------------------ Модуль datetime ------------------
from datetime import *

# ===== Класс date =====
date(year, month, day)                   # создаёт объект даты
date.today()                             # текущая локальная дата
date.min                                 # минимально допустимая дата
date.max                                 # максимально допустимая дата
date.fromordinal(n)                      # дата из порядкового числа (1.1.0001 = 1)
date.toordinal()                         # преобразует дату в порядковое число
date.replace(...)                        # возвращает копию с изменёнными параметрами
date.weekday()                           # день недели (0 — понедельник, 6 — воскресенье)
date.isoweekday()                        # день недели (1 — понедельник, 7 — воскресенье)
date.strftime(fmt)                       # форматирует дату в строку
date.isoformat()                         # строка в формате YYYY-MM-DD
.date.year                               # год
.date.month                              # месяц
.date.day                                # день

# ===== Класс time =====
time(hour=0, minute=0, second=0, microsecond=0)   # создаёт объект времени
time.replace(...)                        # копия объекта с заменёнными параметрами
time.strftime(fmt)                       # форматирует объект time в строку по fmt
time.isoformat()                         # строка в формате HH:MM:SS(.ffffff)
.time.hour                               # часы
.time.minute                             # минуты
.time.second                             # секунды
.time.microsecond                        # микросекунды

# ===== Класс datetime =====
datetime(...)                            # создаёт дату + время
datetime.combine(date_obj, time_obj)     # объединяет date и time
datetime.now(tz=None)                    # локальное текущее время (можно указать tz)
datetime.utcnow()                        # UTC-время (устарело с Python 3.12)
datetime.today()                         # эквивалент now() без tz
datetime.fromtimestamp(sec)              # datetime из секунд с эпохи
datetime.strptime(str, fmt)              # строка → datetime по формату
datetime.replace(...)                    # копия объекта с заменёнными параметрами
datetime.timestamp()                     # кол-во секунд от начала эпохи
datetime.isoformat()                     # строка ISO: YYYY-MM-DDTHH:MM:SS(.ffffff)
datetime.strftime(fmt)                   # форматирование в строку

.datetime.year                           # год
.datetime.month                          # месяц
.datetime.day                            # день
.datetime.hour                           # час
.datetime.minute                         # минута
.datetime.second                         # секунда
.datetime.microsecond                    # микросекунда

datetime.date()                         # извлекает компоненту date
datetime.time()                         # извлекает компоненту time

# ===== Класс timedelta =====
timedelta(...)                           # создаёт временной интервал
timedelta.total_seconds()                # общее кол-во секунд (float)
.timedelta.days                          # количество дней
.timedelta.seconds                       # количество секунд (<86400)
.timedelta.microseconds                  # микросекунды (<1_000_000)

# ===== Таблица форматирования =====
| Формат | Значение
| %a | Сокращенное название дня недели
| %A | Полное название дня недели
| %w | Номер дня недели [0, …, 6]
| %d | День месяца [01, …, 31]
| %b | Сокращенное название месяца
| %B | Полное название месяца
| %m | Номер месяца [01, …,12]
| %y | Год без века [00, …, 99]
| %Y | Год с веком
| %H | Час (24-часовой формат) [00, …, 23]
| %I | Час (12-часовой формат) [01, …, 12]
| %p | До полудня или после (при 12-часовом формате)
| %M | Число минут [00, …, 59]
| %S | Число секунд [00, …, 59]
| %f | Число микросекунд
| %z | Разница с UTC в формате ±HHMM[SS[.ffffff]]
| %Z | Временная зона
| %j | День года [001,366]
| %U | Номер недели в году (неделя начинается с воскр.)
| %W | Номер недели в году (неделя начинается с пон.)
| %c | Дата и время
| %x | Дата
| %X | Время

# ===== Операции с timedelta =====
+                                        # сложение интервалов
-                                        # разность интервалов
*                                        # умножение на число
/                                        # деление на число (float)
/ /                                      # целочисленное деление
%                                        # остаток от деления
abs()                                    # модуль (положительное значение)

# ===== Операции с datetime и date =====
datetime ± timedelta → datetime          # сдвиг даты/времени
date ± timedelta → date                  # сдвиг даты (неполные дни отбрасываются)
datetime - datetime → timedelta          # разность между datetime
date - date → timedelta                  # разность между датами

# ===== Сравнение объектов =====
==, !=, <, >, <=, >=                     # сравнение date/time/datetime/timedelta

# ===== Встроенные функции =====
str(obj)                                 # строковое представление
repr(obj)                                # тех. представление (в виде конструктора)
min(), max(), sorted()                   # работают с date/datetime/timedelta
abs(timedelta)                           # модуль

# ===== Локализация =====
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')     # установка русской локали
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')     # установка английской локали

# ===== Константы =====
datetime.MINYEAR                         # минимальный год — 1
datetime.MAXYEAR                         # максимальный год — 9999

# ===== Важные примечания =====
# datetime и timedelta — неизменяемые типы (hashable)
# datetime наследует методы и атрибуты от date
# strftime() работает одинаково для date/time/datetime
# isoformat() для datetime добавляет "T" между датой и временем
# timedelta не имеет .hours и .minutes — извлекаются из .seconds вручную
# timedelta может быть отрицательным
# timedelta нормализует значения: минуты → секунды, часы → дни и т.д.
# сравнение timedelta с int/str вызывает TypeError (кроме ==, !=)
# str(obj) автоматически вызывается при print()
# при strptime формат и строка должны строго совпадать — иначе ValueError
# date + timedelta с неполными сутками округляется в сторону дней
# timedelta / timedelta → float, // → int
