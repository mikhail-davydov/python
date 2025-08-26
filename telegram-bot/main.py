from telegram.ext import (ApplicationBuilder, CommandHandler, filters, InlineQueryHandler, MessageHandler)

from command.handler import feedback, help, start
from config.settings import read_config
from inline.handler import inline_query
from logger import logger
from message.handler import echo

SETTINGS_FILE_PATH = '.private/bot-settings.json'


def main():
    bot_settings = read_config(SETTINGS_FILE_PATH)
    logger.info(f'bot_settings:\n{bot_settings.to_json()}')

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
