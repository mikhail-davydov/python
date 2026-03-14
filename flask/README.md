# Flask Framework — Коллекция приложений

## Описание

Коллекция учебных Flask-приложений различной сложности. Каждый проект демонстрирует различные подходы к разработке на Flask и служит практическим примером изучения фреймворка.

## Проекты

### [`app/`](app/README.md) — Простое веб-приложение

Минималистичное приложение на основе [Flask QuickStart Tutorial](https://flask.palletsprojects.com/en/stable/quickstart/). Демонстрирует базовые концепции:

- Маршрутизация URL
- Шаблонизация (Jinja2)
- Статические файлы (CSS)
- Обработка форм

### [`flaskr/`](flaskr/README.md) — Блог-приложение

Полноценное блог-приложение из [официального Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/). Включает:

- Система регистрации и входа пользователей
- Создание, редактирование и удаление постов
- Использование SQLite базы данных
- Схема базы данных и миграции

## Технологический стек

| Компонент | Технология |
|-----------|------------|
| Веб-фреймворк | Flask 3.x |
| Шаблонизация | Jinja2 |
| База данных | SQLite |
| Тестирование | pytest |
| WSGI-сервер | встроенный (debug) |

## Структура директории

```
flask/
├── app/                     # Простое Flask-приложение
│   ├── app.py               # Основной файл приложения
│   ├── static/              # Статические файлы
│   └── templates/           # HTML-шаблоны
├── flaskr/                  # Блог-приложение
│   ├── flaskr/              # Пакет приложения
│   │   ├── __init__.py      # Фабрика приложения
│   │   ├── auth.py          # Модуль аутентификации
│   │   ├── blog.py          # Модуль блога
│   │   └── db.py            # Работа с базой данных
│   ├── static/              # CSS-стили
│   ├── templates/           # HTML-шаблоны
│   ├── schema.sql           # Схема базы данных
│   ├── requirements.txt     # Зависимости
│   └── Dockerfile           # Docker-конфигурация
├── tests/                   # Интеграционные тесты
├── instance/                # Директория для БД
└── pyproject.toml          # Конфигурация проекта
```

## Установка и запуск

### Требования

- Python 3.10+
- Flask 3.x

### Вариант 1: Простое приложение (app)

```bash
cd flask/app
pip install flask
python app.py
```

Приложение будет доступно по адресу: http://127.0.0.1:5000/

### Вариант 2: Блог-приложение (flaskr)

```bash
cd flask/flaskr
pip install -r requirements.txt
flask run --debug
```

## Тестирование

```bash
cd flask
pytest
```

Запуск конкретного тестового файла:

```bash
pytest tests/test_auth.py
pytest tests/test_blog.py
```

## Ссылки

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask QuickStart](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)