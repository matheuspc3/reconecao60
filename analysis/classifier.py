"""Classificador de risco de mensagens suspeitas.

Analisa uma mensagem de texto e retorna o nível de risco
(baixo, médio, alto) com explicação e ações recomendadas.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from analysis.patterns import (
    HIGH_RISK_KEYWORDS,
    HIGH_RISK_PATTERNS,
    MEDIUM_RISK_KEYWORDS,
    MEDIUM_RISK_PATTERNS,
)

# Respostas por nível de risco
RISK_RESPONSES: dict[str, dict[str, str]] = {
    "high": {
        "level": "🔴 ALTO RISCO — Pode ser golpe!",
        "explanation": (
            "Essa mensagem tem vários sinais de golpe. "
            "Os golpistas usam esse tipo de mensagem para enganar pessoas "
            "e conseguir dinheiro ou dados pessoais."
        ),
        "actions": (
            "✅ O que fazer agora:\n\n"
            "• NÃO clique em nenhum link.\n"
            "• NÃO responda à mensagem.\n"
            "• NÃO envie dinheiro ou faça Pix.\n"
            "• NÃO compartilhe códigos ou senhas.\n"
            "• Bloqueie o contato que enviou a mensagem.\n"
            "• Se for sobre banco, abra apenas o aplicativo oficial.\n"
            "• Ligue para a empresa ou pessoa usando um número oficial.\n"
            "• Converse com alguém de confiança antes de fazer qualquer coisa."
        ),
    },
    "medium": {
        "level": "🟡 MÉDIO RISCO — Preste atenção!",
        "explanation": (
            "Essa mensagem tem alguns sinais que merecem cuidado. "
            "Pode ser algo normal, mas também pode ser tentativa de golpe. "
            "É melhor confirmar antes de fazer qualquer coisa."
        ),
        "actions": (
            "✅ O que fazer agora:\n\n"
            "• Não clique em links sem antes verificar.\n"
            "• Confirme a informação por outro canal.\n"
            "• Se for promoção, veja o site oficial da loja.\n"
            "• Se for de banco, abra o app oficial, não use links.\n"
            "• Se for conhecido pedindo dinheiro, ligue para confirmar.\n"
            "• Na dúvida, não faça nada agora. Espere e confirme."
        ),
    },
    "low": {
        "level": "🟢 BAIXO RISCO — Parece tranquilo, mas sempre com atenção.",
        "explanation": (
            "Não encontrei sinais claros de golpe nesta mensagem. "
            "Mas lembre-se: é sempre bom manter a atenção e seguir "
            "as dicas de segurança no dia a dia."
        ),
        "actions": (
            "✅ Lembre-se sempre:\n\n"
            "• Não compartilhe senhas ou códigos.\n"
            "• Não faça Pix por pressa ou medo.\n"
            "• Confirme pedidos de dinheiro por ligação.\n"
            "• Desconfie de ofertas boas demais.\n"
            "• Mantenha seu celular atualizado.\n\n"
            "Se quiser aprender mais sobre algum tema específico, "
            "é só escolher no menu abaixo."
        ),
    },
}


@dataclass
class RiskResult:
    """Resultado da análise de risco de uma mensagem."""

    risk_level: str  # "high", "medium", "low"
    level_text: str
    explanation: str
    actions: str
    matched_keywords: list[str] = field(default_factory=list)
    matched_patterns: list[str] = field(default_factory=list)


def classify_message(text: str) -> RiskResult:
    """Analisa uma mensagem e retorna a classificação de risco.

    Args:
        text: O texto da mensagem a ser analisada.

    Returns:
        Um RiskResult com nível de risco, explicação e ações recomendadas.
    """
    text_lower = text.lower()

    matched_keywords: list[str] = []
    matched_patterns: list[str] = []

    # Verifica padrões de alto risco (regex)
    for pattern in HIGH_RISK_PATTERNS:
        match = pattern.search(text)
        if match:
            matched_patterns.append(match.group(0))

    # Verifica palavras-chave de alto risco
    for keyword in HIGH_RISK_KEYWORDS:
        if keyword.lower() in text_lower:
            matched_keywords.append(keyword)

    # Se encontrou padrões ou palavras de alto risco
    if matched_patterns or matched_keywords:
        response = RISK_RESPONSES["high"]
        return RiskResult(
            risk_level="high",
            level_text=response["level"],
            explanation=response["explanation"],
            actions=response["actions"],
            matched_keywords=matched_keywords,
            matched_patterns=matched_patterns,
        )

    # Verifica padrões de médio risco
    for pattern in MEDIUM_RISK_PATTERNS:
        match = pattern.search(text)
        if match:
            # Para links genéricos, não mostrar o link inteiro por segurança
            matched_patterns.append("link suspeito detectado")

    # Verifica palavras-chave de médio risco
    for keyword in MEDIUM_RISK_KEYWORDS:
        if keyword.lower() in text_lower:
            matched_keywords.append(keyword)

    # Se encontrou padrões ou palavras de médio risco
    if matched_patterns or matched_keywords:
        response = RISK_RESPONSES["medium"]
        return RiskResult(
            risk_level="medium",
            level_text=response["level"],
            explanation=response["explanation"],
            actions=response["actions"],
            matched_keywords=matched_keywords,
            matched_patterns=matched_patterns,
        )

    # Nenhum sinal de risco encontrado
    response = RISK_RESPONSES["low"]
    return RiskResult(
        risk_level="low",
        level_text=response["level"],
        explanation=response["explanation"],
        actions=response["actions"],
        matched_keywords=[],
        matched_patterns=[],
    )
