from telegram import (Update)
from telegram.ext import (ContextTypes)

from logger import get_logger

logger = get_logger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("call /start")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    if context.args:
        user_says = " ".join(context.args)
        await update.message.reply_text("You said: " + user_says)


async def help(update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("call /help")
    help_message = (
        "Список доступных команд:\n\n"
        "/start [args] - Запуск бота\n"
        "/help - Показать список команд\n"
        "/feedback - Обратная связь"
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)


async def feedback(update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("call /feedback")
    feedback_message = context.bot_data.get('feedback_email')
    await update.message.reply_text(feedback_message)
