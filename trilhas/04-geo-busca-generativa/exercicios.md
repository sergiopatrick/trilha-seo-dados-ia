# Exercícios · 04 · GEO e busca generativa

Como usar. Cada módulo tem exercícios em três níveis. Fixação confere o conceito. Prática aplica num site ou dado real. Desafio pede para ir além. As respostas não estão aqui de propósito. Compare a sua com a documentação oficial citada em leituras.md.

Respostas de IA mudam entre execuções. Em todo exercício que consulta uma IA, registre data, plataforma, modelo quando visível, se a busca estava ativada e se você estava logado.

## 1. Como buscadores com IA recuperam e citam

**Fixação**
1. Explique query fan-out com um exemplo de pergunta e as buscas que ela pode gerar.
2. Diferencie conhecimento do treino e busca em tempo real. Como saber, numa resposta, qual dos dois foi usado?
3. Por que ser recuperado vem antes de ser citado? O que isso diz sobre a relação entre SEO e GEO?

**Prática**
1. Desenhe em Mermaid o fluxo de uma resposta do AI Mode, da pergunta à citação, com as etapas de fan-out, recuperação, seleção de trechos e geração.
2. Faça a mesma pergunta do seu nicho em 4 IAs com busca ativada (AI Mode, ChatGPT, Perplexity e Copilot, por exemplo). Registre as fontes citadas e conte quantas se repetem entre as plataformas.
3. Escolha uma resposta que citou uma página e encontre nela o trecho que sustentou a frase. Anote se o trecho estava no começo da seção, se tinha número e se fazia sentido sozinho.

**Desafio**
1. Monte um RAG local com 20 páginas públicas do seu nicho (coleta com pausa e parada no primeiro 429). Divida em trechos, gere embeddings com um modelo aberto e responda 5 perguntas citando os trechos recuperados. Compare as fontes que o seu sistema escolheu com as que as IAs do item 2 citaram.

## 2. AI Overviews e AI Mode do Google

**Fixação**
1. Por que não existe marcação especial para entrar no AI Overview? O que conta no lugar dela?
2. Explique o que `nosnippet`, `data-nosnippet` e `max-snippet` fazem nos recursos de IA do Google.
3. O que o Google-Extended controla? O que continua acontecendo com o site mesmo com ele bloqueado?

**Prática**
1. Leia a página do Search Central sobre recursos de IA e o seu site. Resuma em 5 frases o que o dono do site consegue controlar.
2. Numa amostra de 50 buscas do seu nicho, dividida por intenção, registre em quantas aparece AI Overview e quais domínios ele cita. Calcule a taxa por intenção.
3. No Search Console do seu site, abra o relatório de impressões em IA generativa e cruze com as páginas do relatório de desempenho. Escreva o que dá para afirmar e o que é inferência, já que o relatório não mostra a busca nem o clique.

**Desafio**
1. Escolha 10 buscas em que o seu site, ou um site cujos dados você tenha, ranqueia no top 5 com AI Overview na SERP. Compare o CTR dessas buscas com o de buscas parecidas sem AI Overview, na mesma faixa de posição. Diga o tamanho da amostra e o que impede uma conclusão causal.

## 3. ChatGPT, Perplexity, Copilot e Gemini como canais de busca

**Fixação**
1. Diferencie robô de treino, robô de busca e robô que busca a página a pedido do usuário. Dê um exemplo de cada para a OpenAI e para a Anthropic.
2. Por que bloquear o GPTBot deixa o site disponível para a busca do ChatGPT?
3. De onde o Copilot tira os resultados? Por que o Bing Webmaster Tools importa para ele?

**Prática**
1. Monte uma tabela com GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User, Google-Extended, Bingbot, Applebot e Applebot-Extended. Use as colunas operador, finalidade, se respeita robots.txt segundo a documentação oficial, onde o operador publica os IPs e o link da documentação.
2. Num log do seu site ou num log de exemplo, conte visitas de cada robô de IA por semana e por seção. Verifique por IP pelo menos um acesso de cada operador que publica lista de IPs.
3. No GA4 da sua propriedade ou na conta de demonstração do Google, crie um agrupamento de canais personalizado com um canal de IA definido por regex de origem (chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai). Ponha esse canal acima de Referência na ordem das regras.

