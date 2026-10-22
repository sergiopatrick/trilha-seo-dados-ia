# Exercícios · 03 · SEO em escala

Como usar. Cada módulo tem exercícios em três níveis. Fixação confere o conceito. Prática aplica num site ou dado real. Desafio pede para ir além. As respostas não estão aqui de propósito. Compare a sua com a documentação oficial citada em leituras.md.

Toda coleta desta trilha segue a mesma regra. Pausa de 2 a 5 segundos entre requisições, user-agent descritivo com contato e parada no primeiro 429.

## 1. SEO programático (templates e bases de dados)

**Fixação**
1. O que separa uma página programática útil de uma que só troca o nome da cidade? Cite 3 diferenças concretas.
2. Explique os padrões de busca X em Y, X para Y e X vs Y com um exemplo de cada no seu nicho.
3. Por que partir da taxonomia que você já tem é o erro mais caro? O que deve ser modelado primeiro?

**Prática**
1. Escolha uma base pública (API de localidades do IBGE, dados.gov.br ou Wikidata) e modele as entidades, os atributos e as relações numa tabela. Diga qual é a chave canônica de cada entidade.
2. Escreva a regra de slug (acentos, caixa, espaços, hífens) e decida o que acontece quando dois itens colidem. Teste a regra em todos os municípios (cerca de 5.570) de `https://servicodados.ibge.gov.br/api/v1/localidades/municipios` e conte as colisões.
3. Gere 20 páginas de teste a partir de um CSV com Python e Jinja2, num template que separa blocos fixos e blocos variáveis.

**Desafio**
1. Liste 10 padrões de busca do seu nicho. Para cada um, confira no autocomplete e na SERP se há demanda e se o top 10 já tem páginas programáticas. Decida quais padrões viram template e justifique com o que você viu.

## 2. Qualidade em escala

**Fixação**
1. O que diz a política de abuso de conteúdo em escala do Google? Ela muda se a página foi feita com ou sem IA?
2. O que torna uma página programática fina? Dê 3 sinais que dá para medir com código.
3. Por que manter `noindex` até a página atingir o limite de dados, em vez de esperar para publicar?

**Prática**
1. Escreva a regra de qualidade do seu projeto, com campos obrigatórios, quantidade mínima de dados e texto próprio mínimo. Implemente como uma função Python que devolve "indexar", "noindex" ou "não gerar".
2. Aplique a regra à base do módulo 1 e mostre quantas páginas caem em cada grupo.
3. Sorteie 20 páginas e revise cada uma manualmente com um checklist. Compare a sua decisão com a da função e ajuste a regra onde as duas discordam.

**Desafio**
1. Escolha um site programático público grande (comparador, guia de cidades, páginas de "melhores X em Y"). Amostre 30 páginas e classifique cada uma pela sua regra. Escreva o que esse site deveria manter indexado e o que deveria tirar, com exemplos.

## 3. Orçamento de rastreio em sites grandes

**Fixação**
1. Explique limite de capacidade de rastreio e demanda de rastreio. O que aumenta e o que reduz cada um?
2. O que é um espaço de URLs infinito? Dê 3 fontes comuns.
3. Por que erros 5xx e respostas lentas fazem o Google rastrear menos?

**Prática**
1. Nas estatísticas de rastreamento do Search Console do seu site, ou num log carregado no DuckDB, meça a fração das requisições que vai para URLs com parâmetro (`WHERE url LIKE '%?%'`).
2. Encontre num site público um espaço de URLs infinito (calendário, filtros combináveis, busca interna indexável, slug inventado que responde 200). Documente com URLs de exemplo, status e meta robots.
3. Proponha regras para fechar o espaço do item anterior, combinando robots.txt, canonical, `noindex` e mudança nos links. Diga a ordem de aplicação e por que ela importa.

**Desafio**
1. Gere com Python um log sintético de 100 mil linhas com proporções realistas entre páginas úteis, filtros, parâmetros e redirecionamentos. Calcule quanto do rastreio é desperdiçado e quantos dias o robô levaria para passar por todas as páginas úteis antes e depois das suas regras. Deixe as premissas explícitas.

## 4. Linkagem interna automatizada e hubs

**Fixação**
1. Explique a diferença entre hub e página-pilar.
2. Quais os riscos de gerar links relacionados por similaridade sem um limite por página?
3. Como um template pode gerar páginas órfãs sem ninguém perceber?

