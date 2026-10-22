# Exercícios · 07 · IA aplicada

Como usar. Cada módulo tem exercícios em três níveis. Fixação confere o conceito. Prática aplica num site ou dado real. Desafio pede para ir além. As respostas não estão aqui de propósito. Compare a sua com a documentação oficial citada em [leituras.md](leituras.md).

Os exercícios usam Python, a API de um modelo comercial (com limite de gasto configurado no console antes de começar), modelos abertos do Hugging Face e o Ollama. Os dados são públicos. Documentação aberta (DuckDB, dbt, Google Search Central), datasets do Hugging Face, áudio de domínio público do LibriVox e o seu próprio site. Nunca mande dado de cliente para uma API de modelo nos exercícios.

## 1. Como funciona um LLM

**Fixação**
1. Explique, sem jargão, o que acontece entre o envio do prompt e o primeiro token da resposta.
2. Qual é a diferença entre pré-treino, ajuste fino com instruções e RLHF? O que cada etapa muda no comportamento do modelo?
3. Por que o modelo inventa uma referência bibliográfica com a mesma confiança com que cita uma real? O que a temperatura tem a ver com isso, e o que ela não resolve?

**Prática**
1. Pegue o mesmo parágrafo em português e a tradução dele em inglês. Conte os tokens com o tokenizador de um modelo aberto (`AutoTokenizer` da biblioteca `transformers`) e com o endpoint de contagem de tokens da API que você usa. Calcule a razão entre português e inglês e o efeito disso no custo.
2. Rode o mesmo prompt 10 vezes com temperatura 0 e 10 vezes com temperatura 1. Meça quantas respostas distintas saem em cada caso.
3. Pergunte a um modelo sem acesso à web sobre um fato posterior ao corte de conhecimento dele e sobre um artigo científico inexistente com título plausível. Registre as respostas e classifique cada uma como recusa, acerto ou invenção.

**Desafio**
1. Assista a uma introdução completa a LLMs (está em [videos.md](videos.md)) e escreva um resumo de uma página para alguém de marketing. Peça a essa pessoa para explicar de volta o que é janela de contexto e anote onde ela errou.

## 2. Engenharia de prompt e de contexto

**Fixação**
1. Qual é a diferença entre engenharia de prompt e engenharia de contexto? Liste os componentes do contexto que o modelo vê numa chamada.
2. Por que separar dado de instrução com marcação (por exemplo tags XML) melhora a estabilidade e ajuda contra injeção?
3. Por que explicar o porquê de uma regra funciona melhor que só a regra? Reescreva "não use travessão" com o motivo.

**Prática**
1. Faça o tutorial interativo de prompt engineering da Anthropic no GitHub. Anote os três capítulos que mais mudaram a forma como você escreve prompt.
2. Escreva um prompt que classifica buscas do Search Console do seu site em intenção informacional, navegacional, comercial ou transacional. Rode em 50 buscas e anote a taxa de resposta fora do formato. Depois reescreva com papel, 4 exemplos, motivo de cada regra e saída em JSON validado por esquema (saída estruturada ou `pydantic`). Rode de novo e compare.
3. Escreva um arquivo de instruções de projeto (`CLAUDE.md` ou `AGENTS.md`) para um repositório seu, com objetivo, comandos, convenções e decisões já tomadas.

**Desafio**
1. Pegue uma tarefa longa (por exemplo, resumir 20 páginas de documentação). Compare três montagens de contexto. Tudo de uma vez, só os trechos relevantes e trechos relevantes com um resumo do resto. Meça qualidade (com uma rubrica sua) e tokens de entrada em cada uma.

## 3. Embeddings e busca vetorial

**Fixação**
1. O que é similaridade de cosseno e por que ela ignora o tamanho do vetor?
2. Por que a divisão em trechos (chunking) muda o que a busca encontra? Cite o risco de trecho muito pequeno e o de trecho muito grande.
3. Quando a busca por palavra-chave (BM25) ganha da vetorial? O que busca híbrida e reranking acrescentam?

