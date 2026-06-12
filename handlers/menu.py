"""Comandos /menu e /ajuda — suporte secundario via teclado inline."""

from typing import Sequence

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from content.responses import HELP_MESSAGE, MENU_OPTIONS
from content.topics import TOPICS


# Layout do menu (2 botoes por linha)
MENU_LAYOUT: list[list[str]] = [
    ["golpes-whatsapp", "golpes-pix"],
    ["falso-parente", "clonagem-whatsapp"],
    ["boleto-falso", "links-falsos"],
    ["ligacoes-suspeitas", "seguranca-banco-digital"],
    ["promocoes-falsas", "compras-internet"],
    ["senhas-seguras", "verificacao-duas-etapas"],
    ["falso-funcionario-banco", "codigo-verificacao"],
    ["virus-celular", "redes-sociais"],
    ["golpes-sms", "urgencia-medo"],
    ["site-falso", "dicas-gerais"],
]


def build_menu_keyboard() -> InlineKeyboardMarkup:
    """Constrói o teclado inline do menu de temas.

    Returns:
        Um InlineKeyboardMarkup com os botões do menu.
    """
    keyboard: list[list[InlineKeyboardButton]] = []

    for row_slugs in MENU_LAYOUT:
        row: list[InlineKeyboardButton] = []
        for slug in row_slugs:
            label = MENU_OPTIONS.get(slug, slug)
            row.append(
                InlineKeyboardButton(label, callback_data=f"topic:{slug}")
            )
        keyboard.append(row)

    return InlineKeyboardMarkup(keyboard)


async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /menu — mostra todos os temas disponiveis."""
    await update.message.reply_text(
        "📚 Temas que voce pode aprender comigo:\n\n"
        "Clique em um dos botoes abaixo ou digite "
        "sua duvida do seu jeito:",
        reply_markup=build_menu_keyboard(),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /ajuda — explica como usar o bot."""
    await update.message.reply_text(HELP_MESSAGE)


async def topic_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Callback quando o usuario clica em um topico no menu inline."""
    query = update.callback_query
    await query.answer()

    # Extrai o slug do callback_data: "topic:golpes-whatsapp" -> "golpes-whatsapp"
    slug = query.data.removeprefix("topic:")

    topic = TOPICS.get(slug)
    if not topic:
        await query.edit_message_text(
            "Tema nao encontrado. Use /menu para ver os temas disponiveis.",
        )
        return

    # Constrói a mensagem no formato de 3 partes
    message = (
        f"{topic['title']}\n\n"
        f"📖 O que e:\n{topic['what']}\n\n"
        f"🔍 Como identificar:\n{topic['identify']}\n\n"
        f"🛡️ Como se proteger:\n{topic['protect']}"
    )

    await query.edit_message_text(
        message,
        reply_markup=build_menu_keyboard(),
    )
