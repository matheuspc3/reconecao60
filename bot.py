"""reconecao60 — Bot educativo do Telegram para seguranca digital de pessoas idosas.

Entry point do bot. Inicializa o Application, registra os handlers e inicia o polling.

Uso:
    python bot.py

O token do bot deve ser configurado na variavel de ambiente TELEGRAM_BOT_TOKEN
ou no arquivo .env (baseado no .env.example).
"""

from telegram import Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_NAME, TELEGRAM_BOT_TOKEN

# Handlers
from handlers.conversation import handle_message
from handlers.menu import help_command, menu_command, topic_callback
from handlers.start import start


def main() -> None:
    """Inicializa e executa o bot."""
    print(f"Iniciando o {BOT_NAME}...")

    # Cria a aplicacao
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # --- Registro de handlers ---

    # Comando /start — boas-vindas
    application.add_handler(CommandHandler("start", start))

    # Comando /menu — lista de temas com teclado inline
    application.add_handler(CommandHandler("menu", menu_command))

    # Comando /ajuda — explicacao de como usar
    application.add_handler(CommandHandler("ajuda", help_command))
    application.add_handler(CommandHandler("help", help_command))

    # Cliques no menu inline (topic:slug)
    application.add_handler(CallbackQueryHandler(topic_callback, pattern=r"^topic:"))

    # Handler conversacional principal — TODA mensagem de texto
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message,
        )
    )

    print(f"{BOT_NAME} pronto! Iniciando polling...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
