"""Templates de resposta do reconecao60.

Contem mensagens de acolhimento, orientacao pos-golpe, avisos de dados sensiveis,
e respostas conversacionais usadas pelo handler de conversa.
"""

# --- Mensagem de boas-vindas (comando /start) ---
WELCOME_MESSAGE = (
    "Ola! Eu sou o reconecao60 📱🔒\n\n"
    "Estou aqui para te ajudar a usar o celular, a internet, "
    "o WhatsApp e aplicativos com mais seguranca.\n\n"
    "Eu posso te ensinar a reconhecer golpes, mensagens falsas, "
    "links perigosos e cuidados com banco, Pix e senhas.\n\n"
    "Antes de comecar, lembre-se:\n\n"
    "✅ Nunca envie senhas.\n"
    "✅ Nunca envie codigo do banco ou do WhatsApp.\n"
    "✅ Nunca envie foto de documento.\n"
    "✅ Nunca clique em links suspeitos.\n"
    "✅ Nunca faca Pix com pressa sem confirmar antes.\n\n"
    "Sobre o que voce quer aprender hoje?"
)

# --- Boas-vindas conversacional (quando usuario manda "oi" etc.) ---
WELCOME_CONVERSATIONAL = (
    "Ola! Eu sou o reconecao60 📱🔒\n\n"
    "Estou aqui para te ajudar a usar o celular, a internet, "
    "o WhatsApp e aplicativos com mais seguranca.\n\n"
    "Sobre o que voce quer conversar hoje?\n\n"
    "Voce pode me perguntar sobre qualquer tema de seguranca digital. "
    "Pode tambem me enviar uma mensagem que recebeu e eu te ajudo "
    "a verificar se parece golpe.\n\n"
    "E so escrever do seu jeito! 💙"
)

# --- Saudacao ---
GREETING_RESPONSE = (
    "Ola! Que bom falar com voce! 😊\n\n"
    "Sobre o que voce quer aprender hoje?\n\n"
    "Pode me perguntar sobre golpes, seguranca no celular, "
    "ou me enviar uma mensagem suspeita que recebeu para eu analisar.\n\n"
    "Estou aqui para ajudar! 💙"
)

# --- Como vai ---
HOW_ARE_YOU_RESPONSE = (
    "Estou bem e pronto para ajudar! 😊\n\n"
    "Sobre o que voce quer conversar hoje? Pode me perguntar "
    "qualquer coisa sobre seguranca digital, golpes, senhas, "
    "ou me enviar uma mensagem suspeita para analisar.\n\n"
    "E so falar do seu jeito!"
)

# --- Agradecimento ---
THANKS_RESPONSE = (
    "Por nada! Fico feliz em poder ajudar. 💙\n\n"
    "Se tiver mais alguma duvida no futuro, "
    "e so me chamar. Estou sempre aqui!\n\n"
    "Quer aprender sobre mais algum tema?"
)

# --- Despedida ---
GOODBYE_RESPONSE = (
    "Ate mais! Foi um prazer conversar com voce. 💙\n\n"
    "Quando precisar, e so me chamar. Estou sempre aqui "
    "para ajudar com seguranca digital.\n\n"
    "Fique bem e se cuide!"
)

# --- Fallback conversacional ---
FALLBACK_CONVERSATIONAL = (
    "Nao entendi muito bem, mas posso te ajudar com muitas coisas! 😊\n\n"
    "Voce pode me perguntar sobre:\n\n"
    "• Golpes no WhatsApp e no Pix\n"
    "• Como saber se uma mensagem e falsa\n"
    "• Falso parente pedindo dinheiro\n"
    "• Links suspeitos e sites falsos\n"
    "• Seguranca no banco digital\n"
    "• Como criar senhas seguras\n"
    "• Clonagem de WhatsApp\n"
    "• Boletos falsos\n"
    "• E muito mais!\n\n"
    "Tambem pode me enviar uma mensagem que recebeu que eu "
    "te ajudo a verificar se parece golpe.\n\n"
    "E so escrever do seu jeito, com suas palavras. 💙"
)

