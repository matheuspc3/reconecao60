"""Handler conversacional principal do reconecao60.

Processa toda mensagem de texto do usuario:
1. Verifica dados sensiveis (CPF, senha, etc.) → alerta
2. Classifica o risco da mensagem (alto/medio/baixo)
3. Identifica a intencao (topico, saudacao, ajuda, etc.)
4. Responde de forma conversacional e acolhedora
"""

from __future__ import annotations

from telegram import Update
from telegram.ext import ContextTypes

from analysis.classifier import classify_message
from analysis.intents import IntentResult, match_intent
from content.responses import (
    FALLBACK_CONVERSATIONAL,
    GOODBYE_RESPONSE,
    GREETING_RESPONSE,
    HOW_ARE_YOU_RESPONSE,
    POST_SCAM_SUPPORT,
    SENSITIVE_DATA_WARNING,
    THANKS_RESPONSE,
)
from content.topics import TOPICS
from handlers.menu import build_menu_keyboard
from utils.sanitize import has_sensitive_data


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler principal de conversa — processa qualquer mensagem de texto.

    Args:
        update: O update do Telegram.
        context: O contexto do handler.
    """
    text = update.message.text.strip()

    # ---------------------------------------------------------------
    # PASSO 1: Verificar dados sensiveis
    # ---------------------------------------------------------------
    has_sensitive, found_types = has_sensitive_data(text)

    if has_sensitive:
        types_str = ", ".join(found_types)
        warning_message = (
            f"⚠️ Encontrei informacoes pessoais na sua mensagem ({types_str}).\n\n"
            f"{SENSITIVE_DATA_WARNING}"
        )
        await update.message.reply_text(warning_message)
        return

    # ---------------------------------------------------------------
    # PASSO 2: Classificar risco
    # ---------------------------------------------------------------
    risk_result = classify_message(text)

    # ---------------------------------------------------------------
    # PASSO 3: Identificar intencao
    # ---------------------------------------------------------------
    intent_result = match_intent(text)

    # ---------------------------------------------------------------
    # PASSO 4: Montar resposta conversacional
    # ---------------------------------------------------------------
    response = _build_conversational_response(text, risk_result, intent_result)

    # Se a resposta for muito longa e o risco for alto, adiciona o menu
    # para facilitar navegacao. Senao, resposta pura.
    if risk_result.risk_level in ("high", "medium") or intent_result.intent == "unknown":
        keyboard = build_menu_keyboard()
    else:
        keyboard = None

    await update.message.reply_text(response, reply_markup=keyboard)


def _build_conversational_response(
    text: str,
    risk: "RiskResult",  # type: ignore[name-defined]
    intent: IntentResult,
) -> str:
    """Monta a resposta conversacional combinando risco + intencao.

    Args:
        text: Texto original do usuario.
        risk: Resultado da classificacao de risco.
        intent: Resultado do matching de intencao.

    Returns:
        A mensagem de resposta formatada.
    """
    # --- Caso 1: Mensagem de alto risco sendo compartilhada ---
    if risk.risk_level == "high":
        return _respond_high_risk(risk)

    # --- Caso 2: Usuario caiu em golpe ---
    if intent.intent == "post_scam":
        return POST_SCAM_SUPPORT

    # --- Caso 3: Usuario pediu ajuda ---
    if intent.intent == "help":
        return _respond_help()

    # --- Caso 4: Usuario perguntou sobre um topico especifico ---
    if intent.intent == "topic" and intent.topic_slug:
        return _respond_topic(intent, risk)

    # --- Caso 5: Mensagem de medio risco ---
    if risk.risk_level == "medium":
        return _respond_medium_risk(risk, intent)

    # --- Caso 6: Usuario pediu analise de mensagem ---
    if intent.intent == "analyze_request":
        return _respond_analyze_prompt(risk)

    # --- Caso 7: Saudacao ---
    if intent.intent == "greeting":
        return GREETING_RESPONSE

    # --- Caso 8: Como vai ---
    if intent.intent == "how_are_you":
        return HOW_ARE_YOU_RESPONSE

    # --- Caso 9: Agradecimento ---
    if intent.intent == "thanks":
        return THANKS_RESPONSE

    # --- Caso 10: Despedida ---
    if intent.intent == "goodbye":
        return GOODBYE_RESPONSE

    # --- Caso 11: Fallback ---
    return _respond_fallback(text)


def _respond_high_risk(risk: "RiskResult") -> str:  # type: ignore[name-defined]
    """Resposta para mensagem com alto risco de golpe."""
    response = (
        f"{risk.level_text}\n\n"
        f"{risk.explanation}\n\n"
        f"{risk.actions}"
    )

    if risk.matched_keywords:
        sinais = ", ".join(risk.matched_keywords[:4])
        response += (
            f"\n\n🔍 Sinais que encontrei na mensagem que voce mandou: {sinais}.\n\n"
            f"💙 Voce fez bem em perguntar antes de agir! "
            f"Isso ja te protege de muitos golpes."
        )

    return response


def _respond_medium_risk(risk: "RiskResult", intent: IntentResult) -> str:  # type: ignore[name-defined]
    """Resposta para mensagem com medio risco."""
    response = (
        f"{risk.level_text}\n\n"
        f"{risk.explanation}\n\n"
        f"{risk.actions}"
    )
    return response


def _respond_topic(intent: IntentResult, risk: "RiskResult") -> str:  # type: ignore[name-defined]
    """Responde com o conteudo do topico em tom conversacional."""
    topic = TOPICS.get(intent.topic_slug)
    if not topic:
        return _respond_fallback("")

    # Abertura conversacional — varia conforme o topico
    openings = {
        "falso-parente": "Entendo sua preocupacao! Isso que voce descreveu parece o golpe do falso parente, que infelizmente e muito comun no WhatsApp.",
        "clonagem-whatsapp": "Que situacao dificil! Vou te explicar sobre clonagem de WhatsApp e como se proteger.",
        "golpes-pix": "O Pix e muito pratico, mas os golpistas se aproveitam da rapidez dele. Vou te explicar como se proteger.",
        "falso-funcionario-banco": "Isso e muito importante! Golpistas adoram se passar por funcionarios de banco. Vou te explicar como identificar.",
        "links-falsos": "Otima pergunta! Links falsos sao uma das principais armadilhas. Vou te ensinar a reconhecer.",
        "boleto-falso": "Boleto falso e um golpe muito comum. Vou te ajudar a identificar antes de pagar.",
        "seguranca-banco-digital": "Cuidar da seguranca do banco no celular e essencial. Vou te explicar os cuidados principais.",
        "senhas-seguras": "Senhas fortes sao a primeira linha de defesa! Vou te ensinar a criar senhas seguras.",
    }

    opening = openings.get(intent.topic_slug,
        f"Vou te explicar sobre {topic['title'].lower()}.")

    response = (
        f"{opening}\n\n"
        f"📖 {topic['what']}\n\n"
        f"🔍 Como identificar:\n{topic['identify']}\n\n"
        f"🛡️ Como se proteger:\n{topic['protect']}"
    )

    # Fechamento acolhedor se o topico for sobre golpe
    if any(kw in intent.topic_slug for kw in ["falso", "golpe", "clonagem", "falsos", "suspeitas"]):
        response += (
            f"\n\n💙 Espero ter ajudado! Se tiver mais duvidas, "
            f"e so perguntar. Estou aqui para isso."
        )

    return response


def _respond_help() -> str:
    """Resposta quando o usuario pede ajuda generica."""
    from analysis.intents import get_topic_suggestions

    return (
        "Claro, estou aqui para ajudar! 🤗\n\n"
        "Voce pode me perguntar sobre qualquer um destes temas:\n\n"
        f"{get_topic_suggestions()}\n\n"
        "Tambem pode me enviar uma mensagem que recebeu e eu "
        "te ajudo a verificar se parece golpe.\n\n"
        "E so escrever sua duvida do seu jeito. "
        "Nao precisa usar palavras tecnicas! 💙"
    )


def _respond_analyze_prompt(risk: "RiskResult") -> str:  # type: ignore[name-defined]
    """Resposta quando o usuario parece pedir analise mas a mensagem tem baixo risco."""
    return (
        "Pode me enviar o texto da mensagem suspeita que voce recebeu! 📋\n\n"
        "Mas antes, por favor, apague qualquer dado pessoal como:\n"
        "• Nome completo\n"
        "• CPF\n"
        "• Numero de conta ou cartao\n"
        "• Senha\n"
        "• Endereco\n\n"
        "Depois e so colar aqui que eu analiso para voce."
    )


def _respond_fallback(text: str) -> str:
    """Resposta quando nenhuma intencao clara foi identificada."""
    from analysis.intents import get_topic_suggestions

    if len(text) < 3:
        return (
            "Nao entendi muito bem. 😊\n\n"
            "Voce pode me perguntar coisas como:\n\n"
            f"{get_topic_suggestions()}\n\n"
            "Ou pode me enviar uma mensagem suspeita que recebeu "
            "para eu analisar. E so escrever do seu jeito!"
        )

    return FALLBACK_CONVERSATIONAL
