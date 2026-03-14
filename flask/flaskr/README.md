# Flaskr — Блог-приложение

## Описание

Полноценное блог-приложение на Flask, созданное на основе [официального Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/). Демонстрирует архитектурный подход к построению Flask-приложений с использованием паттерна "фабрика приложений".

## Функциональность

### Аутентификация пользователей
- Регистрация новых пользователей
- Вход и выход из системы
- Управление сессиями

### Блог
- Просмотр списка всех постов
- Создание новых постов
- Редактирование существующих постов
- Удаление постов (только автором)

## Архитектура

Приложение использует паттерн "фабрика приложений" (Application Factory) для гибкой конфигурации и тестирования.

```
flaskr/
├── __init__.py      # Фабрика приложения create_app()
├── auth.py          # Маршруты и логика аутентификации
├── blog.py          # Маршруты и логика блога
├── db.py            # Утилиты для работы с базой данных
├── schema.sql       # Схема базы данных
├── static/
│   └── style.css    # CSS-стили
├── templates/       # HTML-шаблоны
│   ├── base.html    # Базовый шаблон
│   ├── auth/        # Шаблоны аутентификации
│   │   ├── login.html
│   │   └── register.html
│   └── blog/        # Шаблоны блога
│       ├── index.html
│       ├── create.html
│       └── update.html
├── requirements.txt # Зависимости
└── Dockerfile       # Docker-конфигурация
```

## База данных

Используется SQLite с следующей схемой:

### Таблица users
| Поле | Тип | Описание |
|------|-----|----------|
| id | INTEGER | ID пользователя (PK) |
| username | TEXT | Уникальное имя пользователя |
| password | TEXT | Хэш пароля |

### Таблица posts
| Поле | Тип | Описание |
|------|-----|----------|
| id | INTEGER | ID поста (PK) |
| author_id | INTEGER | ID автора (FK) |
| title | TEXT | Заголовок поста |
| body | TEXT | Содержание поста |
| created | TIMESTAMP | Дата создания |

## Установка и запуск

### Требования

- Python 3.10+
- Flask 3.x

### Установка зависимостей

```bash
cd flask/flaskr
pip install -r requirements.txt
```

### Инициализация базы данных

```bash
flask init-db
```

### Запуск

```bash
flask run --debug
```

Приложение будет доступно по адресу: http://127.0.0.1:5000/

## Docker

Для запуска в Docker:

```bash
docker build -t flaskr .
docker run -d -p 5000:5000 flaskr
```

## Тестирование

Запуск тестов:

```bash
cd flask
pytest tests/
```

## Ссылки

- [Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)
- [Flask Documentation](https://flask.palletsprojects.com/)