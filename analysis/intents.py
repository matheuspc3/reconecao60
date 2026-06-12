"""Mapeamento de intencoes conversacionais do reconecao60.

Para cada topico, mapeamos palavras-chave e frases que uma pessoa
idosa usaria naturalmente ao perguntar sobre aquele assunto.

Tambem detecta intencoes gerais: saudacao, agradecimento, pedido de ajuda,
relato de golpe sofrido, e pedido de analise de mensagem suspeita.
"""

from __future__ import annotations

from dataclasses import dataclass, field


# --- Palavras-chave por topico ---
# Cada entrada mapeia palavras/frases naturais para o slug do topico

TOPIC_KEYWORDS: dict[str, list[str]] = {
    "falso-parente": [
        # Relacoes familiares
        "filho", "filha", "filhos", "neto", "neta", "netos",
        "sobrinho", "sobrinha", "primo", "prima",
        "irmao", "irma", "mae", "pai", "avo", "avo",
        "parente", "familiar", "familia",
        # Situacao do golpe
        "disse que era", "dizendo que era", "falando que era",
        "se passando por", "fingindo ser", "fingiu ser",
        "pediu dinheiro", "pedindo dinheiro", "pediu pix",
        "pedindo pix", "precisando de dinheiro", "precisa de dinheiro",
        "numero novo", "numero diferente", "outro numero",
        "nao era ele", "nao era ela", "nao era meu",
        "era golpe", "golpista", "falso", "falsa",
        "emergencia", "hospital", "acidente",
        "troquei de numero", "trocou de numero",
        "mudou de numero", "meu numero novo",
        "nao atende", "nao quer atender", "nao atendeu",
        # Emocional
        "preocupado", "preocupada", "medo", "assustado",
    ],
    "clonagem-whatsapp": [
        "clonaram", "clonado", "clonagem", "clonou",
        "whatsapp clonado", "whatsapp foi clonado",
        "meu whatsapp", "whatsapp foi hackeado",
        "hackearam", "invadiram meu whatsapp",
        "codigo do whatsapp", "codigo de verificacao",
        "codigo de seis", "codigo de 6",
        "pediu codigo", "pediu o codigo", "enviar codigo",
        "sms", "mensagem de texto", "codigo por sms",
        "verificacao em duas etapas", "autenticacao",
        "nao consigo entrar", "whatsapp parou",
        "whatsapp bloqueado", "whatsapp desativado",
        "conta do whatsapp", "recuperar whatsapp",
        "entraram no meu whatsapp", "acessaram meu whatsapp",
        "leram minhas mensagens", "mandaram mensagem como se fosse eu",
    ],
    "troquei-de-numero": [
        "troquei de numero", "trocou de numero",
        "mudou de numero", "meu numero novo",
        "salva meu numero", "salve meu numero",
        "apaga o numero antigo", "apague o numero",
        "numero mudou", "numero novo",
        "whatsapp novo", "celular novo", "chip novo",
    ],
    "codigo-verificacao": [
        "codigo", "codigo de seguranca", "codigo de confirmacao",
        "codigo enviado", "codigo recebido", "recebi um codigo",
        "chegou um codigo", "mandaram um codigo",
        "token", "token de seguranca",
        "autenticacao", "confirmacao",
        "sms com codigo", "mensagem com codigo",
        "codigo que chegou", "codigo do banco",
    ],
    "falso-funcionario-banco": [
        "funcionario do banco", "funcionaria do banco",
        "gerente", "atendente do banco",
        "banco ligou", "banco mandou", "banco enviou",
        "ligacao do banco", "ligou dizendo que era do banco",
        "motoboy", "moto boy", "buscar cartao", "buscar o cartao",
        "entregar o cartao", "buscar seu cartao",
        "trocar o cartao", "trocar cartao",
        "cartao clonado", "cartao bloqueado",
        "compra suspeita", "compra nao reconhecida",
        "atualizar dados", "atualizar cadastro",
        "aplicativo do banco", "app do banco", "instalar app",
        "acesso remoto", "acessar meu celular",
        "conta bloqueada", "conta invadida",
        "digitar senha no telefone", "passar senha",
        "falar a senha", "pediu minha senha",
    ],
    "golpes-pix": [
        "pix", "fazer um pix", "faça um pix", "fiz um pix",
        "transferencia", "transferir", "transferi",
        "pix errado", "pix por engano", "pix enganado",
        "devolver pix", "devolucao de pix", "recebi um pix",
        "comprovante de pix", "comprovante falso",
        "pix agendado", "pix nao caiu",
        "pediu pix", "pedindo pix", "cobrando pix",
        "pagamento urgente", "pagamento imediato",
        "pix para receber", "taxa para liberar",
        "pix falso", "golpe do pix",
    ],
    "golpes-whatsapp": [
        "whatsapp", "zap", "whats", "whats zap",
        "mensagem suspeita no whatsapp", "mensagem estranha no zap",
        "golpe pelo whatsapp", "fraude no whatsapp",
        "recebi no whatsapp", "mandaram no whatsapp",
        "grupo de whatsapp", "grupo do zap",
        "contato desconhecido", "numero desconhecido",
        "nao conheco", "quem e essa pessoa",
    ],
    "links-falsos": [
        "link", "links", "clicar", "cliquei", "clique",
        "abrir o link", "abri o link", "acessar o link",
        "site", "sites", "pagina", "endereco",
        "endereco da internet", "url",
        "link que recebi", "link enviado", "mandaram link",
        "bit ly", "encurtador", "link estranho",
        "link suspeito", "link perigoso", "link falso",
        "site falso", "site suspeito", "pagina falsa",
        "cliquei e abriu", "cliquei sem querer",
        "nao sei se posso clicar", "devo clicar",
        "e seguro clicar", "posso clicar",
    ],
    "site-falso": [
        "site", "sites", "site do banco", "site da loja",
        "site falso", "site suspeito", "site estranho",
        "pagina da internet", "pagina falsa",
        "loja online", "loja virtual", "loja na internet",
        "cadeado", "cadeado de seguranca", "https",
        "site seguro", "site nao seguro",
        "comprei em um site", "comprei pela internet",
        "site nao entregou", "site sumiu",
    ],
    "ligacoes-suspeitas": [
        "ligacao", "ligacoes", "ligaram", "ligou",
        "telefonema", "telefone", "celular tocou",
        "numero estranho", "numero desconhecido",
        "nao conheco o numero", "quem ligou",
        "ligacao suspeita", "ligacao estranha",
        "ameaca por telefone", "ameacaram",
        "sequestro", "sequestraram", "falso sequestro",
        "voz robotica", "gravacao",
        "desliguei", "nao atendi", "devo atender",
        "ligaram de madrugada", "ligaram varias vezes",
        "chamada de video", "videochamada suspeita",
    ],
    "seguranca-banco-digital": [
        "banco", "banco digital", "aplicativo do banco",
        "app banco", "app do banco", "conta bancaria",
        "conta corrente", "poupanca", "conta digital",
        "nubank", "caixa", "bradesco", "itau", "santander",
        "banco do brasil", "bb", "inter", "picpay",
        "extrato", "saldo", "movimentacao",
        "cartao de credito", "cartao de debito",
        "biometria", "impressao digital", "reconhecimento facial",
        "perdi o celular", "roubaram meu celular",
        "celular foi roubado", "celular perdido",
        "compras nao reconhecidas", "compra que nao fiz",
        "limite de transferencia", "limite de pix",
    ],
    "boleto-falso": [
        "boleto", "boletos", "conta para pagar",
        "pagar boleto", "paguei boleto", "boleta",
        "codigo de barras", "codigo de barra",
        "vencimento", "data de vencimento",
        "conta de luz", "conta de agua", "conta de internet",
        "conta de telefone", "fatura", "mensalidade",
        "iptu", "ipva", "imposto", "taxa",
        "boleto do governo", "boleto da receita",
        "beneficiario", "nome do beneficiario",
        "valor diferente", "valor errado",
        "banco diferente no boleto",
    ],
    "promocoes-falsas": [
        "promocao", "promocoes", "oferta", "ofertas",
        "desconto", "sorteio", "sorteado", "sorteada",
        "premio", "premios", "ganhei", "ganhou",
        "gratis", "de graca", "cupom", "cupons",
        "promocao imperdivel", "ultimas unidades",
        "so hoje", "aproveite", "promocao relampago",
        "black friday", "liquida", "queima de estoque",
        "ganhou um premio", "voce foi sorteado",
        "beneficio", "beneficio do governo",
        "vale compras", "vale presente",
        "muito barato", "preco muito baixo",
        "boa demais para ser verdade", "bom demais",
    ],
    "falso-suporte": [
        "suporte", "suporte tecnico", "tecnico",
        "central de atendimento", "central de suporte",
        "suporte da microsoft", "suporte do windows",
        "suporte do google", "suporte da apple",
        "suporte da operadora", "operadora de telefone",
        "vivo", "claro", "tim", "oi",
        "acesso remoto", "teamviewer", "anydesk",
        "instalar programa", "instalar aplicativo",
        "virus no celular", "virus no computador",
        "seu aparelho tem virus", "seu computador infectado",
        "limpeza de virus", "remover virus",
    ],
    "golpe-maquininha": [
        "maquininha", "maquininha de cartao",
        "maquina de cartao", "pagamento na maquina",
        "pagar com cartao", "passar cartao",
        "pagamento por aproximacao", "aproximacao",
        "digitar senha", "senha na maquininha",
        "visor quebrado", "visor apagado",
        "valor diferente", "valor errado na maquina",
        "entregador", "entrega", "ifood", "rappi",
        "passou o cartao duas vezes", "passou de novo",
        "nao funcionou", "erro na maquininha",
        "trocou a maquininha", "maquininha diferente",
        "meu cartao foi trocado", "trocaram meu cartao",
    ],
    "compras-internet": [
        "compra", "compras", "comprei", "comprou",
        "loja online", "loja virtual", "site de compras",
        "mercado livre", "amazon", "shopee", "magalu",
        "americanas", "casas bahia", "ponto frio",
        "produto nao chegou", "nao entregaram",
        "produto errado", "produto diferente",
        "nao recebi", "nunca chegou",
        "cartao virtual", "cartao temporario",
        "comprar na internet", "compra segura",
        "reclamacao", "reclame aqui", "direito do consumidor",
        "cnpj", "empresa confiavel", "loja confiavel",
    ],
    "urgencia-medo": [
        "urgencia", "urgente", "corre", "rapido", "agora",
        "medo", "medo de perder", "com medo", "amedrontado",
        "pressao", "pressionado", "pressionada",
        "ameaca", "ameacando", "ameacou",
        "consequencia", "vai bloquear", "vai cancelar",
        "vai suspender", "processado", "processo",
        "nao posso contar", "nao conte para ninguem",
        "segredo", "e confidencial",
        "nao deixou eu desligar", "nao deixou eu pensar",
        "tive medo e fiz", "fiz com medo",
        "agir sem pensar", "fiz por impulso",
    ],
    "redes-sociais": [
        "facebook", "instagram", "tiktok", "youtube",
        "rede social", "redes sociais",
        "perfil", "perfis", "amigo", "amizade",
        "solicitacao de amizade", "pedido de amizade",
        "perfil falso", "perfil fake", "conta falsa",
        "foto de perfil", "fotos minhas",
        "postagem", "post", "publicacao",
        "compartilhar", "curtir", "comentar",
        "privacidade", "perfil privado", "conta privada",
        "marcaram voce", "te marcaram",
        "mensagem no facebook", "mensagem no instagram",
    ],
    "golpes-sms": [
        "sms", "mensagem de texto", "torpedo",
        "mensagem no celular", "mensagem recebida",
        "sms suspeito", "sms estranho",
        "sms do banco", "sms de entrega",
        "sms de confirmacao", "sms com link",
        "codigo por sms", "senha por sms",
        "sms falso", "sms golpe",
    ],
    "senhas-seguras": [
        "senha", "senhas", "password",
        "senha fraca", "senha forte", "senha facil",
        "criar senha", "criar uma senha", "como fazer senha",
        "minha senha", "minhas senhas", "esqueci a senha",
        "trocar senha", "mudar senha", "alterar senha",
        "senha igual", "mesma senha", "senha diferente",
        "anotar senha", "onde guardar senha",
        "senha com data", "senha com nome",
        "123456", "senha simples",
        "senha segura", "senha confiavel",
        "caderno de senhas",
    ],
    "verificacao-duas-etapas": [
        "verificacao em duas etapas", "duas etapas",
        "dois fatores", "autenticacao de dois fatores",
        "protecao extra", "camada extra",
        "codigo extra", "confirmacao extra",
        "ativar duas etapas", "como ativar",
        "seguranca extra", "proteger conta",
        "recuperar conta", "email de recuperacao",
        "codigos de backup", "codigo reserva",
    ],
    "virus-celular": [
        "virus", "virus no celular", "virus no computador",
        "celular lento", "celular travando",
        "bateria acaba rapido", "bateria descarregando",
        "anuncios", "anuncio", "propaganda",
        "anuncios estranhos", "anuncio que nao sai",
        "aplicativo estranho", "app estranho",
        "app que nao instalei", "aplicativo que nao baixei",
        "aplicativos sozinhos", "apps abrindo sozinhos",
        "celular esquentando", "celular quente",
        "antivirus", "antivirus no celular",
        "limpar virus", "remover virus",
        "proteger celular", "celular infectado",
    ],
    "dicas-gerais": [
        "dicas", "dicas de seguranca", "seguranca",
        "como se proteger", "como evitar golpe",
        "protecao", "prevencao", "prevenir",
        "seguro", "seguranca na internet",
        "seguranca digital", "cuidados",
        "cuidados basicos", "o basico",
        "primeiros passos", "por onde comeco",
        "nao sei nada", "sou leigo", "sou leiga",
        "pouca experiencia", "nao entendo",
        "aprender", "quero aprender", "me ensina",
        "idoso", "idosa", "terceira idade",
    ],
}


