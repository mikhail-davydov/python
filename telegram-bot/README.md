# Telegram Bot Sandbox

## Описание

Учебная песочница для создания Telegram-ботов с использованием библиотеки [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot). Демонстрирует различные паттерны и подходы к разработке ботов.

## Функциональность

Проект содержит примеры реализации различных типов обработчиков:

### Обработчики команд
- Команды бота (например, `/start`, `/help`, `/settings`)
- Обработка через [`command/handler.py`](command/handler.py)

### Обработчики сообщений
- Текстовые сообщения
- Обработка через [`message/handler.py`](message/handler.py)

### Инлайн-клавиатуры
- Кнопки в чате
- Обработка через [`inline/handler.py`](inline/handler.py)

## Структура проекта

```
telegram-bot/
├── main.py              # Точка входа, запуск бота
├── logger.py            # Логирование
├── command/
│   └── handler.py       # Обработчики команд
├── message/
│   └── handler.py       # Обработчики сообщений
├── inline/
│   └── handler.py       # Обработчики инлайн-кнопок
└── config/
    └── settings.py      # Конфигурация бота
```

## Установка и запуск

### Требования

- Python 3.10+
- python-telegram-bot

### Установка зависимостей

```bash
cd telegram-bot
pip install python-telegram-bot
```

### Конфигурация

В файле `.private/bot-settings.json` укажите токен вашего бота:

```json
{
    "token": "YOUR_BOT_TOKEN_HERE"
}
```

### Запуск

```bash
python main.py
```

## Примеры кода

### Обработчик команды

```python
from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я Telegram бот.")
```

### Обработчик инлайн-кнопок

```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Вы нажали на кнопку!")
```

## Ссылки

- [python-telegram-bot Wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Документация python-telegram-bot](https://docs.python-telegram-bot.org/)