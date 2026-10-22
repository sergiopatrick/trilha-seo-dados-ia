# Leituras · Engenharia de dados

## 1. Fundamentos e ciclo de vida dos dados

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [Fundamentos de Engenharia de Dados](https://novatec.com.br/livros/fundamentos-de-engenharia-de-dados/) | Joe Reis e Matt Housley (Novatec) | Livro | PT-BR | R$ 165 | A tradução do livro que organiza a área pelo ciclo de vida dos dados. |
| 2 | [The Rise of the Data Engineer](https://www.freecodecamp.org/news/the-rise-of-the-data-engineer-91be18f1e603/) | Maxime Beauchemin (freeCodeCamp) | Artigo | EN | Grátis | O texto que definiu o papel do engenheiro de dados, escrito pelo criador do Airflow. |
| 3 | [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | DataTalksClub | Curso | EN | Grátis | Repositório do curso com código, tarefas e projeto final de cada módulo. |
| 4 | [The Analytics Setup Guidebook](https://www.holistics.io/books/setup-analytics/) | Holistics | Livro grátis | EN | Grátis | Mostra como montar uma pilha de dados analítica do zero, com bom senso de custo. |
| 5 | [Designing Data-Intensive Applications](https://dataintensive.net/) | Martin Kleppmann (O'Reilly) | Livro | EN | Cerca de US$ 60 | A base teórica de armazenamento, replicação, lotes e fluxos para quem quer ir fundo. |

## 2. SQL avançado (CTEs, funções de janela, performance)

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [Select Star SQL](https://selectstarsql.com/) | Zi Chong Kao | Livro grátis | EN | Grátis | Livro interativo que treina SQL em dados reais direto no navegador. |
| 2 | [SQL Window Functions](https://www.thoughtspot.com/sql-tutorial/sql-window-functions) | ThoughtSpot (antigo tutorial da Mode) | Guia | EN | Grátis | Lição prática de ROW_NUMBER, LAG, LEAD e NTILE com editor embutido. |
| 3 | [WITH Queries (Common Table Expressions)](https://www.postgresql.org/docs/current/queries-with.html) | PostgreSQL | Documentação | EN | Grátis | A referência oficial de CTE, inclusive recursiva e com escrita de dados. |
| 4 | [Use The Index, Luke](https://use-the-index-luke.com/) | Markus Winand | Livro grátis | EN | Grátis | O melhor material aberto sobre índice e performance de consulta. |
| 5 | [SQL para Análise de Dados](https://novatec.com.br/livros/sql-para-analise-dados/) | Cathy Tanimura (Novatec) | Livro | PT-BR | R$ 119 | Padrões avançados de SQL para coortes, séries temporais e experimentos. |

## 3. Modelagem dimensional

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [Entenda o esquema em estrela e a importância para o Power BI](https://learn.microsoft.com/pt-br/power-bi/guidance/star-schema) | Microsoft Learn | Documentação | PT-BR | Grátis | Explica fato, dimensão e chave substituta em português, e vale para qualquer BI. |
| 2 | [Dimensional Modeling Techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/) | Kimball Group | Guia | EN | Grátis | O glossário oficial das técnicas Kimball, uma por página. |
| 3 | [Building a Kimball dimensional model with dbt](https://docs.getdbt.com/blog/kimball-dimensional-model) | dbt Developer Blog | Artigo | EN | Grátis | Leva o esquema estrela para o dbt, com código de cada etapa. |
| 4 | [The Data Warehouse Toolkit, 3rd Edition](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/) | Ralph Kimball e Margy Ross | Livro | EN | Cerca de US$ 60 | O livro de referência da modelagem dimensional, com casos por setor. |

## 4. Ingestão, ETL e ELT (inclusive coleta de APIs)

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [ETL x ELT · Diferença entre abordagens de processamento de dados](https://aws.amazon.com/pt/compare/the-difference-between-etl-and-elt/) | AWS | Artigo | PT-BR | Grátis | Comparação direta das duas abordagens, em português. |
| 2 | [REST API source](https://dlthub.com/docs/dlt-ecosystem/verified-sources/rest_api/basic) | dlt Docs | Documentação | EN | Grátis | Coleta de API com paginação, autenticação e carga incremental declaradas em config. |
| 3 | [Tempos limite, novas tentativas e recuo com jitter](https://aws.amazon.com/pt/builders-library/timeouts-retries-and-backoff-with-jitter/) | Marc Brooker (Amazon Builders' Library) | Artigo | PT-BR | Grátis | Ensina a repetir chamadas sem derrubar a API, regra de ouro com limitador. |
| 4 | [How to make data pipelines idempotent](https://www.startdataengineering.com/post/why-how-idempotent-data-pipeline/) | Joseph Machado (Start Data Engineering) | Artigo | EN | Grátis | Mostra como reprocessar um dia sem duplicar nem deixar dado velho. |

## 5. Orquestração (cron, Airflow, Kestra, Prefect)

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [Crontab.guru](https://crontab.guru/) | Cronitor | Ferramenta | EN | Grátis | Traduz a expressão do cron em linguagem comum antes de agendar. |
| 2 | [Airflow 101: Building Your First Workflow](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html) | Apache Airflow | Documentação | EN | Grátis | O tutorial oficial da primeira DAG na versão atual. |
| 3 | [Best Practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) | Apache Airflow | Documentação | EN | Grátis | Evita os erros clássicos de DAG lenta, tarefa não idempotente e código no topo do arquivo. |
| 4 | [Quickstart Guide: Run Your First Kestra Workflow](https://kestra.io/docs/quickstart) | Kestra | Documentação | EN | Grátis | Primeiro fluxo em YAML no Kestra, em poucos minutos. |
| 5 | [Quickstart](https://docs.prefect.io/v3/get-started/quickstart) | Prefect | Documentação | EN | Grátis | Transforma uma função Python em fluxo agendado e monitorado. |

## 6. Data lake e lakehouse (S3, Parquet, Athena, Databricks, DuckDB)

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [O que é um data lakehouse?](https://docs.databricks.com/aws/pt/lakehouse/) | Databricks | Documentação | PT-BR | Grátis | Define lakehouse e a arquitetura em camadas, em português. |
| 2 | [Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) | Armbrust, Ghodsi, Xin e Zaharia (CIDR 2021) | Artigo científico | EN | Grátis | O artigo que formalizou o conceito de lakehouse. |
| 3 | [Particionar dados](https://docs.aws.amazon.com/pt_br/athena/latest/ug/partitions.html) | Amazon Athena | Documentação | PT-BR | Grátis | Particionar no S3 é o que mais reduz custo e tempo de consulta no Athena. |
| 4 | [Top 10 Performance Tuning Tips for Amazon Athena](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/) | AWS Big Data Blog | Artigo | EN | Grátis | Lista prática de formato, compressão, tamanho de arquivo e consulta. |
| 5 | [Reading and Writing Parquet Files](https://duckdb.org/docs/current/data/parquet/overview) | DuckDB | Documentação | EN | Grátis | Lê e grava Parquet local ou no S3 com SQL, sem infraestrutura. |

## 7. Transformação com dbt

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [dbt Fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals) | dbt Learn | Curso | EN | Grátis | O curso oficial de entrada, com modelos, fontes, testes e documentação. |
| 2 | [What is dbt?](https://docs.getdbt.com/docs/introduction) | dbt Developer Hub | Documentação | EN | Grátis | Visão geral do dbt e de onde ele entra num pipeline ELT. |
| 3 | [How we structure our dbt projects](https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview) | dbt Developer Hub | Guia | EN | Grátis | O padrão de staging, intermediate e marts usado no mercado. |
| 4 | [Configure incremental models](https://docs.getdbt.com/docs/build/incremental-models) | dbt Developer Hub | Documentação | EN | Grátis | Processa só o que mudou, essencial em tabela grande e cara. |
| 5 | [04-analytics-engineering](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/04-analytics-engineering) | DataTalksClub | Curso | EN | Grátis | Módulo do Zoomcamp com um projeto dbt completo para reproduzir. |

## 8. Qualidade e observabilidade de dados

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [Add data tests to your DAG](https://docs.getdbt.com/docs/build/data-tests) | dbt Developer Hub | Documentação | EN | Grátis | Testes de unicidade, nulos e relacionamento que rodam junto com o modelo. |
| 2 | [Source freshness](https://docs.getdbt.com/docs/deploy/source-freshness) | dbt Developer Hub | Documentação | EN | Grátis | Alerta quando a fonte parou de atualizar antes do painel mostrar dado velho. |
| 3 | [Great Expectations](https://docs.greatexpectations.io/docs/home/) | Great Expectations | Documentação | EN | Grátis | Validações declarativas em Python para qualquer etapa do pipeline. |
| 4 | [Elementary](https://docs.elementary-data.com/home) | Elementary | Ferramenta | EN | Grátis | Observabilidade aberta feita para dbt, com detecção de anomalia e relatório. |
| 5 | [What Is Data Observability? 5 Key Pillars To Know In 2026](https://montecarlo.ai/blog-what-is-data-observability) | Monte Carlo | Artigo | EN | Grátis | Os cinco pilares de frescor, distribuição, volume, schema e linhagem. |

## 9. BI e painéis (Metabase, Looker Studio)

| # | Leitura | Autor ou fonte | Tipo | Idioma | Custo | Por que ler |
|---|---|---|---|---|---|---|
| 1 | [Learn Metabase](https://www.metabase.com/learn) | Metabase | Curso | EN | Grátis | Trilhas oficiais de consulta, modelagem, painel e administração. |
| 2 | [BI dashboard best practices](https://www.metabase.com/learn/metabase-basics/querying-and-dashboards/dashboards/bi-dashboard-best-practices) | Metabase Learn | Guia | EN | Grátis | Como escolher métricas, filtros e layout para um painel que as pessoas usam. |
| 3 | [Documentação do Data Studio](https://docs.cloud.google.com/data-studio?hl=pt-BR) | Google Cloud | Documentação | PT-BR | Grátis | Referência oficial do Looker Studio, que voltou a se chamar Data Studio. |
| 4 | [Common Pitfalls in Dashboard Design](https://www.perceptualedge.com/articles/Whitepapers/Common_Pitfalls.pdf) | Stephen Few | Artigo | EN | Grátis | Os erros clássicos de painel, explicados por uma referência em design de dashboards. |