**Prática**
1. Faça o crawl do seu site (ou de um site público, com pausa entre requisições) com o Screaming Frog gratuito, limitado a 500 URLs, e exporte os títulos. Gere embeddings com um modelo multilíngue aberto (`intfloat/multilingual-e5-small` ou `paraphrase-multilingual-MiniLM-L12-v2` no `sentence-transformers`). Agrupe com k-means ou HDBSCAN e dê nome a cada grupo.
2. Monte 20 perguntas sobre uma documentação aberta (por exemplo, a do DuckDB, no repositório `duckdb/duckdb-web`). Compare BM25 (`rank_bm25`) e busca vetorial na mesma base. Para cada pergunta, anote se o trecho certo aparece entre os 5 primeiros.
3. Repita a busca vetorial com trechos de 200, 500 e 1.000 tokens, com sobreposição de 10%. Monte uma tabela de recall@5 por tamanho.

**Desafio**
1. Combine BM25 e vetor com Reciprocal Rank Fusion e depois aplique um reranker multilíngue aberto (por exemplo `BAAI/bge-reranker-v2-m3`). Mostre quanto cada etapa acrescentou em recall@5 e quanto custou em tempo.

## 4. RAG (geração aumentada por recuperação)

**Fixação**
1. Desenhe os dois pipelines de um RAG, o de indexação e o de consulta, e diga em qual deles cada falha comum acontece.
2. O que é contextual retrieval e que problema dos trechos soltos ele resolve?
3. Qual é a diferença entre recall da recuperação e fidelidade da resposta? Dê um exemplo de resposta fiel e errada.

**Prática**
1. Construa um RAG sobre a documentação do DuckDB ou do dbt, usando a busca do módulo 3. A resposta deve citar o arquivo e o trecho de origem.
2. Escreva 20 perguntas de teste com o trecho que deveria ser recuperado. Meça recall@5 e precisão@5.
3. Escolha 10 respostas e confira cada citação abrindo o trecho de origem. Marque se a citação sustenta a afirmação, sustenta em parte ou não sustenta.

**Desafio**
1. Implemente reescrita de consulta (o modelo reescreve a pergunta antes de buscar) e contextual retrieval (um parágrafo de contexto antes de cada trecho no índice). Meça o ganho de cada um separado e juntos. Escreva também três perguntas em que RAG é a ferramenta errada e diga qual seria a certa.

## 5. Agentes, ferramentas e MCP

**Fixação**
1. Qual é a diferença entre um fluxo fixo (encadeamento, roteamento) e um agente autônomo? Quando o segundo vale o custo?
2. Explique o que são servidor, cliente, ferramenta e recurso no MCP.
3. Por que "leitura livre, escrita com confirmação" é um bom padrão de permissão? Dê um exemplo de ferramenta que nunca deveria rodar sem confirmação.

**Prática**
1. Usando a API de um modelo com tool use, crie um agente com 2 ferramentas. Uma busca a série diária de pageviews de um artigo na API da Wikimedia (com User-Agent descritivo e pausa) e a outra calcula a variação entre dois períodos. Peça ao agente para dizer qual de três artigos mais cresceu no último mês. Registre cada chamada de ferramenta.
2. Escreva um servidor MCP com o SDK oficial em Python (`mcp`, com `FastMCP`) que expõe uma consulta somente leitura ao DuckDB do projeto da trilha 06. Teste no MCP Inspector (`npx @modelcontextprotocol/inspector`).
3. Ligue o servidor a um cliente MCP (Claude Desktop, Claude Code ou outro) e faça uma conversa que use a ferramenta. Tente pedir um `DELETE` e mostre que o servidor recusa.

**Desafio**
1. Resolva a mesma tarefa de duas formas. Primeiro, um fluxo fixo em que o código chama as ferramentas na ordem. Depois, um agente que decide sozinho. Compare acerto, tokens gastos e tempo em 10 execuções, e escreva quando cada abordagem compensa.

## 6. Programar com IA

**Fixação**
1. Qual é a diferença entre um assistente no editor e um agente no terminal? Dê uma tarefa em que cada um rende mais.
2. Por que testes funcionam como critério de pronto para um agente de código?
3. O que deve ir no arquivo de instruções do projeto e o que não deve (segredos, regras que mudam toda semana)?

