# reconecao60 📱🔒

Bot educativo do Telegram que ajuda pessoas idosas a aprenderem segurança digital de forma simples, paciente e respeitosa.

**Disponível em:** [t.me/reconecao60_bot](https://t.me/reconecao60_bot)

---

## Sobre o bot

O reconecao60 ensina pessoas idosas a se protegerem de golpes digitais, ajudando-as a reconhecer:

- Mensagens falsas e links perigosos
- Golpes pelo WhatsApp (falso parente, clonagem, "troquei de número")
- Golpes do Pix e falso funcionário de banco
- Boletos falsos e promoções fraudulentas
- Ligações suspeitas e golpes por SMS
- E muito mais

A interação é **conversacional**: o usuário digita sua dúvida com palavras naturais e o bot entende e responde com conteúdo educativo!

```
Usuário: "meu filho pediu dinheiro por mensagem, o que eu faço?"
Bot:     Entendo sua preocupação! Isso parece o golpe do falso parente...
         [explica o golpe, sinais de alerta e o que fazer]
```

---

## Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| 💬 **Conversa natural** | Entende perguntas em português coloquial, sem comandos complexos |
| 🎯 **23 temas educativos** | Cada tema explicado em 3 partes: o que é → como identificar → como se proteger |
| 🔍 **Análise de mensagens** | Classifica mensagens suspeitas em 3 níveis de risco (baixo/médio/alto) |
| 🛡️ **Detecção de dados sensíveis** | Alerta o usuário se ele enviar CPF, senha, cartão ou outros dados pessoais |
| 🤗 **Acolhimento pós-golpe** | Orienta com empatia quem já caiu em golpe (9 passos de ação) |
| 📋 **Menu de apoio** | Comando `/menu` com teclado inline para navegação alternativa |

---

## Arquitetura

```
reconecao60/
├── bot.py                    # Entry point — registra handlers e inicia polling
├── config.py                 # Carrega TELEGRAM_BOT_TOKEN do .env
├── requirements.txt          # python-telegram-bot, python-dotenv
├── .env.example              # Template de variáveis de ambiente
│
├── handlers/
│   ├── conversation.py       # Handler conversacional principal
│   ├── start.py              # Comando /start — boas-vindas
│   └── menu.py               # Comandos /menu, /ajuda + callbacks inline
│
├── content/
│   ├── topics.py             # Base de conhecimento — 23 temas
│   └── responses.py          # Templates de resposta (tom acolhedor)
│
├── analysis/
│   ├── intents.py            # Mapeamento de palavras-chave → intenções
│   ├── classifier.py         # Classificador de risco (alto/médio/baixo)
│   └── patterns.py           # Padrões regex e keywords para detecção
│
└── utils/
    └── sanitize.py           # Detecção de dados sensíveis (CPF, senha, etc.)
```

### Fluxo de uma mensagem

```
Mensagem do usuário
        │
        ▼
┌──────────────────────┐
│ 1. Sanitização       │  Detecta CPF, senha, cartão, etc. → alerta
├──────────────────────┤
│ 2. Classificação     │  Analisa risco da mensagem (alto/médio/baixo)
├──────────────────────┤
│ 3. Matching de      │  Identifica a intenção (tópico, ajuda, saudação...)
│    intenção          │
├──────────────────────┤
│ 4. Resposta          │  Monta resposta conversacional e acolhedora
└──────────────────────┘
```

---

## Instalação

### Pré-requisitos

- Python 3.9+
- Um token de bot do Telegram (obtenha com o [@BotFather](https://t.me/BotFather))

### Passos

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd reconecao60

# 2. Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o token do bot
cp .env.example .env
# Edite o arquivo .env e insira o token do seu bot:
# TELEGRAM_BOT_TOKEN=seu_token_aqui

# 5. Execute o bot
python bot.py
```

---

## Uso

### Comandos disponíveis

| Comando | Descrição |
|---|---|
| `/start` | Mensagem de boas-vindas |
| `/menu` | Lista de todos os temas com botões |
| `/ajuda` | Explica como conversar com o bot |

### Exemplos de conversa

```
"meu filho pediu dinheiro por WhatsApp mas não era ele"
"recebi um link dizendo que ganhei um prêmio, é verdade?"
"como faço uma senha segura?"
"caí em um golpe, perdi dinheiro, o que faço agora?"
"ligaram do banco pedindo minha senha"
"como ativar a verificação em duas etapas no WhatsApp?"
```

---

## Segurança

- O **token do Telegram** é armazenado apenas em variável de ambiente (`.env`)
- O `.env` está listado no `.gitignore` — nunca é commitado
- O bot **nunca** pede senhas, códigos ou dados pessoais
- Mensagens com dados sensíveis (CPF, cartão, etc.) são detectadas e o usuário é alertado

---

## Tecnologias

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) v20+ — framework assíncrono para bots do Telegram
- [python-dotenv](https://github.com/theskumar/python-dotenv) — carregamento de variáveis de ambiente

---

## Licença

Este projeto é software livre. Use, estude, modifique e distribua como quiser.

---

🤖 Feito com cuidado para ajudar quem mais precisa.
