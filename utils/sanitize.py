"""Função para detectar dados sensíveis em mensagens do usuário."""

from __future__ import annotations

from analysis.patterns import SENSITIVE_DATA_PATTERNS


def has_sensitive_data(text: str) -> tuple[bool, list[str]]:
    """Verifica se uma mensagem contém dados pessoais sensíveis.

    Args:
        text: O texto da mensagem a ser verificada.

    Returns:
        Uma tupla (tem_dados_sensiveis, lista_de_tipos_encontrados).
        Exemplo: (True, ["CPF", "número de cartão"])
    """
    found_types: list[str] = []

    for pattern, data_type in SENSITIVE_DATA_PATTERNS:
        if pattern.search(text):
            if data_type not in found_types:
                found_types.append(data_type)

    return len(found_types) > 0, found_types