**Desafio**
1. Faça um `curl -sI` com o user-agent de 3 robôs de IA a partir do seu computador e registre as respostas. Depois escreva por que esse resultado não prova bloqueio nem liberação, e desenhe a consulta de log que fecharia a questão.

## 4. Conteúdo citável, entidades e marca

**Fixação**
1. O que é um trecho autossuficiente? Reescreva um parágrafo vago do seu nicho para que ele se sustente sozinho.
2. Por que autoria e data de atualização visíveis ajudam a IA a citar uma página?
3. Como menções de terceiros e o Knowledge Graph influenciam a forma como a IA descreve uma marca?

**Prática**
1. Reescreva uma página sua para ter definição direta e resposta no começo de cada seção, com números e datas acompanhados de fonte. Versione a página antes e depois no Git.
2. Pergunte a 3 IAs "o que é a <marca>?" e "quais as melhores opções de <categoria>?" para uma marca do seu nicho. Registre a descrição, as fontes citadas e os erros factuais.
3. Liste onde a marca aparece fora do próprio site (Wikipédia, Wikidata, imprensa, diretórios, fóruns, sites de reclamação). Confira se ela tem item no Wikidata e painel de conhecimento no Google.

**Desafio**
1. Escreva o JSON-LD de Organization com `sameAs` para os perfis oficiais e de Person para um autor, ligados por `@id`. Mostre como esse grafo se relaciona com o item da marca no Wikidata e o que falta para a entidade ficar consistente entre as fontes.

## 5. llms.txt e controle de acesso de robôs de IA

**Fixação**
1. Qual a função do llms.txt e qual a do robots.txt? Por que um não substitui o outro?
2. Escreva em 3 frases, para um gestor, por que o llms.txt não é garantia de nada.
3. Além do robots.txt, que camadas controlam o acesso de robôs de verdade?

**Prática**
1. Verifique com `curl -sI` se 10 sites do seu nicho têm `/llms.txt` e `/llms-full.txt`, com pausa entre os pedidos. Para os que têm, confira se os links do arquivo respondem 200 e tente descobrir quem o gerou.
2. Escreva um llms.txt para um site pequeno seguindo a especificação de llmstxt.org (título em H1, resumo em citação e seções com listas de links).
3. Escreva regras de robots.txt que liberam robôs de busca de IA (OAI-SearchBot, Claude-SearchBot, PerplexityBot) e bloqueiam robôs de treino (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, CCBot). Teste cada regra com a biblioteca `protego`.

**Desafio**
1. Avalie uma página como um agente a leria. Abra a árvore de acessibilidade no DevTools e rode um extrator de texto, como o `trafilatura`, na mesma URL. Liste o que se perde (botões sem nome, texto dentro de imagem, conteúdo que só aparece depois de clique) e proponha a correção no HTML.

## 6. Medir visibilidade em IA

**Fixação**
1. Por que nenhuma fonte sozinha mede GEO? Diga o que Search Console, GA4, log e monitoramento de prompts mostram e o que cada um esconde.
2. Por que a mesma pergunta dá respostas diferentes em execuções seguidas? Como isso afeta o tamanho da amostra?
3. Por que quase nenhuma ferramenta de visibilidade em IA tem comparação ano contra ano em 2026?

**Prática**
1. Monte um conjunto de 30 prompts fixos do seu tema, distribuídos por intenção e por etapa de decisão. Grave em CSV com id, prompt, intenção e marcas esperadas.
2. Rode os prompts em 2 plataformas toda semana por 4 semanas, 3 vezes cada prompt. Registre se a marca foi citada, se houve link e quais domínios apareceram.
3. Junte numa planilha semanal o tráfego de referência de IA no GA4, as visitas de robôs de IA no log e as impressões em IA generativa do Search Console.

**Desafio**
1. Calcule a taxa de citação por plataforma com intervalo de confiança (o intervalo de Wilson funciona bem para proporções). Diga a partir de que diferença entre duas semanas você trataria a mudança como real, e quantas execuções seriam necessárias para detectar uma variação de 10 pontos.

