import streamlit as st

st.set_page_config(page_title="Projeto Despluguito", page_icon="🤖", layout="wide")

# 🎨 DESIGN ESCOLAR ATUALIZADO (Injeção de estilo limpa e sem erros de sintaxe)
st.markdown("""
    <style>
    .stApp { background-color: #f0f7f9 !important; }
    h1 { color: #1e56a0 !important; font-family: 'Arial', sans-serif; font-weight: bold; }
    h2, h3 { color: #2d6a4f !important; }
    .streamlit-expanderHeader { background-color: #ffffff !important; border-left: 5px solid #ff9a00 !important; }
    
    /* Customização estética dos seletores do topo */
    div[data-testid="stSelectbox"] {
        background-color: #fff9db !important;
        border-radius: 8px;
        padding: 5px;
        border: 1px dashed #ffe066;
    }
    </style>
""", unsafe_allow_html=True)

# BANCO DE DADOS COMPLETO E EXPANDIDO
REPOSITORIO_ATIVIDADES = {
    "🎒 Educação Infantil": {
        "🧩 Pensamento Computacional": [
            {
                "titulo": "O Caminho do Tesouro (Algoritmos e Orientação)",
                "objetivo": "BNCC: (EI03ET07) Orientar-se no espaço e reconhecer direções.",
                "materiais": "Giz colorido para o chão ou fita crepe, um brinquedo para ser o tesouro.",
                "desenvolvimento": "Desenhe uma grade no chão. Um aluno faz o papel de robô (anda conforme as instruções) e outro dá os comandos: 'um passo à frente', 'vire à esquerda'. O objetivo é chegar ao tesouro desviando de obstáculos fictícios.",
                "etica": "Discussão: Computadores não têm vontade própria. Eles apenas seguem regras rígidas que humanos criam. Se a instrução for errada, o robô erra. Nós somos os responsáveis."
            },
            {
                "titulo": "Siga o Padrão (Reconhecimento de Padrões)",
                "objetivo": "BNCC: (EI03ET05) Classificar objetos e identificar sequências lógicas.",
                "materiais": "Elementos da natureza (folhas, pedrinhas, gravetos) ou tampinhas de garrafa.",
                "desenvolvimento": "O professor cria uma sequência no chão: 'Folha, Pedra, Folha, Pedra'. As crianças devem identificar o padrão e continuar a sequência. Depois, aumente a complexidade (ex: duas folhas, uma pedra).",
                "etica": "Discussão: A Inteligência Artificial aprende olhando padrões das coisas que os humanos fazem. Se mostrarmos só padrões legais, ela aprende coisas legais."
            }
        ],
        "🌐 Mundo Digital": [
            {
                "titulo": "Caçadores de Dispositivos",
                "objetivo": "Identificar o que é e o que não é tecnologia no cotidiano.",
                "materiais": "Imagens de revistas ou desenhos diversos (geladeira, livro, árvore, celular).",
                "desenvolvimento": "Espalhe as imagens pela sala. Peça para as crianças 'caçarem' e agruparem apenas os objetos que precisam de energia, pilhas ou bateria para funcionar.",
                "etica": "Discussão: Tecnologia serve para nos ajudar, mas existem momentos certos para tudo. Brincar ao ar livre e conversar com os amigos é tão importante quanto o tempo que passamos perto das telas."
            }
        ],
        "⚖️ Cultura Digital": [
            {
                "titulo": "Semáforo da Privacidade",
                "objetivo": "Introduzir a noção de segurança de dados pessoais de forma lúdica.",
                "materiais": "Cartões coloridos (Verde e Vermelho) para cada aluno.",
                "desenvolvimento": "O professor dita situações. Se for seguro falar em público, as crianças levantam o cartão verde. Se for privado, o vermelho. Exemplos: 'Dizer seu nome', 'Contar onde você mora para um estranho', 'Falar sua cor favorita'.",
                "etica": "Discussão: Na internet, nossos dados pessoais são como tesouros trancados. Não devemos dar a chave da nossa casa ou nossas informações para quem não conhecemos."
            }
        ]
    },
    "📐 Ensino Fundamental - Anos Iniciais": {
        "🧩 Pensamento Computacional": [
            {
                "titulo": "Fábrica de Monstros (Variáveis e Estados)",
                "objetivo": "BNCC: (EF03MA15) Seguir instruções lógicas e associar formas geométricas.",
                "materiais": "Papel, lápis de cor e um dado de jogo comum.",
                "desenvolvimento": "Desenhe uma tabela no quadro: Dado 1 = Corpo redondo; Dado 2 = Corpo quadrado. Dado 1 (olhos) = 3 olhos; Dado 2 = 1 olho. Os alunos jogam o dado para cada parte do monstro. O valor do dado funciona como uma 'variável' que muda o resultado do desenho.",
                "etica": "Discussão: Se mudarmos os dados que entram no jogo, o monstro muda completamente. Na IA é igual: se os dados que colocamos nela forem ruins ou injustos, as respostas dela serão injustas (conceito de viés)."
            },
            {
                "titulo": "Treinando o Robô Separador (Machine Learning)",
                "objetivo": "Compreender como algoritmos de classificação aprendem por exemplos.",
                "materiais": "Cartões desenhados com frutas e vegetais diversos.",
                "desenvolvimento": "Um aluno faz o papel de 'IA'. O professor coloca na caixa A imagens de frutas e diz 'isso são Frutas'. Coloca na caixa B vegetais e diz 'vegetais'. O aluno-IA deve analisar as características compartilhadas para classificar novos cartões misteriosos.",
                "etica": "Discussão: Se treinarmos nossa IA mostrando apenas maçãs vermelhas, ela vai conseguir reconhecer uma maçã verde? Sistemas precisam de diversidade de dados para serem inclusivos e não excluírem ninguém."
            }
        ],
        "🌐 Mundo Digital": [
            {
                "titulo": "A Rede Humana (Roteamento de Pacotes de Internet)",
                "objetivo": "Compreender como a informação viaja pela internet sem computadores.",
                "materiais": "Barbantes compridos e folhas de papel divididas em pedaços.",
                "desenvolvimento": "Cada aluno representa um roteador conectado por barbantes. Uma mensagem comprida é escrita em um papel, cortada em 3 pedaços (pacotes) e numerada. Os pacotes viajam de mão em mano por caminhos diferentes até chegar ao destino final, onde são remontados.",
                "etica": "Discussão: Se um desses pedaços passar por uma pessoa não confiável na rede, ela pode tentar ler a mensagem. Por isso usamos criptografia e senhas fortes para proteger nossos dados enquanto eles viajam."
            }
        ],
        "⚖️ Cultura Digital": [
            {
                "titulo": "O Detetive das Fake News",
                "objetivo": "Desenvolver o pensamento crítico sobre conteúdos que circulam em meios digitais.",
                "materiais": "Manchetes de notícias reais e histórias evidentemente inventadas impressas.",
                "desenvolvimento": "Em grupos, os alunos recebem as manchetes e aplicam um checklist: Quem escreveu? Tem data? Parece absurdo demais? Eles devem julgar a confiabilidade da informação.",
                "etica": "Discussão: Criar ou espalhar mentiras na internet prejudica a vida de pessoas de verdade. Temos a obrigação ética de verificar antes de compartilhar qualquer conteúdo."
            }
        ]
    },
    "📝 Ensino Fundamental - Anos Finais": {
        "🧩 Pensamento Computacional": [
            {
                "titulo": "O Teste de Turing Humano (IA e Linguagem Natural)",
                "objetivo": "Debater a capacidade de simulação de linguagem natural por máquinas.",
                "materiais": "Papel e caneta.",
                "desenvolvimento": "Um aluno assume o papel de 'Juiz' e fica de costas. Atrás dele, um aluno responde como humano e outro responde fingindo ser um Chatbot de IA limitado. O Juiz envia perguntas escritas e, pelas respostas frias, repetitivas ou hiper-rápidas, deve adivinhar quem é a máquina.",
                "etica": "Discussão: É ético criar robôs que imitam perfeitamente sentimentos humanos para enganar pessoas? Como diferenciar textos gerados por IA e textos autorais legítimos na escola?"
            }
        ],
        "🌐 Mundo Digital": [
            {
                "titulo": "A Bolha dos Algoritmos de Recomendação",
                "objetivo": "Compreender o funcionamento dos sistemas de recomendação das redes sociais.",
                "materiais": "Fichas temáticas (Futebol, Jogos, Maquiagem, Notícias).",
                "desenvolvimento": "Um aluno interpreta o algoritmo de uma rede social. Se o usuário passa mais tempo olhando para fichas de 'Jogos', o algoritmo passa a entregar apenas fichas de 'Jogos'. No final da dinâmica, o usuário percebe que não recebe mais nenhum outro tema.",
                "etica": "Discussão: Os algoritmos são projetados para prender nossa atenção pelo maior tempo possível. Isso cria 'bolhas' onde as pessoas não enxergam opiniões diferentes. Como manter nossa autonomia digital?"
            }
        ],
        "⚖️ Cultura Digital": [
            {
                "titulo": "Tribunal da IA: Deepfakes e Direitos Autorais",
                "objetivo": "Analisar os impactos éticos da geração de mídias sintéticas por IA.",
                "materiais": "Um caso fictício impresso para debate em formato de júri.",
                "desenvolvimento": "Divida a sala em grupos: Defesa, Acusação e Júri. Caso: Uma ferramenta de IA gerou uma música inédita imitando perfeitamente a voz de um artista famoso que já faleceu, lucrando sem a autorização da família. Debatam se isso é correto.",
                "etica": "Princípio Ético: O consentimento humano, os direitos autorais e o respeito à imagem e identidade do próximo devem prevalecer sempre sobre a capacidade técnica de replicar dados."
            }
        ]
    }
}

# Cabeçalho decorado principal
st.title("✏️ Projeto Despluguito: BNCC Computação & IA")
st.markdown("### 📒 *Raciocínio Lógico e Ética Digital sem Uso de Telas*")
