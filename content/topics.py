"""Conteúdo textual de cada tema de ensino do reconecao60.

Cada tema segue o formato de 3 partes:
1. O que é o golpe
2. Como identificar
3. O que fazer para se proteger
"""

TOPICS: dict[str, dict[str, str]] = {
    "golpes-whatsapp": {
        "title": "📱 Golpes no WhatsApp",
        "what": (
            "O WhatsApp é o aplicativo de mensagens mais usado no Brasil. "
            "Por isso, os golpistas tentam enganar as pessoas por lá de várias formas.\n\n"
            "Os golpes mais comuns no WhatsApp são:\n"
            "• Falso parente pedindo dinheiro\n"
            "• Golpe do \"troquei de número\"\n"
            "• Falso funcionário de banco\n"
            "• Golpe da clonagem de WhatsApp\n"
            "• Links falsos enviados por mensagem\n"
            "• Falsas promoções e sorteios"
        ),
        "identify": (
            "⚠️ Sinais de alerta no WhatsApp:\n\n"
            "• Alguém que diz ser parente, mas usa número desconhecido.\n"
            "• Pedido de dinheiro urgente, de preferência por Pix.\n"
            "• A pessoa diz que não pode atender ligação.\n"
            "• Mensagem com muitos erros de português.\n"
            "• Foto de perfil diferente ou muito genérica.\n"
            "• Pedido de código de verificação que chegou por SMS.\n"
            "• Links para sites que você não conhece.\n"
            "• Promoções boas demais para ser verdade."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Ative a verificação em duas etapas no WhatsApp.\n"
            "• Nunca compartilhe o código de verificação do WhatsApp.\n"
            "• Desconfie de pedidos de dinheiro por mensagem.\n"
            "• Ligue para a pessoa no número antigo para confirmar.\n"
            "• Não clique em links de desconhecidos.\n"
            "• Configure a privacidade do WhatsApp:\n"
            "  - Foto de perfil: apenas contatos\n"
            "  - Status: apenas contatos\n"
            "  - Visto por último: apenas contatos"
        ),
    },
    "golpes-pix": {
        "title": "💸 Golpes do Pix",
        "what": (
            "O Pix é um meio de pagamento rápido criado pelo Banco Central. "
            "Ele é gratuito e muito útil, mas os golpistas se aproveitam da "
            "rapidez do Pix para enganar as pessoas.\n\n"
            "Principais golpes do Pix:\n"
            "• Golpe do falso parente pedindo Pix\n"
            "• Golpe do falso sequestro\n"
            "• Golpe do falso comprovante\n"
            "• Golpe da falsa venda pela internet\n"
            "• Golpe do Pix errado (devolução falsa)\n"
            "• Golpe do falso funcionário de banco"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• Alguém pede Pix com muita urgência.\n"
            "• A pessoa diz que é parente, mas você não reconhece o número.\n"
            "• Dizem que você ganhou algo, mas precisa pagar uma taxa antes.\n"
            "• Alguém manda comprovante de Pix e pede devolução.\n"
            "• Pedem Pix para liberar um prêmio ou benefício.\n"
            "• O nome do destinatário do Pix é diferente do que você esperava.\n"
            "• Prometem multiplicar seu dinheiro com Pix."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Nunca faça Pix com pressa ou por medo.\n"
            "• Confirme por ligação ou pessoalmente antes de transferir.\n"
            "• Sempre verifique o nome do destinatário antes de confirmar.\n"
            "• Desconfie de pedidos de dinheiro de números desconhecidos.\n"
            "• Use o limite de valor por transação no app do banco.\n"
            "• Se recebeu um Pix por engano, use a função de devolução do app.\n"
            "• Nunca faça Pix para receber prêmio ou benefício.\n"
            "• Se caiu em golpe, avise o banco imediatamente."
        ),
    },
    "falso-parente": {
        "title": "👨‍👩‍👧 Golpe do Falso Parente",
        "what": (
            "O golpe do falso parente acontece quando alguém manda mensagem "
            "dizendo que é filho, neto, sobrinho ou outro familiar.\n\n"
            "A pessoa geralmente diz que:\n"
            "• Trocou de número de celular\n"
            "• Está com o celular quebrado\n"
            "• Teve uma emergência e precisa de dinheiro\n"
            "• Não pode atender ligação no momento"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• Diz que está com pressa ou que é urgente.\n"
            "• Pede Pix ou transferência imediatamente.\n"
            "• Não quer ou não pode atender ligação.\n"
            "• Pede segredo — \"não conte para ninguém\".\n"
            "• Usa um número de telefone desconhecido.\n"
            "• A forma de escrever é diferente do que a pessoa costuma usar.\n"
            "• A foto de perfil parece estranha ou foi tirada da internet."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Não envie dinheiro na mesma hora.\n"
            "• Ligue para o familiar pelo número antigo.\n"
            "• Tente falar por chamada de vídeo com a pessoa.\n"
            "• Pergunte algo que só a pessoa de verdade saberia responder.\n"
            "• Fale com outro parente para confirmar a história.\n"
            "• Bloqueie o contato se confirmar que é golpe.\n"
            "• Avise outros familiares sobre a tentativa de golpe."
        ),
    },
    "trocou-de-numero": {
        "title": "📞 Golpe do \"Troquei de Número\"",
        "what": (
            "Neste golpe, o criminoso se passa por alguém que você conhece "
            "e diz que trocou de número de celular.\n\n"
            "Ele geralmente copia a foto de perfil da pessoa verdadeira e "
            "tenta se passar por ela. Depois de alguns dias de conversa, "
            "inventa uma emergência e pede dinheiro."
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• Mensagem dizendo \"Oi, troquei de número, esse é o novo\".\n"
            "• A pessoa pede para salvar o novo número.\n"
            "• Depois de alguns dias, pede dinheiro emprestado.\n"
            "• Inventa uma história de urgência ou problema.\n"
            "• Evita fazer chamada de voz ou vídeo.\n"
            "• Pede para não contar para outros familiares."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Sempre ligue para o número antigo para confirmar.\n"
            "• Mande mensagem para a pessoa em outra rede social.\n"
            "• Pergunte algo pessoal que um estranho não saberia.\n"
            "• Não salve o novo número antes de confirmar.\n"
            "• Avise seus familiares se receber esse tipo de mensagem.\n"
            "• Se confirmar que é golpe, bloqueie e denuncie o número."
        ),
    },
    "falso-funcionario-banco": {
        "title": "🏦 Falso Funcionário de Banco",
        "what": (
            "Neste golpe, uma pessoa finge ser funcionário do seu banco. "
            "Ela pode entrar em contato por telefone, WhatsApp ou até "
            "pessoalmente.\n\n"
            "O golpista diz que:\n"
            "• Sua conta foi bloqueada ou invadida\n"
            "• Houve uma compra suspeita no seu cartão\n"
            "• Você precisa atualizar seus dados\n"
            "• Seu cartão precisa ser trocado"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• Pedem sua senha ou código de segurança.\n"
            "• Pedem para você instalar um aplicativo no celular.\n"
            "• Dizem que vão enviar um motoboy buscar seu cartão.\n"
            "• Pedem para você fazer um Pix ou transferência de teste.\n"
            "• Ligam pedindo para você digitar a senha no telefone.\n"
            "• A ligação é muito insistente e apressada.\n"
            "• O número de telefone não é o oficial do banco."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Bancos NUNCA pedem senha por telefone ou WhatsApp.\n"
            "• Bancos NUNCA mandam motoboy buscar cartão.\n"
            "• Bancos NUNCA pedem para instalar app por telefone.\n"
            "• Desligue e ligue para o número oficial do banco.\n"
            "• O número oficial está no verso do seu cartão.\n"
            "• Use apenas o aplicativo oficial do banco.\n"
            "• Nunca entregue seu cartão a estranhos.\n"
            "• Em caso de dúvida, vá até a agência pessoalmente."
        ),
    },
    "clonagem-whatsapp": {
        "title": "🔄 Clonagem de WhatsApp",
        "what": (
            "A clonagem de WhatsApp acontece quando alguém consegue usar "
            "sua conta do WhatsApp em outro celular, sem sua permissão.\n\n"
            "O golpista pode então:\n"
            "• Ler suas conversas\n"
            "• Enviar mensagens se passando por você\n"
            "• Pedir dinheiro para seus contatos\n"
            "• Acessar seus grupos"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• Alguém pede o código de 6 dígitos que chegou por SMS.\n"
            "• Dizem ser do suporte do WhatsApp.\n"
            "• Oferecem \"verificação de segurança\" da sua conta.\n"
            "• Seu WhatsApp para de funcionar do nada.\n"
            "• Você recebe código de verificação sem ter pedido.\n"
            "• Seus contatos recebem mensagens que você não enviou."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Ative a verificação em duas etapas AGORA:\n"
            "  WhatsApp > Configurações > Conta > Verificação em duas etapas\n"
            "• NUNCA compartilhe o código de 6 dígitos com ninguém.\n"
            "• Use uma senha forte e um e-mail de recuperação.\n"
            "• Se seu WhatsApp for clonado:\n"
            "  1. Tente entrar de novo com seu número\n"
            "  2. O código vai para você, desconectando o golpista\n"
            "  3. Avise seus contatos\n"
            "  4. Ative a verificação em duas etapas"
        ),
    },
    "codigo-verificacao": {
        "title": "🔐 Código de Verificação",
        "what": (
            "O código de verificação é uma senha temporária enviada por SMS "
            "ou aplicativo para confirmar sua identidade.\n\n"
            "Golpistas tentam enganar as pessoas para conseguir esse código, "
            "porque com ele podem:\n"
            "• Entrar no seu WhatsApp\n"
            "• Acessar sua conta bancária\n"
            "• Fazer compras no seu cartão\n"
            "• Criar cadastros no seu nome"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• Alguém pede o código que acabou de chegar por SMS.\n"
            "• Dizem que é para \"confirmar seu cadastro\".\n"
            "• Falam que é para \"liberar um benefício\".\n"
            "• Dizem que é o banco verificando sua conta.\n"
            "• Pedem o código com urgência ou ameaça de bloqueio."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• NUNCA compartilhe código de verificação com ninguém.\n"
            "• Nenhuma empresa de verdade pede esse código.\n"
            "• Código é pessoal e intransferível.\n"
            "• Se alguém pedir código, é golpe — bloqueie na hora.\n"
            "• Leia a mensagem do código: ela avisa para não compartilhar.\n"
            "• Se receber código sem ter pedido, ignore e não compartilhe."
        ),
    },
    "boleto-falso": {
        "title": "📄 Boleto Falso",
        "what": (
            "O golpe do boleto falso acontece quando criminosos criam um "
            "boleto bancário que parece real, mas o dinheiro vai para a "
            "conta do golpista, e não para a empresa ou pessoa correta.\n\n"
            "Isso pode acontecer com:\n"
            "• Boletos de compras online\n"
            "• Boletos de contas (luz, água, internet)\n"
            "• Boletos de impostos ou taxas\n"
            "• Boletos de mensalidades"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• O boleto veio por e-mail ou WhatsApp de fonte desconhecida.\n"
            "• O valor está diferente do esperado.\n"
            "• O código de barras ou os números estão borrados.\n"
            "• O nome da empresa no boleto parece errado.\n"
            "• O banco que aparece no boleto é diferente do normal.\n"
            "• A data de vencimento está muito próxima ou já passou.\n"
            "• O e-mail tem erros de português ou aparência estranha."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Sempre confira o nome do beneficiário antes de pagar.\n"
            "• Compare o boleto com um anterior que você já pagou.\n"
            "• Prefira pagar pelo aplicativo oficial da empresa.\n"
            "• Use o Débito Direto Autorizado (débito automático).\n"
            "• Baixe boletos apenas do site oficial da empresa.\n"
            "• Leia o código de barras com o app do banco para verificar.\n"
            "• Se desconfiar, entre em contato com a empresa pelos canais oficiais."
        ),
    },
    "links-falsos": {
        "title": "🔗 Links Falsos",
        "what": (
            "Links falsos são endereços de internet que parecem verdadeiros, "
            "mas levam para sites criados por golpistas.\n\n"
            "Esses sites podem:\n"
            "• Roubar suas senhas\n"
            "• Instalar vírus no seu celular\n"
            "• Capturar seus dados pessoais\n"
            "• Fazer compras no seu nome\n"
            "• Acessar sua conta bancária"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• O link foi enviado por um número desconhecido.\n"
            "• O endereço tem nomes estranhos ou com erros.\n"
            "• Exemplo: \"bancodobrasil-seguranca.xyz\" em vez de \"bb.com.br\".\n"
            "• Links muito curtos como \"bit.ly/algumacoisa\".\n"
            "• A mensagem diz que você ganhou algo e precisa clicar.\n"
            "• Diz que sua conta será bloqueada se não clicar.\n"
            "• Promete fotos, vídeos ou notícias chocantes."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• NÃO clique em links de mensagens suspeitas.\n"
            "• Passe o dedo e veja o endereço completo antes de clicar.\n"
            "• Digite o endereço do site diretamente no navegador.\n"
            "• Use o aplicativo oficial em vez de links.\n"
            "• Se o link for de banco, abra apenas pelo app do banco.\n"
            "• Mantenha o celular atualizado.\n"
            "• Se clicou sem querer, não digite nenhuma informação."
        ),
    },
    "ligacoes-suspeitas": {
        "title": "📞 Ligações Suspeitas",
        "what": (
            "Ligações suspeitas são chamadas telefônicas feitas por golpistas "
            "tentando enganar você.\n\n"
            "Os golpistas podem:\n"
            "• Se passar por funcionário de banco\n"
            "• Dizer que é do suporte técnico\n"
            "• Fingir que é um parente em apuros\n"
            "• Ameaçar com falsos sequestros\n"
            "• Oferecer prêmios ou benefícios falsos"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• A pessoa pede dinheiro ou dados pessoais por telefone.\n"
            "• Pedem para você digitar senha no telefone.\n"
            "• Dizem que é urgente e você precisa agir na hora.\n"
            "• O número que aparece é desconhecido ou estranho.\n"
            "• Ameaçam bloquear sua conta se você não cooperar.\n"
            "• Oferecem prêmios que você não concorreu.\n"
            "• A ligação é gravada ou parece robótica."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Não confirme dados pessoais por telefone.\n"
            "• Desligue e ligue para o número oficial da empresa.\n"
            "• Use bloqueador de chamadas do seu celular.\n"
            "• Cadastre seu número no Não Me Perturbe (www.naomeperturbe.com.br).\n"
            "• Se for ameaça de sequestro, desligue e tente falar com a pessoa.\n"
            "• Nunca faça Pix ou transferência por pressão em ligação.\n"
            "• Avise familiares sobre números suspeitos."
        ),
    },
    "seguranca-banco-digital": {
        "title": "🏦 Segurança no Banco Digital",
        "what": (
            "Banco digital é o aplicativo do banco no seu celular. "
            "Ele é muito prático, mas precisa de cuidados especiais "
            "para manter seu dinheiro seguro.\n\n"
            "Os riscos incluem:\n"
            "• Alguém acessar o app sem sua permissão\n"
            "• Golpes pelo próprio aplicativo\n"
            "• Roubo de senha\n"
            "• Compras não autorizadas"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• O app do banco pede para atualizar fora da loja oficial.\n"
            "• Você recebe mensagem do \"banco\" com link.\n"
            "• Alguém pede sua senha por telefone, WhatsApp ou SMS.\n"
            "• Aparece uma compra que você não reconhece.\n"
            "• O aplicativo está diferente ou pede dados estranhos."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Use senha forte e diferente de outras senhas suas.\n"
            "• Ative a biometria (impressão digital ou rosto).\n"
            "• Nunca salve a senha do banco no celular de forma fácil.\n"
            "• Baixe o app do banco apenas da loja oficial (Play Store ou App Store).\n"
            "• Ative as notificações de movimentação da conta.\n"
            "• Confira o extrato bancário toda semana.\n"
            "• Use limite de transferência diário.\n"
            "• Se perder o celular, avise o banco imediatamente."
        ),
    },
    "promocoes-falsas": {
        "title": "🎁 Promoções Falsas",
        "what": (
            "Golpistas criam promoções falsas na internet para enganar pessoas. "
            "Elas aparecem no WhatsApp, Facebook, Instagram e até em anúncios.\n\n"
            "Promessas comuns:\n"
            "• Celular por R$ 99\n"
            "• Prêmio que você ganhou sem participar\n"
            "• Desconto de 90% em lojas famosas\n"
            "• Vale-compras grátis\n"
            "• Benefício do governo que precisa de cadastro"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• Oferta boa demais para ser verdade.\n"
            "• Pedem para compartilhar com amigos.\n"
            "• Pedem dados pessoais ou pagamento adiantado.\n"
            "• O site não é o oficial da loja.\n"
            "• A promoção tem prazo muito curto: \"só hoje\".\n"
            "• Não tem CNPJ ou informações da empresa.\n"
            "• Pedem para clicar em link suspeito."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Desconfie de ofertas boas demais.\n"
            "• Verifique o site oficial da loja.\n"
            "• Nunca pague nada adiantado para receber prêmio.\n"
            "• Não compartilhe promoções antes de verificar.\n"
            "• Pesquise o nome da loja + \"reclamações\".\n"
            "• Veja se o site tem o cadeado de segurança (https).\n"
            "• Se parece falso, avise amigos e familiares."
        ),
    },
    "falso-suporte": {
        "title": "💻 Falso Suporte Técnico",
        "what": (
            "Neste golpe, alguém finge ser do suporte técnico de uma empresa "
            "como banco, operadora de telefone ou loja.\n\n"
            "O golpista pode:\n"
            "• Ligar dizendo que seu computador ou celular tem vírus\n"
            "• Pedir para instalar um programa de acesso remoto\n"
            "• Dizer que sua conta bancária foi invadida\n"
            "• Pedir senhas para \"resolver o problema\""
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• A empresa liga para você (empresas reais raramente ligam).\n"
            "• Pedem para instalar aplicativo no celular ou computador.\n"
            "• Solicitam senhas ou códigos.\n"
            "• Dizem que é urgente e você precisa agir rápido.\n"
            "• A pessoa é insistente e não deixa você desligar.\n"
            "• O número de telefone não é oficial da empresa."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Empresas de verdade NÃO ligam pedindo senha.\n"
            "• NUNCA instale programas que estranhos pedem.\n"
            "• Desligue e ligue para o número oficial da empresa.\n"
            "• Não permita acesso remoto ao seu celular ou computador.\n"
            "• Se recebeu esse tipo de ligação, bloqueie o número.\n"
            "• Avise familiares sobre essa tentativa de golpe."
        ),
    },
    "golpe-maquininha": {
        "title": "💳 Golpe da Maquininha",
        "what": (
            "O golpe da maquininha acontece na hora do pagamento com cartão, "
            "em lojas físicas ou na entrega em casa.\n\n"
            "Os golpistas podem:\n"
            "• Trocar a maquininha na hora de você digitar a senha\n"
            "• Mostrar um valor e digitar outro\n"
            "• Dizer que a maquininha não funcionou e passar de novo\n"
            "• Copiar os dados do seu cartão\n"
            "• Trocar seu cartão por outro na hora da entrega"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• A maquininha tem visor quebrado ou apagado.\n"
            "• O vendedor insiste em passar o cartão longe de você.\n"
            "• O valor no visor é diferente do esperado.\n"
            "• Pedem para você digitar a senha mais de uma vez.\n"
            "• A maquininha mostra mensagem de erro.\n"
            "• O entregador diz que só aceita cartão (não aceita dinheiro)."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Sempre confira o valor no visor antes de digitar a senha.\n"
            "• Cubra o teclado com a mão ao digitar a senha.\n"
            "• Não entregue seu cartão para ninguém passar longe de você.\n"
            "• Se der erro, peça o comprovante de erro antes de passar de novo.\n"
            "• Prefira pagar por aproximação (sem digitar senha).\n"
            "• Confira se o cartão devolvido é realmente o seu.\n"
            "• Ative as notificações do banco para cada compra."
        ),
    },
    "compras-internet": {
        "title": "🛒 Compras pela Internet",
        "what": (
            "Comprar pela internet é muito prático, mas exige cuidado para "
            "não cair em sites falsos ou perder dinheiro.\n\n"
            "Os perigos incluem:\n"
            "• Sites falsos que imitam lojas reais\n"
            "• Produtos que nunca são entregues\n"
            "• Roubo de dados do cartão\n"
            "• Cobranças indevidas depois da compra"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• Preço muito mais baixo que em outras lojas.\n"
            "• O site não tem o cadeado de segurança (https).\n"
            "• Só aceita Pix ou transferência, não aceita cartão.\n"
            "• Não tem CNPJ ou informações da empresa.\n"
            "• O site tem muitos erros de português.\n"
            "• Não tem telefone de contato ou endereço físico.\n"
            "• As avaliações de outros compradores são muito negativas."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Compre apenas em sites conhecidos e confiáveis.\n"
            "• Pesquise o nome da loja + \"Reclame Aqui\".\n"
            "• Veja se o site começa com \"https://\" e tem cadeado.\n"
            "• Prefira pagar com cartão de crédito (dá para contestar).\n"
            "• Guarde os comprovantes e e-mails da compra.\n"
            "• Desconfie de preços muito abaixo do normal.\n"
            "• Use um cartão virtual para compras online (o app do banco gera)."
        ),
    },
    "urgencia-medo": {
        "title": "⚠️ Golpes com Urgência ou Medo",
        "what": (
            "Muitos golpes usam urgência e medo para fazer a vítima agir "
            "sem pensar. Essa é a principal tática dos golpistas.\n\n"
            "Eles criam situações falsas como:\n"
            "• Sequestro de familiar\n"
            "• Conta bancária bloqueada\n"
            "• Processo judicial urgente\n"
            "• Acidente com parente\n"
            "• Cobrança de dívida falsa"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• A mensagem ou ligação causa medo ou pânico.\n"
            "• Dizem que você precisa agir AGORA, sem pensar.\n"
            "• Pedem para não contar para ninguém.\n"
            "• Exigem pagamento imediato por Pix ou transferência.\n"
            "• Ameaçam consequências graves se não pagar.\n"
            "• Não deixam você desligar ou consultar alguém."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Respire fundo. Golpistas usam o medo para enganar.\n"
            "• NUNCA tome decisões financeiras com medo ou pressa.\n"
            "• Desligue a ligação. Isso não vai causar nada de ruim.\n"
            "• Ligue para a pessoa envolvida na história.\n"
            "• Converse com alguém de confiança antes de agir.\n"
            "• Se for ameaça, registre boletim de ocorrência.\n"
            "• Lembre-se: urgência é o principal sinal de golpe."
        ),
    },
    "redes-sociais": {
        "title": "📱 Cuidados com Redes Sociais",
        "what": (
            "Redes sociais como Facebook, Instagram e TikTok são divertidas, "
            "mas expõem informações pessoais que golpistas podem usar.\n\n"
            "Os riscos incluem:\n"
            "• Golpistas estudando sua vida para enganar você\n"
            "• Falsos perfis usando suas fotos\n"
            "• Links maliciosos em comentários\n"
            "• Pessoas estranhas se passando por amigos"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• Solicitação de amizade de alguém que você já tem adicionado.\n"
            "• Perfil com poucas fotos e poucos amigos.\n"
            "• Mensagem pedindo dinheiro ou favores.\n"
            "• Alguém pedindo informações pessoais por mensagem.\n"
            "• Links enviados por pessoas que você não conhece bem."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Deixe seu perfil privado (apenas amigos podem ver).\n"
            "• Não aceite solicitações de quem você não conhece.\n"
            "• Não poste fotos de documentos, passagens ou cartões.\n"
            "• Não compartilhe sua localização em tempo real.\n"
            "• Não divulgue quando estiver viajando (publique depois).\n"
            "• Cuidado com fotos de familiares — sempre peça permissão.\n"
            "• Use senhas diferentes para cada rede social."
        ),
    },
    "golpes-sms": {
        "title": "📩 Golpes por SMS",
        "what": (
            "Golpistas enviam mensagens SMS falsas se passando por bancos, "
            "lojas ou empresas de entrega.\n\n"
            "Essas mensagens geralmente:\n"
            "• Dizem que seu banco bloqueou sua conta\n"
            "• Falam de uma entrega que precisa ser confirmada\n"
            "• Oferecem prêmios ou promoções\n"
            "• Avisam sobre uma compra suspeita"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• A mensagem contém um link para clicar.\n"
            "• O texto tem erros de português.\n"
            "• O remetente é um número de celular, não um nome de empresa.\n"
            "• Pedem para responder com dados pessoais.\n"
            "• A mensagem é sobre algo que você não reconhece.\n"
            "• O link parece estranho ou diferente do site oficial."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• NUNCA clique em links enviados por SMS.\n"
            "• Empresas sérias não resolvem problemas por SMS.\n"
            "• Abra o app oficial da empresa para verificar.\n"
            "• Apague a mensagem e bloqueie o número.\n"
            "• Se for sobre entrega, use o app ou site oficial.\n"
            "• Se for sobre banco, abra o app do banco.\n"
            "• Nunca responda a SMS suspeitos com dados pessoais."
        ),
    },
    "senhas-seguras": {
        "title": "🔑 Senhas Seguras",
        "what": (
            "A senha é a chave da sua casa digital. Uma senha fraca é como "
            "deixar a porta aberta para os golpistas.\n\n"
            "Com senhas fracas, golpistas podem:\n"
            "• Acessar seu e-mail\n"
            "• Entrar no seu WhatsApp\n"
            "• Invadir seu banco\n"
            "• Fazer compras no seu nome"
        ),
        "identify": (
            "⚠️ Senhas que NÃO são seguras:\n\n"
            "• Datas de aniversário (sua ou de parentes)\n"
            "• Nomes de filhos, netos ou animal de estimação\n"
            "• Sequências simples: 123456, 000000\n"
            "• A mesma senha em vários lugares\n"
            "• Senhas anotadas em papel solto ou no celular\n"
            "• \"senha\", \"brasil\", \"deus\", \"amor\""
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Use senhas com pelo menos 8 caracteres.\n"
            "• Misture letras, números e símbolos.\n"
            "• Exemplo de senha forte: \"Caf3_com_P@o_azul\"\n"
            "• Use uma senha diferente para cada serviço importante.\n"
            "• Anote as senhas em um caderno guardado em casa.\n"
            "• Troque as senhas a cada 6 meses.\n"
            "• Ative a verificação em duas etapas sempre que possível."
        ),
    },
    "verificacao-duas-etapas": {
        "title": "🛡️ Verificação em Duas Etapas",
        "what": (
            "A verificação em duas etapas é uma camada extra de segurança. "
            "Mesmo que alguém descubra sua senha, não consegue entrar na sua "
            "conta sem o segundo passo.\n\n"
            "Funciona assim:\n"
            "1. Você coloca sua senha (primeira etapa)\n"
            "2. O sistema pede um código extra (segunda etapa)\n"
            "3. Só com os dois você entra"
        ),
        "identify": (
            "✅ Serviços que permitem verificação em duas etapas:\n\n"
            "• WhatsApp\n"
            "• Facebook e Instagram\n"
            "• Google (Gmail, YouTube)\n"
            "• Aplicativos de banco\n"
            "• Apple (iPhone)\n"
            "• Microsoft (Outlook, Skype)"
        ),
        "protect": (
            "✅ Como ativar:\n\n"
            "No WhatsApp:\n"
            "Configurações > Conta > Verificação em duas etapas\n\n"
            "No Google:\n"
            "minhaconta.google.com > Segurança > Verificação em duas etapas\n\n"
            "No Facebook:\n"
            "Configurações > Segurança > Autenticação de dois fatores\n\n"
            "• Use um e-mail de recuperação que você acessa.\n"
            "• Anote os códigos de backup em um lugar seguro.\n"
            "• Ative em todas as contas importantes."
        ),
    },
    "virus-celular": {
        "title": "🦠 Vírus no Celular",
        "what": (
            "Vírus de celular são programas maliciosos que podem se instalar "
            "no seu aparelho sem você perceber.\n\n"
            "Eles podem:\n"
            "• Roubar suas senhas\n"
            "• Ver o que você digita\n"
            "• Acessar suas fotos e mensagens\n"
            "• Fazer o celular ficar lento\n"
            "• Mostrar anúncios que não fecham"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• O celular ficou muito lento de repente.\n"
            "• A bateria acaba muito rápido.\n"
            "• Aparecem anúncios que não saem da tela.\n"
            "• Aplicativos abrem sozinhos.\n"
            "• Aparecem aplicativos que você não instalou.\n"
            "• O celular esquenta mesmo sem usar.\n"
            "• Você recebe cobranças estranhas na conta do celular."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Instale apps apenas da Play Store (Android) ou App Store (iPhone).\n"
            "• Não clique em links de mensagens suspeitas.\n"
            "• Mantenha o celular sempre atualizado.\n"
            "• Não aceite instalar apps que \"alguém indicou por WhatsApp\".\n"
            "• Se desconfiar de vírus:\n"
            "  1. Peça ajuda a alguém de confiança\n"
            "  2. Use um antivírus da loja oficial\n"
            "  3. Desinstale apps que você não reconhece"
        ),
    },
    "site-falso": {
        "title": "🌐 Sites Falsos",
        "what": (
            "Sites falsos são páginas da internet criadas para imitar sites "
            "verdadeiros, como bancos, lojas ou serviços do governo.\n\n"
            "Eles copiam o visual do site verdadeiro para enganar você e:\n"
            "• Roubar sua senha\n"
            "• Capturar seu CPF e dados pessoais\n"
            "• Fazer você pagar por algo que não existe\n"
            "• Instalar vírus no seu celular"
        ),
        "identify": (
            "⚠️ Sinais de alerta:\n\n"
            "• O endereço do site é diferente do oficial.\n"
            "  Exemplo falso: \"banco-brasil.com\"\n"
            "  Exemplo real: \"bb.com.br\"\n"
            "• Não tem o cadeado de segurança (ícone ao lado do endereço).\n"
            "• O visual é parecido, mas tem detalhes estranhos.\n"
            "• Pede informações que o site real nunca pede.\n"
            "• Aparece como anúncio no Google, não como resultado normal."
        ),
        "protect": (
            "✅ O que fazer:\n\n"
            "• Digite o endereço do site diretamente, não use links.\n"
            "• Confira se o endereço termina com o correto (.com.br, .gov.br).\n"
            "• Procure pelo cadeado de segurança antes de digitar dados.\n"
            "• Use os aplicativos oficiais em vez do site no navegador.\n"
            "• Salve os sites importantes nos favoritos do navegador.\n"
            "• Se desconfiar, feche e acesse pelo app oficial."
        ),
    },
    "dicas-gerais": {
        "title": "💡 Dicas Gerais de Segurança",
        "what": (
            "Aqui estão as dicas mais importantes para usar o celular e a "
            "internet com segurança no dia a dia.\n\n"
            "Pense na segurança digital como a segurança da sua casa:\n"
            "você tranca as portas, não deixa estranhos entrarem e cuida "
            "de quem você convida para dentro."
        ),
        "identify": (
            "⚠️ Sinais gerais de golpe — memorize estes:\n\n"
            "🚩 Pediu dinheiro com urgência? É suspeito.\n"
            "🚩 Pediu senha ou código? É golpe.\n"
            "🚩 Mandou link sem você pedir? Não clique.\n"
            "🚩 Prometeu dinheiro fácil? É golpe.\n"
            "🚩 Ameaçou ou assustou? Desligue na hora.\n"
            "🚩 Era para ser segredo? Desconfie.\n"
            "🚩 Bom demais para ser verdade? Provavelmente é falso."
        ),
        "protect": (
            "✅ Os 10 mandamentos da segurança digital:\n\n"
            "1. Nunca compartilhe senhas ou códigos.\n"
            "2. Desconfie de pedidos de dinheiro por mensagem.\n"
            "3. Ligue para confirmar antes de fazer Pix.\n"
            "4. Use senhas fortes e diferentes.\n"
            "5. Ative a verificação em duas etapas.\n"
            "6. Não clique em links suspeitos.\n"
            "7. Mantenha o celular atualizado.\n"
            "8. Compre apenas em sites confiáveis.\n"
            "9. Banco não pede senha por telefone ou WhatsApp.\n"
            "10. Na dúvida, pare e peça ajuda a alguém de confiança."
        ),
    },
}
