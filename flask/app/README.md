# Simple Flask Web Application

## Описание

Минималистичное Flask-приложение, созданное на основе [Flask QuickStart Tutorial](https://flask.palletsprojects.com/en/stable/quickstart/). Служит введением в основные концепции Flask-фреймворка.

## Функциональность

- Основные маршруты URL
- Рендеринг HTML-шаблонов с использованием Jinja2
- Статические файлы (CSS-стили)
- Обработка базовых HTTP-запросов

## Структура проекта

```
app/
├── app.py              # Основной файл приложения
├── static/
│   └── styles.css      # CSS-стили
└── templates/
    └── login.html      # HTML-шаблон страницы входа
```

## Установка и запуск

### Требования

- Python 3.10+
- Flask 3.x

### Установка

```bash
cd flask/app
pip install flask
```

### Запуск

```bash
python app.py
```

Приложение будет доступно по адресу: http://127.0.0.1:5000/

## Ключевые концепции

### Создание приложения

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
```

### Запуск в режиме отладки

```python
if __name__ == '__main__':
    app.run(debug=True)
```

## Ссылки

- [Flask QuickStart Tutorial](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Flask Documentation](https://flask.palletsprojects.com/)