**Prática**
1. Use um agente de código (Claude Code ou outro) para criar um script que valida um `sitemap.xml` (status de cada URL, canonical, `noindex`), com testes em `pytest`. Peça primeiro um plano, aprove e só então deixe editar.
2. Escreva um arquivo de instruções com três regras do projeto (por exemplo, pausa entre requisições, sem dependência nova sem pedir, testes antes de terminar). Rode a mesma tarefa com e sem o arquivo e compare o resultado.
3. Revise linha a linha o diff gerado. Ache pelo menos um problema (caso de borda, teste que não testa nada, tratamento de erro faltando) e escreva o que pediria para mudar.

**Desafio**
1. Divida uma tarefa maior em partes independentes e rode cada parte num subagente ou numa sessão paralela. Documente como você definiu as regras de cada parte, como juntou o resultado e quantos problemas encontrou na revisão.

## 7. Avaliação (evals) e confiabilidade

**Fixação**
1. Por que a análise de erros vem antes da escolha de métrica?
2. Quando usar avaliação por código, por humano e por modelo? Dê um exemplo de cada para um classificador de intenção de busca.
3. Por que rodar o mesmo eval várias vezes? O que é variância entre execuções e como ela afeta a comparação de dois prompts?

**Prática**
1. Monte 30 casos de teste para o classificador de intenção do módulo 2, rotulados por você, cobrindo casos fáceis, ambíguos e fora do domínio. Guarde num arquivo JSONL.
2. Rode os dois prompts do módulo 2 contra os 30 casos, 3 vezes cada. Reporte acurácia média, desvio e a matriz de confusão.
3. Use um modelo como juiz para avaliar respostas abertas do RAG do módulo 4 (fidelidade de 1 a 5, com rubrica). Avalie as mesmas 20 respostas você mesmo e meça a concordância entre o juiz e você (kappa de Cohen ou porcentagem de acordo).

**Desafio**
1. Transforme o eval em teste de regressão que roda a cada mudança de prompt (um `pytest` ou uma ação do GitHub). Defina um limite mínimo de acurácia e mostre uma mudança de prompt sendo barrada.

## 8. IA local (Whisper, TTS, Ollama, modelos abertos)

**Fixação**
1. O que é quantização e qual é a troca entre tamanho, memória e qualidade? Como estimar a memória que um modelo de 8 bilhões de parâmetros em 4 bits precisa?
2. Qual é a diferença entre a licença de um modelo aberto permissivo (Apache 2.0, MIT) e uma licença com restrições de uso? Onde conferir isso no Hugging Face?
3. Quando é aceitável clonar uma voz? Por que voz sintética ou com autorização por escrito é a única regra segura?

**Prática**
1. Baixe 10 minutos de um audiolivro em português de domínio público no LibriVox. Transcreva com Whisper local (`faster-whisper` ou `whisper.cpp`) em dois tamanhos de modelo. Calcule a taxa de erro de palavra contra o texto original com `jiwer` e compare o tempo.
2. Rode um modelo aberto com Ollama (por exemplo `ollama run qwen2.5:7b` ou `llama3.1:8b`). Compare com um modelo de API nos 30 casos do módulo 7, medindo acerto, tempo e custo.
3. Gere uma narração de um parágrafo com TTS local usando uma voz sintética de licença aberta (Piper ou Kokoro, por exemplo). Transcreva o áudio gerado com Whisper e compare com o texto do roteiro, palavra por palavra.

**Desafio**
1. Monte um pipeline local que recebe um roteiro, gera a narração com TTS, transcreve com Whisper e aponta automaticamente as frases em que a transcrição diverge do roteiro acima de um limite. É o jeito de conferir voz sem ouvir tudo.

## 9. Custo, segurança e prompt injection

**Fixação**
1. Por que tokens de saída costumam custar mais que os de entrada? Como cache de prompt e processamento em lote reduzem a conta?
2. Qual é a diferença entre injeção direta e indireta? Dê um exemplo de injeção indireta escondida numa página web.
3. Liste os três itens do OWASP Top 10 para aplicações com LLM que mais se aplicam a um agente que lê páginas e envia e-mails, e diga a mitigação de cada um.