## 7. Pesquisa acadêmica sobre GEO

**Fixação**
1. Quais as nove táticas testadas no artigo GEO de Aggarwal e colegas? Quais funcionaram melhor e quais não funcionaram?
2. O que é o GEO-bench? Quais métricas de visibilidade o artigo propõe?
3. Que limites o artigo tem para quem quer aplicar as conclusões no Google e no ChatGPT de hoje?

**Prática**
1. Leia o artigo (arXiv 2311.09735) e escreva um resumo de uma página com método, resultados e limites.
2. Aplique 3 táticas do artigo (citar fontes, incluir estatísticas, usar citações diretas) numa página sua. Meça antes e depois com o conjunto de prompts do módulo 6 por pelo menos 4 semanas.
3. Encontre 2 trabalhos posteriores sobre viés de fonte ou citação em LLMs no arXiv ou no Google Acadêmico e resuma o que cada um acrescenta.

**Desafio**
1. Replique em pequena escala um experimento do artigo com um modelo aberto rodando local, via Ollama por exemplo. Use 10 perguntas com 5 fontes cada, modifique uma das fontes com uma tática e meça quantas vezes ela passa a ser citada em relação à versão original.

## Projeto da trilha · Diagnóstico de GEO de uma marca

**Objetivo.** Medir como uma marca aparece em respostas de IA, verificar se os robôs certos conseguem ler o site e propor um plano de conteúdo citável com base em evidência.

**Dados de entrada.** Uma marca pública ou a sua própria, mais 3 concorrentes. Respostas de IAs coletadas por você, o robots.txt e o llms.txt públicos da marca, a documentação oficial de cada robô e, se o site for seu, Search Console, GA4 e log.

**Passos**
1. Escolha a marca e 3 concorrentes. Descreva o mercado em um parágrafo.
2. Escreva 30 prompts fixos, distribuídos por intenção (descoberta, comparação, decisão, marca).
3. Rode os 30 prompts em 3 IAs com busca ativada, em duas rodadas com uma semana de intervalo. Registre citação da marca, link, posição na resposta, domínios citados e erros factuais.
4. Monte a tabela de robôs de IA com operador, finalidade, regra de robots.txt e link da documentação.
5. Analise o robots.txt da marca e diga, robô por robô, o que ele pode fazer. Se houver log, confirme com dado de acesso.
6. Confira se existe llms.txt, quem o gera e se os links funcionam. Proponha uma versão revisada e explique os limites dele.
7. Avalie a entidade (Wikidata, painel de conhecimento, Organization em JSON-LD, menções de terceiros).
8. Escreva o plano de conteúdo citável com 10 páginas a criar ou reescrever. Para cada uma, diga o prompt que ela atende, o trecho de resposta direta, o dado próprio ou fonte e a autoria.
9. Escreva as limitações (tamanho da amostra, variação entre execuções, série curta, ausência de dado de busca no relatório de IA do Search Console).

**Entregável.** Repositório público com `prompts.csv`, `respostas.csv` com as duas rodadas, `robos.md` com a tabela, o robots.txt e o llms.txt propostos, `plano-conteudo.md` e um `README.md` com o diagnóstico, os números principais e as limitações.

**Critérios de avaliação**
- [ ] Os 30 prompts cobrem intenções diferentes e estão versionados
- [ ] Cada resposta registra data, plataforma, busca ativada e estado de login
- [ ] A taxa de citação da marca e dos concorrentes aparece por plataforma e por rodada
- [ ] A tabela de robôs cita a documentação oficial de cada um
- [ ] O robots.txt proposto separa busca de treino e foi testado
- [ ] O llms.txt é apresentado como complemento, sem promessa de efeito
- [ ] Afirmações sobre bloqueio de robô se apoiam em log ou ficam marcadas como hipótese
- [ ] O plano tem 10 páginas, cada uma ligada a um prompt e com trecho citável
- [ ] As limitações estão escritas e o relatório evita conclusão causal sem teste
