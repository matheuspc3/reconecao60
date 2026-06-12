"""Carrega configurações do bot a partir de variáveis de ambiente."""

import os
import sys

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TELEGRAM_BOT_TOKEN:
    print("ERRO: TELEGRAM_BOT_TOKEN nao encontrado.")
    print("   Crie um arquivo .env baseado no .env.example com o token do seu bot.")
    print("   Obtenha o token com o @BotFather no Telegram.")
    sys.exit(1)

# Nome e identidade do bot
BOT_NAME = "reconecao60"
BOT_USERNAME = "@reconecao60_bot"
BOT_LINK = "t.me/reconecao60_bot"