**Prática**
1. Estime o custo mensal do RAG do módulo 4 antes de escalar. Considere 1.000 perguntas por dia, tokens médios de entrada e saída medidos em 20 chamadas reais e os preços da página oficial do provedor. Monte a planilha com cenário pessimista e otimista.
2. Reduza o custo da mesma tarefa de duas formas. Ative cache de prompt na parte fixa do contexto e troque o modelo por um menor numa etapa simples (por exemplo, a classificação). Meça custo e acerto antes e depois.
3. Crie uma página HTML local com uma instrução escondida (texto branco, comentário HTML ou atributo `alt`) pedindo ao agente para ignorar a tarefa e chamar uma ferramenta de escrita. Rode o agente do módulo 5 sobre ela e registre se ele obedeceu.

**Desafio**
1. Implemente três defesas contra a injeção da prática 3 (dado marcado como não confiável no prompt, ferramentas de escrita com confirmação humana e uma lista fechada de destinos permitidos). Rode 10 variações da injeção e reporte quantas passaram antes e depois de cada defesa.

## Projeto da trilha · Assistente RAG com avaliação

**Objetivo.** Construir um assistente que responde perguntas sobre uma documentação pública citando a fonte, com avaliação automática, exposto por MCP, com custo estimado e testado contra injeção.

**Dados de entrada.** Uma documentação pública com licença aberta, como a do DuckDB (`duckdb/duckdb-web`, MIT), a do dbt (`dbt-labs/docs.getdbt.com`) ou a do Google Search Central (CC BY 4.0). Confira a licença no repositório antes de usar.

**Passos**
1. Baixe a documentação pelo repositório no GitHub (sem crawl do site) e registre a versão usada.
2. Divida em trechos, gere embeddings e monte a busca híbrida com reranking. Justifique o tamanho de trecho com o teste do módulo 3.
3. Escreva o prompt de resposta com dado separado de instrução e citação obrigatória do trecho de origem.
4. Monte um conjunto de 30 perguntas com o trecho esperado e uma resposta de referência. Inclua 5 perguntas que a documentação não responde, em que o certo é dizer que não sabe.
5. Meça recall@5 e precisão@5 da recuperação, fidelidade das respostas (juiz conferido contra você em pelo menos 15 casos) e taxa de recusa correta nas 5 sem resposta.
6. Exponha a busca como ferramenta num servidor MCP somente leitura e use num cliente.
7. Estime o custo mensal para 1.000 perguntas por dia e mostre o efeito do cache de prompt.
8. Teste 10 variações de prompt injection indireta escondidas em trechos da base e documente quais passaram e qual defesa barrou.

**Entregável.** Um repositório no GitHub com `README.md` (arquitetura, como rodar, resultados e custo), o código de indexação e consulta, o servidor MCP, `eval/perguntas.jsonl` com as 30 perguntas, o script de avaliação, `eval/resultados.md` com as métricas, `seguranca.md` com os testes de injeção e `custo.md` com a estimativa. Chaves de API ficam num `.env` fora do Git.

**Critérios de avaliação**
- [ ] A documentação usada tem licença aberta e a versão está registrada
- [ ] Toda resposta cita o trecho de origem e 10 citações foram conferidas à mão
- [ ] O conjunto tem 30 perguntas, 5 delas sem resposta na base
- [ ] Recall@5, precisão@5 e fidelidade estão medidos e reportados com o número de casos
- [ ] O juiz automático foi conferido contra a avaliação humana e a concordância está reportada
- [ ] O assistente diz que não sabe nas perguntas sem resposta
- [ ] O servidor MCP é somente leitura e funciona num cliente real
- [ ] A estimativa de custo usa tokens medidos e preços da página oficial, com data da consulta
- [ ] Os testes de injeção mostram o resultado antes e depois das defesas
- [ ] O eval roda com um comando só e pode ser repetido por outra pessoa
