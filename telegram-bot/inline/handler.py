from html import escape
from uuid import uuid4

from telegram import (InlineQueryResultArticle, InputTextMessageContent, Update)
from telegram.constants import ParseMode
from telegram.ext import (ContextTypes)

from logger import get_logger

logger = get_logger(__name__)


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
