# 04 · GEO e busca generativa

GEO (Generative Engine Optimization) é o trabalho de ser encontrado, entendido e citado por sistemas que respondem com texto gerado. AI Overviews e AI Mode no Google, ChatGPT, Perplexity, Gemini, Copilot e Claude. A base é a mesma do SEO. O que muda é como a resposta é montada e como medir.

**Pré-requisitos.** Trilhas 01 e 02. Trilha 07, módulos 3 e 4 (embeddings e RAG), ajudam muito.
**Carga estimada.** 30 h.

**Ao terminar, você consegue**
- explicar como um buscador com IA recupera trechos e decide o que citar;
- dizer quais robôs de IA existem, o que cada um faz e como controlá-los;
- escrever conteúdo que a IA consegue extrair e atribuir a você;
- medir visibilidade em IA com o que existe hoje, sabendo os limites de cada fonte;
- separar evidência de promessa nesse mercado novo.

## Roteiro

### 1. Como buscadores com IA recuperam e citam

Um buscador generativo funciona como um RAG gigante. A pergunta vira várias buscas (query fan-out), os resultados viram trechos, os trechos entram no contexto do modelo e o modelo escreve a resposta citando parte deles. Para ser citado, você precisa primeiro ser recuperado.

**Conceitos-chave.** Recuperação, ranqueamento de trechos e geração. Query fan-out. Grounding. Citação e atribuição. Índice próprio contra índice de terceiros (Bing, Google). Conhecimento do treino contra busca em tempo real.

- [ ] Desenhei o fluxo de uma resposta do AI Mode, da pergunta à citação
- [ ] Fiz a mesma pergunta em 4 IAs e comparei quais fontes cada uma citou

### 2. AI Overviews e AI Mode do Google

O Google usa o mesmo índice e os mesmos sistemas de qualidade da busca tradicional, com uma camada de geração por cima. Não existe marcação especial para entrar. Existe o básico bem feito.

**Conceitos-chave.** Quando o AI Overview aparece. AI Mode como experiência separada. Controles `nosnippet`, `data-nosnippet` e `max-snippet`. Google-Extended e o que ele controla (e o que não controla). Impacto no CTR.

**Na prática.** O Search Console passou a mostrar impressões em IA generativa num relatório próprio, em beta, só com impressões, sem busca e sem clique, e com série começando em maio de 2026. Numa loja, a maior parte dessas impressões estava na home, que ranqueia quase só por marca. Isso sugere AI Overview na busca de marca, mas é inferência, porque o relatório não mostra a busca. Diga isso no relatório.

- [ ] Li a documentação do Google sobre recursos de IA e o seu site
- [ ] Sei dizer o que Google-Extended bloqueia e o que continua acontecendo
- [ ] Medi, numa amostra de buscas, em quantas aparece AI Overview

### 3. ChatGPT, Perplexity, Copilot e Gemini como canais de busca

Cada plataforma tem robôs diferentes, para treino, para busca e para buscar a página quando o usuário pede. Bloquear um não bloqueia os outros.

**Conceitos-chave.** GPTBot, OAI-SearchBot e ChatGPT-User. ClaudeBot, Claude-SearchBot e Claude-User. PerplexityBot e Perplexity-User. Bingbot e o índice que alimenta o Copilot. Applebot e Applebot-Extended. Verificação por IP. Tráfego de referência dessas plataformas no GA4.

**Na prática.** O log de um portal de saúde mostrou, num mês, visitas de Applebot, Googlebot, Bingbot, OAI-SearchBot, ClaudeBot, GPTBot, PerplexityBot e outros, todos sendo atendidos. Um teste local tinha sugerido o contrário. Prova de acesso é log de servidor.

- [ ] Montei uma tabela com cada robô de IA, quem opera, para que serve e como bloquear
- [ ] Contei visitas de robôs de IA num log real ou de exemplo
- [ ] Criei no GA4 um agrupamento de canal para tráfego vindo de IAs

