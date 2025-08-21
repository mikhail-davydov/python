import logging, json
from config.settings import BotSettings

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    )

ROOT = '..'
SETTINGS_FILE_PATH = '/.private/bot-settings.json'
TOKEN = '<token-template>'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    )


def main():
    bot_settings = read_config(ROOT + SETTINGS_FILE_PATH)
    logging.info(f'bot_settings:\n{bot_settings.to_json()}')

    app = ApplicationBuilder().token(bot_settings.token).build()

    # Сохраняем параметры в контексте бота
    app.bot_data['feedback_email'] = bot_settings.feedback_email

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('feedback', feedback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()


async def echo(update: Update, context):
    # Простой ответ на сообщение
    logging.info(f'get message: {update.message.text}')
    await update.message.reply_text(f'Вы написали: {update.message.text}')


async def start(update: Update, context):
    logging.info("call /start")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def help(update, context):
    logging.info("call /help")
    help_message = (
        "Список доступных команд:\n\n"
        "/start - Запуск бота\n"
        "/help - Показать список команд\n"
        "/feedback - Обратная связь"
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)


async def feedback(update, context):
    logging.info("call /feedback")
    feedback_message = context.bot_data.get('feedback_email')
    await update.message.reply_text(feedback_message)


def read_config(file_path):
    logging.info(f'file_path: {file_path}')
    with open(file_path, 'r') as file:
        data = json.load(file)
        return BotSettings(**data)


if __name__ == '__main__':
    main()
