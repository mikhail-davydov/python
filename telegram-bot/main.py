import json
import logging
from html import escape
from uuid import uuid4

from telegram import (
    Update,
    InlineQueryResultArticle,
    InputTextMessageContent,
    )
from telegram.constants import ParseMode
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    InlineQueryHandler,
    )

from config.settings import BotSettings

SETTINGS_FILE_PATH = '.private/bot-settings.json'

# Настройка уровня логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    )

# Установка уровня для HTTPX
logging.getLogger('httpx').setLevel(logging.WARNING)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Простой ответ на сообщение
    logging.info(f'get message: {update.message.text}')
    await update.message.reply_text(f'Вы написали: {update.message.text}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("call /start")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    if context.args:
        user_says = " ".join(context.args)
        await update.message.reply_text("You said: " + user_says)


async def help(update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("call /help")
    help_message = (
        "Список доступных команд:\n\n"
        "/start [args] - Запуск бота\n"
        "/help - Показать список команд\n"
        "/feedback - Обратная связь"
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)


async def feedback(update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("call /feedback")
    feedback_message = context.bot_data.get('feedback_email')
    await update.message.reply_text(feedback_message)


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query

    if not query:  # пустой запрос не должен обрабатываться
        return

    # Создаем результаты для отображения
    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Scream",
            input_message_content=InputTextMessageContent(f"Scream: {query.upper()}!"),
            ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Bold",
            input_message_content=InputTextMessageContent(
                f"Bold: <b>{escape(query)}</b>", parse_mode=ParseMode.HTML,
                ),
            ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Italic",
            input_message_content=InputTextMessageContent(
                f"Italic: <i>{escape(query)}</i>", parse_mode=ParseMode.HTML,
                ),
            ),
        ]

    await update.inline_query.answer(results)


def read_config(file_path):
    logging.info(f'file_path: {file_path}')
    with open(file_path, 'r') as file:
        data = json.load(file)
        return BotSettings(**data)


def main():
    bot_settings = read_config(SETTINGS_FILE_PATH)
    logging.info(f'bot_settings:\n{bot_settings.to_json()}')

    app = ApplicationBuilder().token(bot_settings.token).build()

    # Сохраняем параметры в контексте бота
    app.bot_data['feedback_email'] = bot_settings.feedback_email

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('feedback', feedback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.add_handler(InlineQueryHandler(inline_query))

    app.run_polling()


if __name__ == '__main__':
    main()
