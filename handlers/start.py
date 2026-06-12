"""Handler do comando /start — mensagem de boas-vindas conversacional."""

from telegram import Update
from telegram.ext import ContextTypes

from content.responses import WELCOME_CONVERSATIONAL


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde ao comando /start com a mensagem de boas-vindas."""
    await update.message.reply_text(WELCOME_CONVERSATIONAL)