# --- Mensagem de ajuda (/ajuda) ---
HELP_MESSAGE = (
    "Como usar o reconecao60 📱🔒\n\n"
    "Eu sou um assistente educativo. Voce pode conversar comigo "
    "naturalmente, como se estivesse falando com uma pessoa.\n\n"
    "Por exemplo, voce pode digitar:\n\n"
    "• \"meu filho pediu dinheiro por mensagem\"\n"
    "• \"como sei se um link e perigoso\"\n"
    "• \"recebi um boleto estranho\"\n"
    "• \"cai em um golpe, o que faco\"\n"
    "• \"como criar uma senha segura\"\n\n"
    "Ou simplesmente me enviar a mensagem suspeita "
    "que voce recebeu para eu analisar!\n\n"
    "Comandos disponiveis:\n"
    "/start — Mensagem de boas-vindas\n"
    "/menu — Ver todos os temas\n"
    "/ajuda — Esta mensagem\n\n"
    "Lembre-se: nunca compartilhe senhas, CPF ou dados bancarios aqui. 💙"
)

# --- Aviso de dados sensiveis ---
SENSITIVE_DATA_WARNING = (
    "Por seguranca, nao envie esse tipo de informacao aqui.\n\n"
    "Apague dados pessoais antes de compartilhar qualquer "
    "mensagem suspeita, como:\n\n"
    "• Nome completo\n"
    "• CPF\n"
    "• Numero de conta\n"
    "• Senha\n"
    "• Codigo recebido por SMS\n"
    "• Numero de cartao\n"
    "• Endereco\n"
    "• Foto de documento\n\n"
    "Depois que voce apagar essas informacoes, pode me enviar "
    "a mensagem novamente que eu ajudo a verificar!"
)

# --- Acolhimento pos-golpe ---
POST_SCAM_SUPPORT = (
    "Sinto muito que isso tenha acontecido. Golpistas usam truques "
    "para enganar pessoas de todas as idades. Agora o mais importante "
    "e agir rapido e com calma.\n\n"
    "✅ O que fazer agora:\n\n"
    "1. Pare de conversar com o suspeito.\n"
    "2. Nao envie mais dinheiro.\n"
    "3. Tire prints das conversas.\n"
    "4. Avise o banco imediatamente.\n"
    "5. Bloqueie cartoes, se necessario.\n"
    "6. Troque suas senhas.\n"
    "7. Avise seus familiares.\n"
    "8. Registre boletim de ocorrencia, se houve prejuizo.\n"
    "9. Peca ajuda a alguem de confianca.\n\n"
    "Voce nao esta sozinho(a). Isso pode acontecer com qualquer pessoa. "
    "O importante agora e se proteger e impedir que continue.\n\n"
    "Se quiser conversar mais sobre o assunto ou tiver outras duvidas, "
    "estou aqui. 💙"
)

# --- Labels do menu (usado no /menu e no teclado inline de fallback) ---
MENU_OPTIONS = {
    "golpes-whatsapp": "📱 Golpes no WhatsApp",
    "golpes-pix": "💸 Golpes do Pix",
    "links-falsos": "🔗 Links falsos",
    "ligacoes-suspeitas": "📞 Ligacoes suspeitas",
    "seguranca-banco-digital": "🏦 Seguranca no banco digital",
    "dicas-gerais": "💡 Dicas gerais de seguranca",
    "falso-parente": "👨‍👩‍👧 Falso parente",
    "trocou-de-numero": "📞 Troquei de numero",
    "falso-funcionario-banco": "🏦 Falso funcionario de banco",
    "clonagem-whatsapp": "🔄 Clonagem de WhatsApp",
    "codigo-verificacao": "🔐 Codigo de verificacao",
    "boleto-falso": "📄 Boleto falso",
    "promocoes-falsas": "🎁 Promocoes falsas",
    "falso-suporte": "💻 Falso suporte tecnico",
    "golpe-maquininha": "💳 Golpe da maquininha",
    "compras-internet": "🛒 Compras pela internet",
    "urgencia-medo": "⚠️ Golpes com urgencia ou medo",
    "redes-sociais": "📱 Cuidados com redes sociais",
    "golpes-sms": "📩 Golpes por SMS",
    "senhas-seguras": "🔑 Senhas seguras",
    "verificacao-duas-etapas": "🛡️ Verificacao em duas etapas",
    "virus-celular": "🦠 Virus no celular",
    "site-falso": "🌐 Sites falsos",
}
