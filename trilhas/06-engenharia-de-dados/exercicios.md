# Exercícios · 06 · Engenharia de dados

Como usar. Cada módulo tem exercícios em três níveis. Fixação confere o conceito. Prática aplica num site ou dado real. Desafio pede para ir além. As respostas não estão aqui de propósito. Compare a sua com a documentação oficial citada em [leituras.md](leituras.md).

Ferramentas gratuitas usadas aqui. Python 3.12, DuckDB, dbt Core com o adaptador `dbt-duckdb`, Docker (para Metabase e Kestra) e o sandbox gratuito do BigQuery. Os dados são públicos. Viagens de táxi de Nova York (NYC TLC Trip Record Data, em Parquet), o projeto Jaffle Shop do dbt, a API de agregados do IBGE (https://servicodados.ibge.gov.br/api/docs/agregados), a API de pageviews da Wikimedia e o Search Console do seu próprio site. Em toda API, pause entre as requisições, mande um User-Agent descritivo e pare no primeiro 429.

## 1. Fundamentos e ciclo de vida dos dados

**Fixação**
1. Nomeie as cinco etapas do ciclo de vida da engenharia de dados e as correntes que passam por baixo delas. Para cada etapa, cite uma ferramenta.
2. Explique a diferença entre OLTP e OLAP pensando num e-commerce. Que pergunta cada um responde bem e qual responde mal?
3. Quando batch resolve e quando streaming se paga? Dê um exemplo de dado de SEO ou marketing para cada caso.

**Prática**
1. Desenhe num diagrama (Mermaid ou Excalidraw) o caminho de um dado que você usa no trabalho ou nos estudos, por exemplo os cliques do Search Console, da origem ao painel. Marque em cada etapa onde ele fica guardado, quem transforma e com que frequência.
2. Compare data warehouse, data lake e lakehouse numa tabela com custo de armazenamento, custo de processamento, formato do dado e quem consulta. Use os preços públicos do BigQuery e do Athena para preencher as linhas de custo.

**Desafio**
1. Uma empresa pequena quer juntar Search Console, GA4 e um CRM com 50 mil contatos. Escreva em uma página a arquitetura mais barata que funciona, com estimativa de custo mensal, e diga em que volume ou dor ela deixaria de servir.

## 2. SQL avançado

**Fixação**
1. Qual é a diferença entre `ROW_NUMBER`, `RANK` e `DENSE_RANK` quando há empate?
2. Explique por que um join entre uma tabela diária de cliques e uma tabela de páginas com uma linha por categoria pode multiplicar o total. Como você detecta isso antes de publicar o número?
3. O que é poda de partição e por que um filtro numa coluna transformada (por exemplo `CAST(data AS VARCHAR)`) pode desligá-la?

**Prática**
1. No DuckDB, leia direto da URL um mês de táxi amarelo de Nova York (`read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet')`). Resolva 10 perguntas com funções de janela. Exemplos. Ranking das 10 zonas de embarque por dia, receita acumulada no mês, variação dia contra dia com `LAG`, variação contra o mesmo dia da semana anterior, média móvel de 7 dias e participação de cada zona no total do dia com `SUM() OVER`.
2. Monte uma tabela com duplicatas de propósito (o mesmo `mql_id` ou id de pedido coletado em três cargas com datas diferentes). Deduplique mantendo a linha mais recente por chave com `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ... DESC)` e prove com uma contagem que sobrou uma linha por chave.
3. Rode `EXPLAIN ANALYZE` numa consulta lenta sobre um ano de dados de táxi. Reescreva lendo só as colunas e os meses necessários e compare o dado lido e o tempo.

**Desafio**
1. Escreva uma consulta que compare cada dia de um mês com o mesmo dia da semana do mês anterior (alinhando pela posição na semana) e mostre o efeito de não alinhar. Use os dados de táxi ou os cliques do seu Search Console.

## 3. Modelagem dimensional

**Fixação**
1. O que é granularidade de uma tabela fato? Escreva a granularidade de uma tabela de cliques do Search Console por busca, página, país, dispositivo e data em uma frase.
2. Qual é a diferença entre SCD tipo 1 e tipo 2? Dê um exemplo de atributo de página (categoria, autor, status de indexação) que pede cada tipo.
3. Explique as camadas bronze, prata e ouro e quando uma One Big Table é melhor que o esquema estrela.

**Prática**
1. Rode o Jaffle Shop do dbt com DuckDB e identifique quais modelos são fatos e quais são dimensões. Desenhe o esquema estrela resultante.
2. Modele Search Console, GA4 e um CRM de exemplo (o conjunto "Marketing Funnel by Olist", do Kaggle) num esquema estrela. Defina por escrito a granularidade de cada fato, as dimensões compartilhadas (data, página, canal) e as chaves substitutas.

**Desafio**
1. Implemente um SCD tipo 2 para uma dimensão de páginas em que a categoria muda ao longo do tempo. Use `dbt snapshot` ou SQL puro com `valido_de` e `valido_ate`. Mostre uma consulta que atribui os cliques de cada dia à categoria que a página tinha naquele dia.

## 4. Ingestão, ETL e ELT

**Fixação**
1. Qual é a diferença entre ETL e ELT e por que ELT ficou comum com warehouses na nuvem?
2. O que torna uma carga idempotente? Cite duas técnicas (substituir partição, merge por chave).
3. Descreva o que o pipeline deve fazer ao receber um 429. Por que tentar de novo em laço sem espera é pior que parar?

**Prática**
1. Escreva em Python uma ingestão incremental da API de agregados do IBGE ou da API de pageviews da Wikimedia. Guarde num arquivo de estado a última data carregada e, na próxima execução, peça só o que falta. Ponha uma pausa entre as requisições e pare no primeiro 429, gravando de onde parou.
2. Grave a saída em Parquet particionado por data (`ano=2026/mes=10/dia=21/`). Rode a mesma carga duas vezes no mesmo dia e prove com `SELECT COUNT(*)` e uma contagem por chave que nada duplicou.
3. Faça a mesma ingestão com o `dlt` e compare com o seu script. O que ele resolve sozinho (esquema, estado, paginação) e o que você ainda precisou escrever?

**Desafio**
1. Escreva uma ingestão incremental da API do Search Console do seu site, por data, busca e página. Respeite que a série é publicada até dois dias antes e que o dia publicado não muda depois. Paginação por `startRow` até a resposta vir vazia. Documente a decisão sobre recarregar ou não os últimos dias e justifique com uma comparação entre duas coletas.

## 5. Orquestração

**Fixação**
1. O que é uma DAG e por que dependência explícita é melhor que agendar duas tarefas com 10 minutos de diferença?
2. Qual é a diferença entre um alerta de "falhou" e um alerta de "não rodou"? Por que o segundo é o que costuma faltar?
3. Explique backfill e o cuidado que ele exige com cotas de API.

**Prática**
1. Agende o pipeline do módulo 4 com cron. Cada execução grava uma linha num log com início, fim, linhas carregadas e status. Rode a primeira execução olhando e confirme que nenhuma permissão ficou esperando aprovação.
2. Suba o Kestra com Docker e reescreva o mesmo pipeline como um flow com duas tarefas (ingerir e transformar), novas tentativas com espera, tempo limite e uma notificação quando falhar. Force uma falha e mostre o alerta chegando.
3. Faça um backfill de 30 dias usando o mesmo flow, respeitando a pausa entre requisições.

**Desafio**
1. Crie uma verificação independente do orquestrador que confere, todo dia às 9h, se a tabela recebeu dados nas últimas 24 horas e avisa se não recebeu. Teste desligando o agendamento e mostrando que o aviso dispara.

## 6. Data lake e lakehouse

**Fixação**
1. Por que Parquet consulta mais rápido e mais barato que CSV para análise? Fale de armazenamento colunar, compressão e estatísticas por bloco.
2. Como o Athena cobra uma consulta? O que particionamento e seleção de colunas mudam nesse valor?
3. O que Delta Lake e Iceberg acrescentam a um monte de arquivos Parquet num bucket?

**Prática**
1. Monte um mini data lake local com 12 meses de táxi amarelo em Parquet, particionado por ano e mês. Consulte com DuckDB usando `hive_partitioning = true` e mostre que um filtro por mês lê só uma partição.
2. Estime o custo da mesma consulta no Athena antes e depois de particionar. Use o tamanho dos arquivos lidos e o preço por TB publicado na página oficial do Athena.
3. Converta um mês de CSV em Parquet com compressão `zstd` e `snappy`. Compare tamanho em disco e tempo de consulta.

**Desafio**
1. Faça o curso introdutório gratuito de uma plataforma lakehouse (Databricks, por exemplo). Depois recrie localmente uma tabela Delta ou Iceberg com DuckDB ou `deltalake` em Python, faça uma atualização e consulte a versão anterior (time travel).

## 7. Transformação com dbt

**Fixação**
1. Qual é a diferença entre `ref` e `source` e o que cada um faz no grafo de linhagem?
2. Quando usar materialização view, table e incremental? Qual é o risco de um modelo incremental sem `unique_key`?
3. Qual é a diferença entre teste genérico e teste singular? Dê um exemplo de cada para uma tabela de cliques.

**Prática**
1. Crie um projeto dbt com `dbt-duckdb` sobre os Parquet do módulo 4 ou 6, com três camadas (`staging`, `intermediate` e `marts`). Declare as fontes em `sources.yml`.
2. Escreva testes `unique`, `not_null` e `relationships` nos modelos e um teste singular que falha se a soma de cliques no mart for diferente da soma na fonte.
3. Gere a documentação com `dbt docs generate` e `dbt docs serve` e salve uma captura do grafo de linhagem.

**Desafio**
1. Transforme o mart principal em modelo incremental com `unique_key` e estratégia `delete+insert`. Rode duas vezes, reprocesse os últimos 3 dias e prove que o total não mudou nem duplicou.

## 8. Qualidade e observabilidade de dados

**Fixação**
1. Explique os quatro tipos de teste de dado (esquema, volume, frescor e distribuição) com um exemplo de falha real de cada.
2. O que é um contrato de dados e em que ele difere de um teste?
3. Por que reconciliar com a fonte acha erros que testes de unicidade e não nulo não acham?

**Prática**
1. Configure `source freshness` no dbt com `error_after` de 2 dias na fonte do Search Console ou da API pública. Faça falhar de propósito parando a ingestão.
2. Reconcilie a tabela transformada com o total da fonte. Para o Search Console, compare a soma por página com o total da propriedade no mesmo período e explique a diferença. Liste as páginas que ficaram de fora, se houver.
3. Escreva um alerta de volume que dispara quando as linhas ou os cliques de um dia caem mais de 30% contra a média dos mesmos dias da semana nas 4 semanas anteriores.

**Desafio**
1. Monte um relatório diário de qualidade (uma tabela no próprio DuckDB) com o resultado de cada teste, a hora e a quantidade de linhas afetadas. Mostre a evolução de 14 dias e escreva qual teste mais falhou e por quê.

## 9. BI e painéis

**Fixação**
1. Qual é a diferença entre painel de TV e painel analítico? Dê um exemplo de quem usa cada um.
2. Por que definir uma métrica uma vez, num só lugar, evita discussão em reunião? Onde ela deve morar no seu projeto (dbt, camada semântica, ferramenta de BI)?
3. Um gestor pede um parágrafo explicando cada gráfico do painel semanal. O que você propõe no lugar?

**Prática**
1. Suba o Metabase com `docker run -d -p 3000:3000 metabase/metabase`. Conecte aos marts do dbt (pelo driver DuckDB da comunidade ou exportando os marts para Postgres). Monte um painel com filtros de data, página e dispositivo.
2. Para cada gráfico do painel, escreva a pergunta que ele responde e a ação que o gestor toma depois de olhar. Corte o que não tiver ação.
3. Defina cada métrica do painel (cliques, CTR, posição média, sessões) uma vez, no dbt ou no modelo semântico do Metabase, e prove que dois gráficos usam a mesma definição.

**Desafio**
1. Meça o tempo de carga do painel com um ano de dados. Se passar de 5 segundos, resolva com agregação prévia num mart, cache ou divisão em abas, e registre o antes e depois.

## Projeto da trilha · Pipeline de SEO de ponta a ponta

**Objetivo.** Construir um pipeline que roda sozinho todo dia, da API ao painel, com ingestão incremental, testes e alerta. É a versão de bolso de um data warehouse de SEO.

**Dados de entrada.** A API do Search Console do seu próprio site. Se você não tem site com tráfego, use a API de pageviews da Wikimedia para um conjunto de artigos da Wikipédia em português.

**Passos**
1. Desenhe o ciclo de vida do dado (origem, ingestão, armazenamento, transformação, consumo) num diagrama Mermaid no README.
2. Escreva a ingestão incremental em Python, com arquivo de estado, paginação, pausa entre requisições e parada no primeiro 429.
3. Grave em Parquet particionado por data e prove a idempotência rodando duas vezes.
4. Consulte com DuckDB e crie um projeto dbt com `staging`, `intermediate` e `marts`, com a granularidade de cada fato escrita.
5. Escreva testes de unicidade, não nulo, relacionamento, frescor de 2 dias e reconciliação com a fonte.
6. Orquestre com cron ou Kestra, com novas tentativas, log de execução e alerta para "falhou" e para "não rodou".
7. Faça um backfill de 30 dias.
8. Monte um painel no Metabase com filtros e no máximo 6 gráficos, com cada métrica definida uma vez.

**Entregável.** Um repositório no GitHub com `README.md` (diagrama, como rodar e custo estimado), `ingestao/`, o projeto dbt, a definição do orquestrador (crontab ou flow do Kestra), `docker-compose.yml` do Metabase e uma pasta `evidencias/` com o log de 7 dias de execução, a captura do grafo do dbt e a do painel. Credenciais ficam fora do repositório, num `.env` listado no `.gitignore`, com um `.env.exemplo` sem valores reais.

**Critérios de avaliação**
- [ ] A ingestão é incremental e retoma de onde parou
- [ ] O pipeline para no primeiro 429 e registra o ponto de retomada
- [ ] Rodar duas vezes no mesmo dia não duplica nenhuma linha
- [ ] O Parquet está particionado por data e a consulta por período lê só as partições necessárias
- [ ] O dbt tem três camadas e a granularidade de cada fato está documentada
- [ ] Há testes de unicidade, não nulo, relacionamento, frescor e reconciliação, todos passando
- [ ] O orquestrador tem novas tentativas e alertas para falha e para ausência de execução
- [ ] O backfill de 30 dias rodou sem estourar a cota da API
- [ ] O painel tem filtros, no máximo 6 gráficos e métricas definidas num só lugar
- [ ] Nenhuma credencial está no histórico do Git
