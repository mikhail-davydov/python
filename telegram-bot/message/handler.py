from telegram import (Update)
from telegram.ext import (ContextTypes)

from logger import get_logger

logger = get_logger(__name__)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Простой ответ на сообщение
    logger.info("Get message: %s", update.message.text)
    await update.message.reply_text(f'Вы написали: {update.message.text}')