# --- Intencoes gerais (nao topicos especificos) ---

GENERAL_INTENTS: dict[str, list[str]] = {
    "greeting": [
        "oi", "ola", "oie", "oi tudo bem", "ola tudo bem",
        "bom dia", "boa tarde", "boa noite",
        "e ai", "ei", "hello", "hi",
    ],
    "thanks": [
        "obrigado", "obrigada", "obrigado mesmo", "obrigada mesmo",
        "muito obrigado", "muito obrigada",
        "valeu", "brigado", "brigada",
        "obrigado pela ajuda", "obrigada pela ajuda",
        "gratidao", "agradeco", "te agradeco",
        "ajudou muito", "me ajudou", "obrigado viu",
    ],
    "help": [
        "ajuda", "me ajuda", "me ajude", "me ajudem",
        "socorro", "preciso de ajuda", "preciso ajuda",
        "nao sei", "nao sei o que fazer", "nao sei o que faço",
        "estou perdido", "estou perdida",
        "o que eu faço", "o que fazer", "o que devo fazer",
        "como faz", "como funciona", "como eu uso",
        "me explica", "explica", "me orienta",
        "nao entendo", "nao entendi", "nao compreendo",
        "pode me ajudar", "pode ajudar",
    ],
    "post_scam": [
        "cai em um golpe", "cai em golpe", "cai num golpe",
        "fui enganado", "fui enganada", "me enganaram",
        "fui vitima", "fui vitima de golpe",
        "paguei", "paguei o boleto", "paguei e era golpe",
        "fiz o pix", "fiz um pix", "fiz a transferencia",
        "enviei dinheiro", "mandei dinheiro", "transferi",
        "perdi dinheiro", "perdi um dinheiro", "perdi tudo",
        "fui assaltado", "fui roubado", "me roubaram",
        "fui hackeado", "hackearam", "invadiram",
        "cai no golpe", "cair em golpe",
        "era golpe", "era um golpe", "descobri que era golpe",
        "ja cai", "aconteceu comigo", "aconteceu isso",
        "o que fazer depois", "como recuperar", "tem como recuperar",
    ],
    "analyze_request": [
        "recebi essa mensagem", "recebi isso", "recebi essa",
        "olha essa mensagem", "olha isso", "olha so",
        "ve essa mensagem", "ve isso", "veja isso",
        "e golpe", "e golpe?", "sera que e golpe",
        "isso e golpe", "isso e verdade", "isso e real",
        "e confiavel", "e seguro", "e verdade",
        "sera que e verdade", "sera que e golpe",
        "pode ser golpe", "parece golpe",
        "me mandaram isso", "enviaram isso", "chegou essa mensagem",
        "recebi um email", "recebi um sms", "recebi por email",
        "verificar se e golpe", "confere se e golpe",
        "analisa isso", "da uma olhada",
        "desconfiei", "achei estranho", "achei suspeito",
        "estranho", "suspeito", "nao sei se e golpe",
        "recebi uma ligacao", "ligaram para mim",
        "to em duvida", "estou em duvida", "estou na duvida",
        "nao tenho certeza",
    ],
    "goodbye": [
        "tchau", "xau", "ate mais", "ate logo", "ate breve",
        "adeus", "falou", "flw", "fui",
        "vou indo", "vou nessa", "ate depois",
    ],
    "how_are_you": [
        "como vai", "como voce esta", "como voce ta",
        "tudo bem", "tudo bom", "tudo certo",
        "como esta", "como ta", "joia",
        "bem e voce", "tudo bem e voce",
    ],
}


