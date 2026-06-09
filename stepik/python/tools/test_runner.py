import os
import subprocess
import sys


def run_tests_in_directory(tests_dir, code_file):
    """
    Выполняет все файлы без расширения в указанной директории как Python-скрипты
    и сравнивает их вывод с содержимым соответствующих .clue-файлов.
    Код из указанного файла будет доступен при выполнении тестов.
    
    Аргументы:
    tests_dir (str): Директория с тестовыми файлами и .clue-файлами
    code_file (str): Путь к .py файлу с кодом, который нужно использовать в тестах
    """
    # Проверяем существование директории с тестами
    if not os.path.exists(tests_dir):
        print(f"Ошибка: Директория с тестами не существует: {tests_dir}")
        return

    # Проверяем существование файла с кодом
    if not os.path.exists(code_file):
        print(f"Ошибка: Файл с кодом не существует: {code_file}")
        return

    # Получаем список всех файлов в директории с тестами
    files = os.listdir(tests_dir)

    # Фильтруем файлы без расширения (и не .clue)
    script_files = [f for f in files if '.' not in f and f != 'clue']

    # Сортируем файлы для предсказуемого порядка выполнения
    script_files.sort()

    # Читаем содержимое файла с кодом
    try:
        with open(code_file, 'r', encoding='utf-8') as f:
            code_content = f.read()
    except Exception as e:
        print(f"Ошибка при чтении файла с кодом {code_file}: {str(e)}")
        return

    for script_file in script_files:
        clue_file = script_file + '.clue'

        # Проверяем наличие .clue файла
        if clue_file not in files:
            print(f"Предупреждение: Для файла {script_file} не найден соответствующий {clue_file}")
            continue

        # Полные пути к файлам
        script_path = os.path.join(tests_dir, script_file)
        clue_path = os.path.join(tests_dir, clue_file)

        # Читаем содержимое тестового скрипта
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                script_code = f.read()
        except Exception as e:
            actual_output = f"[ERROR: Не удалось прочитать файл {script_file}: {str(e)}]\n"
            print(f"Test #{script_file}: НЕСОВПАДЕНИЕ")
            print(f"Ожидаемый вывод:\n{expected_output.strip()}\n")
            print(f"Текущий вывод:\n{actual_output.strip()}\n")
            print(f"Код из теста:\n{script_code.strip()}\n")
            print("-" * 50)
            continue

        # Объединяем код: сначала код из файла с кодом, затем код скрипта
        combined_code = code_content + "\n" + script_code

        # Создаем временный файл с объединенным кодом
        temp_script_path = script_path + "._temp"
        try:
            with open(temp_script_path, 'w', encoding='utf-8') as f:
                f.write(combined_code)

            # Используем абсолютные пути и экранируем их при необходимости
            executable = sys.executable
            temp_script = os.path.abspath(temp_script_path)
            work_dir = os.path.abspath(os.path.dirname(code_file))
            python_path = os.path.abspath(os.path.dirname(code_file))

            # Выполняем временный файл, передавая правильные аргументы окружения
            result = subprocess.run(
                [executable, temp_script],
                capture_output=True,
                text=True,
                timeout=30,
                cwd=work_dir,
                env={**os.environ, 'PYTHONPATH': python_path},
                encoding='utf-8'
            )
            actual_output = result.stdout

            if result.returncode != 0:
                actual_output += result.stderr

        except subprocess.TimeoutExpired:
            actual_output = "[ERROR: Таймаут выполнения]\n"
        except Exception as e:
            actual_output = f"[ERROR: {str(e)}]\n"
        finally:
            # Удаляем временный файл
            if os.path.exists(temp_script_path):
                try:
                    os.remove(temp_script_path)
                except:
                    pass

        # Читаем ожидаемый вывод из .clue файла
        try:
            with open(clue_path, 'r', encoding='utf-8') as f:
                expected_output = f.read()
        except Exception as e:
            print(f"Ошибка при чтении {clue_file}: {str(e)}")
            continue

        # Сравниваем вывод
        if actual_output.strip() == expected_output.strip():
            print(f"Test #{script_file}: успешно")
        else:
            print("-" * 10)
            print(f"Test #{script_file}: НЕСОВПАДЕНИЕ")
            print(f"Ожидаемый вывод:\n{expected_output.strip()}\n")
            print(f"Текущий вывод:\n{actual_output.strip()}\n")
            print(f"Код из теста:\n{script_code.strip()}\n")
            print("-" * 10)


if __name__ == "__main__":
    # run_tests_in_directory('task_3_test', 'task_3.py')
    pass
