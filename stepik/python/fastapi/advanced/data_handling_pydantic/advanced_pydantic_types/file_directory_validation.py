# Создадим фиктивные файлы/директории для примера
import os

from pydantic import BaseModel, FilePath, DirectoryPath

if not os.path.exists("test_dir"):
    os.makedirs("test_dir")
with open("test_file.txt", "w") as f:
    f.write("Hello")


class ConfigPaths(BaseModel):
    log_file: FilePath
    data_directory: DirectoryPath


try:
    # Корректный пример
    paths = ConfigPaths(
        log_file="test_file.txt",
        data_directory="test_dir"
    )
    print(f"\n--- Корректные пути ---")
    print(paths)

    # Некорректный пример: файл не существует
    print(f"\n--- Некорректный файл ---")
    ConfigPaths(
        log_file="non_existent_file.txt",
        data_directory="test_dir"
    )
except Exception as e:  # Перехватываем PydanticCustomError или ValidationError
    print(e)
    # Ожидаемая ошибка: log_file: file_not_found (для FilePath)

try:
    # Некорректный пример: директория не существует
    print(f"\n--- Некорректная директория ---")
    ConfigPaths(
        log_file="test_file.txt",
        data_directory="non_existent_dir"
    )
except Exception as e:
    print(e)
    # Ожидаемая ошибка: data_directory: directory_not_found (для DirectoryPath)

# Очистка
os.remove("test_file.txt")
os.rmdir("test_dir")