**Prática**
1. Escreva a regra de links relacionados de um template. Diga quantos links, por qual atributo, como desempatar e o que acontece com uma entidade sem pares.
2. Gere os links do seu projeto com a regra e calcule a profundidade de clique de cada página com `networkx`, fazendo uma busca em largura a partir da home. Liste as páginas a mais de 3 cliques.
3. Conte os links de entrada de cada página gerada e encontre as órfãs.

**Desafio**
1. Compare duas regras de links relacionados, uma por atributo (mesmo estado, mesma categoria) e outra por similaridade de embeddings do texto, com um modelo aberto do `sentence-transformers`. Avalie numa amostra de 20 páginas qual gera links mais úteis e meça como cada uma distribui os links de entrada.

## 5. Automação de SEO com Python

**Fixação**
1. A interface do Search Console devolve no máximo 1.000 linhas. Quais as alternativas e o que cada uma entrega?
2. Explique a paginação da API Search Analytics com `rowLimit` e `startRow`. O que fazer quando a cota acaba?
3. Quais os três cuidados ao fatiar a tabela da interface por prefixo de URL e somar depois?

**Prática**
1. Crie um projeto no Google Cloud, ative a API do Search Console e colete 16 meses de dados por página e por busca do seu site. Grave em Parquet.
2. Agende a coleta diária com cron, ou com GitHub Actions usando segredo do repositório, e grave em DuckDB sem duplicar os dias já coletados.
3. Use a API URL Inspection em 20 URLs e grave o estado de indexação e a canonical escolhida pelo Google.

**Desafio**
1. Escreva um alerta que compara a última semana com a média das 4 anteriores por seção (primeiro nível da URL) e avisa quando uma seção perde mais de 20% de cliques. Envie por e-mail ou para um canal seu e explique como você evitou alarme falso (feriado, dias recentes com dado ainda incompleto).

## Projeto da trilha · Projeto programático com dados abertos

**Objetivo.** Construir um pequeno site programático a partir de dados públicos, com regra de qualidade explícita, e provar que cada página publicada merece existir.

**Dados de entrada.** Uma base pública com licença aberta. Sugestões. API de localidades e agregados do IBGE (SIDRA), dados.gov.br, Wikidata ou outra API pública gratuita. A coleta respeita pausa e para no primeiro 429.

**Passos**
1. Escolha um padrão de busca (ex. "X em Y") e valide a demanda com autocomplete, Trends e SERP. Registre as evidências.
2. Modele entidades, atributos e chave canônica. Escreva a regra de slug e o tratamento de colisão.
3. Colete os dados com script, guarde o bruto e gere uma tabela limpa em DuckDB ou Parquet.
4. Escreva a regra de qualidade (campos obrigatórios, mínimo de dados, texto próprio) e classifique cada item em "indexar", "noindex" ou "não gerar".
5. Monte o template com Jinja2, com blocos variáveis que mudam de verdade de uma página para outra (números, comparações, tabelas).
6. Gere pelo menos 50 páginas indexáveis num site estático publicado no GitHub Pages ou similar.
7. Inclua sitemap, canonical, breadcrumbs, links relacionados por regra e dados estruturados de tipos vigentes (BreadcrumbList, Organization, WebSite).
8. Rode um crawl no site publicado e confira status, canonical, profundidade de clique e órfãs.
9. Se publicar num domínio seu, conecte o Search Console e registre a indexação depois de 4 semanas.

**Entregável.** Repositório público com o script de coleta, os dados brutos e limpos, a função de qualidade, o template, o gerador, o site publicado e um `README.md` com padrão de busca, regra de qualidade, números de cada grupo e resultado do crawl.

**Critérios de avaliação**
- [ ] A demanda do padrão de busca tem evidência registrada
- [ ] A fonte de dados é pública, tem licença citada e a coleta respeitou pausa e 429
- [ ] A regra de slug trata colisões e foi testada
- [ ] A regra de qualidade está em código e tem números por grupo
- [ ] Páginas abaixo do limite ficam com `noindex` ou não são geradas
- [ ] Pelo menos 50 páginas indexáveis publicadas, cada uma com dado próprio
- [ ] Sitemap, canonical e breadcrumbs conferidos por crawl
- [ ] Nenhuma página indexável está a mais de 3 cliques da home nem órfã
- [ ] Dados estruturados validados e sem tipos descontinuados