### 4. Conteúdo citável, entidades e marca

A IA cita o trecho que responde a pergunta de forma clara, específica e atribuível. E prefere fontes que o resto da web já reconhece como referência no assunto.

**Conceitos-chave.** Trechos autossuficientes (cada seção se sustenta sozinha). Definição direta logo no começo. Dados, números e datas. Autoria e data de atualização visíveis. Entidades e Knowledge Graph. Menções de marca em fontes de terceiros. Dados estruturados de Organization, Person e Product.

- [ ] Reescrevi uma página para ter respostas diretas no começo de cada seção
- [ ] Verifiquei como 3 IAs descrevem uma marca e de onde tiram a informação
- [ ] Listei onde a marca é mencionada fora do próprio site

### 5. llms.txt e controle de acesso de robôs de IA

O llms.txt é uma proposta de arquivo em Markdown que resume o site para modelos de linguagem. O guia de otimização para IA generativa do Google, publicado em maio de 2026, diz que a Busca ignora esse tipo de arquivo e que não existe marcação especial de Schema.org para aparecer nos recursos de IA. Outras plataformas podem ler o arquivo, sem garantia de efeito. O controle de acesso de verdade continua sendo robots.txt, cabeçalhos e WAF.

**Conceitos-chave.** Especificação do llms.txt e llms-full.txt. Diferença entre llms.txt e robots.txt. Regras por robô no robots.txt. Bloqueio na CDN. Páginas legíveis por agente (HTML limpo, árvore de acessibilidade).

**Na prática.** Num portal, existia um llms.txt esquecido, gerado por um plugin já desinstalado, apontando para páginas que davam 404. Antes de criar o arquivo, procure se já existe um e quem o gera. Lojas em Shopify, por exemplo, já recebem um gerado pela plataforma.

- [ ] Li a especificação do llms.txt e escrevi um para um site pequeno
- [ ] Escrevi regras de robots.txt que permitem busca e bloqueiam treino
- [ ] Sei explicar a um gestor por que llms.txt não é garantia de nada

### 6. Medir visibilidade em IA

Medir GEO ainda é juntar sinais imperfeitos. Nenhuma fonte sozinha conta a história.

**Conceitos-chave.** Relatório de IA generativa do Search Console. Tráfego de referência de IAs no GA4. Logs de robôs de busca de IA. Ferramentas de monitoramento de citação (amostra de prompts). Variação entre execuções. Painel de prompts fixos com série semanal.

**Na prática.** As ferramentas de visibilidade em IA começaram suas séries entre 2025 e 2026, então quase nenhuma tem comparação ano contra ano. Diga isso no relatório e trabalhe com tendência de curto prazo.

- [ ] Montei um conjunto de 30 prompts fixos do meu tema
- [ ] Rodei os prompts em 2 plataformas por 4 semanas e registrei as citações
- [ ] Juntei referência no GA4, robôs no log e impressões no Search Console num só painel

### 7. Pesquisa acadêmica sobre GEO

O termo GEO vem de um artigo de 2023 que testou nove táticas em buscadores generativos. Citar fontes, incluir estatísticas e usar citações diretas aumentaram a visibilidade. Encher de palavra-chave não. Ler a pesquisa protege contra promessa sem base.

**Conceitos-chave.** O artigo GEO de Aggarwal e colegas (KDD 2024) e o benchmark GEO-bench. Métricas de visibilidade em resposta gerada. Trabalhos seguintes sobre viés de fonte e citação em LLMs.

- [ ] Li o artigo GEO e resumi as táticas que funcionaram e as que não
- [ ] Apliquei 3 táticas do artigo numa página e medi antes e depois

## Material

- [Vídeos](videos.md)
- [Leituras](leituras.md)
- [Exercícios e projeto da trilha](exercicios.md)

**Próximo passo.** [Projetos integradores](../../projetos), em especial o [monitor de visibilidade em IA](../../projetos/02-monitor-de-visibilidade-em-ia.md).