@dataclass
class IntentResult:
    """Resultado do matching de intencao."""

    intent: str  # "topic", "greeting", "thanks", "help", "post_scam", "analyze_request", "goodbye", "how_are_you", "unknown"
    topic_slug: str = ""  # Preenchido apenas se intent == "topic"
    topic_title: str = ""  # Preenchido apenas se intent == "topic"
    score: int = 0  # Quantidade de keywords que deram match
    matched_keywords: list[str] = field(default_factory=list)


def match_intent(text: str) -> IntentResult:
    """Analisa o texto do usuario e identifica a intencao.

    A prioridade eh:
    1. Intencoes especificas (help, post_scam) — alto sinal
    2. Topicos — por quantidade de matches
    3. Intencoes leves (greeting, thanks, goodbye, how_are_you)

    Args:
        text: O texto da mensagem do usuario.

    Returns:
        Um IntentResult com a intencao identificada.
    """
    text_lower = text.lower().strip()

    # Primeiro verifica intencoes com alto sinal (help, post_scam)
    for keyword in GENERAL_INTENTS["help"]:
        if keyword in text_lower:
            return IntentResult(
                intent="help",
                matched_keywords=[keyword],
            )

    for keyword in GENERAL_INTENTS["post_scam"]:
        if keyword in text_lower:
            matched = [keyword]
            # Procura mais matches para dar contexto
            for kw2 in GENERAL_INTENTS["post_scam"]:
                if kw2 != keyword and kw2 in text_lower:
                    matched.append(kw2)
            return IntentResult(
                intent="post_scam",
                score=len(matched),
                matched_keywords=matched,
            )

    # Verifica topicos — acumula score por topico
    best_topic = ""
    best_score = 0
    best_keywords: list[str] = []

    for slug, keywords in TOPIC_KEYWORDS.items():
        score = 0
        matched: list[str] = []
        for keyword in keywords:
            if keyword in text_lower:
                score += 1
                matched.append(keyword)
        if score > best_score:
            best_score = score
            best_topic = slug
            best_keywords = matched

    # Se encontrou topico com score razoavel (>=2 keywords ou keyword muito especifica)
    if best_score >= 2 or (best_score >= 1 and len(text_lower.split()) <= 5):
        from content.topics import TOPICS
        topic_info = TOPICS.get(best_topic, {})
        return IntentResult(
            intent="topic",
            topic_slug=best_topic,
            topic_title=topic_info.get("title", ""),
            score=best_score,
            matched_keywords=best_keywords,
        )

    # Se teve match de topico mas fraco, ainda retorna como topico com score baixo
    if best_score >= 1:
        from content.topics import TOPICS
        topic_info = TOPICS.get(best_topic, {})
        return IntentResult(
            intent="topic",
            topic_slug=best_topic,
            topic_title=topic_info.get("title", ""),
            score=best_score,
            matched_keywords=best_keywords,
        )

    # Verifica analyze_request
    for keyword in GENERAL_INTENTS["analyze_request"]:
        if keyword in text_lower:
            return IntentResult(
                intent="analyze_request",
                matched_keywords=[keyword],
            )

    # Verifica intencoes leves
    for keyword in GENERAL_INTENTS["greeting"]:
        if keyword == text_lower or (len(text_lower.split()) <= 3 and keyword in text_lower):
            return IntentResult(
                intent="greeting",
                matched_keywords=[keyword],
            )

    for keyword in GENERAL_INTENTS["thanks"]:
        if keyword in text_lower:
            return IntentResult(
                intent="thanks",
                matched_keywords=[keyword],
            )

    for keyword in GENERAL_INTENTS["goodbye"]:
        if keyword in text_lower:
            return IntentResult(
                intent="goodbye",
                matched_keywords=[keyword],
            )

    for keyword in GENERAL_INTENTS["how_are_you"]:
        if keyword in text_lower:
            return IntentResult(
                intent="how_are_you",
                matched_keywords=[keyword],
            )

    # Nenhuma intencao identificada
    return IntentResult(intent="unknown")


def get_topic_suggestions() -> str:
    """Retorna uma lista de sugestoes de topicos para o usuario perguntar."""
    suggestions = [
        "Golpes no WhatsApp",
        "Golpes do Pix",
        "Falso parente pedindo dinheiro",
        "Clonagem de WhatsApp",
        "Links falsos e sites suspeitos",
        "Falso funcionario de banco",
        "Boleto falso",
        "Promocoes falsas",
        "Compras pela internet",
        "Ligacoes suspeitas",
        "Senhas seguras",
        "Verificacao em duas etapas",
        "Virus no celular",
        "Cuidados com redes sociais",
        "Golpes com urgencia ou medo",
    ]
    return "\n".join(f"• {s}" for s in suggestions)
