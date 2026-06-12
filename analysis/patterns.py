"""Padrões de regex e palavras-chave para detecção de golpes."""

import re

# Palavras-chave de ALTO risco — indicam forte probabilidade de golpe
HIGH_RISK_KEYWORDS: list[str] = [
    # Ameaças e urgência
    "bloqueado", "bloqueada", "bloquearam", "bloqueio",
    "urgente", "urgência", "imediatamente", "agora",
    "cancelado", "cancelada", "suspeita", "invadida",
    "invadiram", "invadido", "processo judicial",
    "ordem judicial", "protesto", "serasa", "spc",

    # Pedidos de ação com link
    "clique no link", "clique aqui", "acesse o link",
    "acesse aqui", "abra o link", "link abaixo",
    "atualize seus dados", "confirme seus dados",
    "verifique sua conta", "valide seu cadastro",
    "regularize", "regularização",

    # Pedidos de Pix/dinheiro
    "pix agora", "faz um pix", "faça um pix",
    "pix urgente", "preciso de um pix", "me faz um pix",
    "deposita", "transfere pra mim",

    # Senhas e códigos
    "envie sua senha", "digite sua senha", "sua senha",
    "código de segurança", "código de verificação",
    "código que chegou", "código enviado",
    "token", "senha do banco", "senha do cartão",

    # Prêmios falsos
    "ganhou um prêmio", "você foi sorteado", "prêmio grátis",
    "resgate seu prêmio", "benefício liberado",
    "você tem direito", "saque seu dinheiro",

    # Falso funcionário
    "falso funcionário", "central de segurança",
    "central de atendimento", "suporte técnico",
    "motoboy", "buscar seu cartão", "entregar o cartão",

    # Compartilhamento de dados
    "confirme seu cpf", "informe seu cpf",
    "dados bancários", "dados do cartão",
    "atualização cadastral", "recadastramento",

    # WhatsApp
    "whatsapp clonado", "clonaram seu whatsapp",
    "seu whatsapp será", "whatsapp será bloqueado",
]

# Palavras-chave de MÉDIO risco — merece atenção, mas não é necessariamente golpe
MEDIUM_RISK_KEYWORDS: list[str] = [
    "atualize", "atualização", "atualizar",
    "promoção", "promocional", "desconto exclusivo",
    "desconto imperdível", "últimas unidades",
    "só hoje", "aproveite", "não perca",
    "verificação", "verificar", "confirme",
    "confirmar", "validação", "validar",
    "sorteio", "sorteado", "concorra",
    "grátis", "liberado", "disponível",
    "pendente", "regularizar",
    "troquei de número", "número novo",
    "meu número mudou", "salva meu número",
]

# Padrões de regex para ALTO risco
HIGH_RISK_PATTERNS: list[re.Pattern] = [
    # Links encurtados
    re.compile(r"bit\.ly/\S+", re.IGNORECASE),
    re.compile(r"tinyurl\.com/\S+", re.IGNORECASE),
    re.compile(r"encurtador\.\S+", re.IGNORECASE),
    re.compile(r"is\.gd/\S+", re.IGNORECASE),
    re.compile(r"ow\.ly/\S+", re.IGNORECASE),
    re.compile(r"goo\.gl/\S+", re.IGNORECASE),
    re.compile(r"encurta\.\S+", re.IGNORECASE),

    # URLs suspeitas com termos bancários falsos
    re.compile(r"https?://(?!.*\.gov\.br)(?!.*\.com\.br).*banco.*\.(xyz|tk|ml|ga|cf|gq|top|click|site|online|live)", re.IGNORECASE),
    re.compile(r"https?://.*itau(?!.*\.com\.br).*\.(xyz|tk|ml|ga|cf|gq|top|click|site|online|live)", re.IGNORECASE),
    re.compile(r"https?://.*bradesco(?!.*\.com\.br).*\.(xyz|tk|ml|ga|cf|gq|top|click|site|online|live)", re.IGNORECASE),
    re.compile(r"https?://.*nubank(?!.*\.com\.br).*\.(xyz|tk|ml|ga|cf|gq|top|click|site|online|live)", re.IGNORECASE),
    re.compile(r"https?://.*caixa(?!.*\.gov\.br).*\.(xyz|tk|ml|ga|cf|gq|top|click|site|online|live)", re.IGNORECASE),
    re.compile(r"https?://.*santander(?!.*\.com\.br).*\.(xyz|tk|ml|ga|cf|gq|top|click|site|online|live)", re.IGNORECASE),

    # Pedidos de Pix com valor (padrão "pix de R$ X" ou "pix no valor de")
    re.compile(r"pix\s+(de|no valor de)\s+r?\$\s*\d+", re.IGNORECASE),
    re.compile(r"fa(ç|z)\w*\s+(um\s+)?pix\s+(de\s+)?r?\$\s*\d+", re.IGNORECASE),

    # Pedido de código de 4-6 dígitos (código de verificação)
    re.compile(r"(código|codigo|token|senha)\s.*\d{4,6}", re.IGNORECASE),
    re.compile(r"(?:recebeu|chegou|enviei|mandei|vou enviar)\s.*c[óo]digo", re.IGNORECASE),

    # CPF (formato xxx.xxx.xxx-xx)
    re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}"),

    # Dados de cartão (16 dígitos)
    re.compile(r"\d{4}\s?\d{4}\s?\d{4}\s?\d{4}"),
]

# Padrões de regex para MÉDIO risco
MEDIUM_RISK_PATTERNS: list[re.Pattern] = [
    # Links genéricos em mensagens (potencialmente phishing)
    re.compile(r"https?://\S+", re.IGNORECASE),
]

# Dados sensíveis que o usuário nunca deve enviar
SENSITIVE_DATA_PATTERNS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}"), "CPF"),
    (re.compile(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}"), "CNPJ"),
    (re.compile(r"\d{4}\s?\d{4}\s?\d{4}\s?\d{4}"), "número de cartão"),
    (re.compile(r"(?:senha|password|passwd)\s*[:=]\s*\S+", re.IGNORECASE), "senha"),
    (re.compile(r"código\s+(?:de\s+)?segurança\s*[:=]?\s*\d{3,4}", re.IGNORECASE), "código de segurança"),
    (re.compile(r"agência\s*\d{4}", re.IGNORECASE), "dados bancários"),
    (re.compile(r"conta\s*(?:corrente|poupança)?\s*\d{4,8}-\d", re.IGNORECASE), "dados bancários"),
]
