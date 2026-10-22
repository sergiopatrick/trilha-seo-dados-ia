# Vídeos · Engenharia de dados

Ordem sugerida de estudo. Tudo gratuito no YouTube.

## 1. Fundamentos e ciclo de vida dos dados

| # | Vídeo ou playlist | Canal | Idioma | Formato | Por que assistir |
|---|---|---|---|---|---|
| 1 | [Fundamentals of Data Engineering • Matt Housley & Joe Reis • GOTO 2025](https://www.youtube.com/watch?v=VdGVmqiJkeg) | GOTO Conferences | EN | Vídeo | Os autores do livro de referência explicam o ciclo de vida dos dados em meia hora. |
| 2 | [Vocabulary for Data Engineers · Data Engineering 101](https://www.youtube.com/watch?v=TDbjd6Wl6TI) | Seattle Data Guy | EN | Vídeo | Fixa os termos que aparecem em toda a trilha, de pipeline a data warehouse. |
| 3 | [Data Engineering Road Map · How To Learn Data Engineering Quickly( By A FAANG Data Engineer)](https://www.youtube.com/watch?v=SpaFPPByOhM) | Seattle Data Guy | EN | Vídeo | Mostra a ordem prática de estudo e o que pode ficar para depois. |
| 4 | [Data Engineering Zoomcamp](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb) | DataTalksClub ⬛ | EN | Curso completo | O curso aberto mais completo da área, com Docker, ingestão, orquestração, dbt e batch. |

## 2. SQL avançado (CTEs, funções de janela, performance)

| # | Vídeo ou playlist | Canal | Idioma | Formato | Por que assistir |
|---|---|---|---|---|---|
| 1 | [Aprenda SQL · Primeiras Magias na Linguagem dos Dados](https://www.youtube.com/playlist?list=PLvlkVRRKOYFRo651oD0JptVqfQGDvMi3j) | Téo Me Why | PT-BR | Playlist | Curso em português do básico até window functions, com dados reais e exercícios. |
| 2 | [SQL WITH Clause · Clearly Explained · CTEs vs Subqueries vs Temp Tables · Recursive CTEs](https://www.youtube.com/watch?v=LJC8277LONg) | Maven Analytics | EN | Vídeo | Compara CTE, subquery e tabela temporária e mostra quando usar cada uma. |
| 3 | [The Ultimate SQL Window Functions Course · Complete End-to-End Guide](https://www.youtube.com/watch?v=Wvg4PjbMTO8) | Data with Baraa | EN | Curso completo | Cobre ranking, agregação, LAG, LEAD e frames com diagramas muito claros. |
| 4 | [SQL Indexes (Visually Explained) · Clustered vs Nonclustered · #SQL Course 35](https://www.youtube.com/watch?v=BxAj3bl00-o) | Data with Baraa | EN | Vídeo | Explica visualmente como o índice muda o custo de uma consulta. |
| 5 | [Postgres Explain Explained · How Databases Prepare Optimal Query Plans to Execute SQL](https://www.youtube.com/watch?v=P7EUFtjeAmI) | Hussein Nasser | EN | Vídeo | Ensina a ler um plano de execução antes de sair otimizando no escuro. |

## 3. Modelagem dimensional

| # | Vídeo ou playlist | Canal | Idioma | Formato | Por que assistir |
|---|---|---|---|---|---|
| 1 | [Modelagem Relacional x Modelagem Dimensional x Modelagem de Data Lakes](https://www.youtube.com/watch?v=on1pC7swq18) | Data Science Academy | PT-BR | Vídeo | Situa a modelagem dimensional entre as outras em poucos minutos. |
| 2 | [Data Modeling Tutorial: Star Schema (aka Kimball Approach)](https://www.youtube.com/watch?v=gRE3E7VUzRU) | Kahan Data Solutions | EN | Vídeo | Monta um esquema estrela passo a passo, com fato e dimensões. |
| 3 | [Dimensional Modeling](https://www.youtube.com/watch?v=lWPiSZf7-uQ) | Bryan Cafferky | EN | Vídeo | Aula longa e didática sobre grão, fatos, dimensões e o método Kimball. |
| 4 | [Data Modeling · Slowly Changing Dimensions and Idempotency · Day 2 Lecture · DataExpert.io Boot Camp](https://www.youtube.com/watch?v=emQM9gYh0Io) | DataExpert | EN | Vídeo | Aprofunda dimensões que mudam no tempo e cargas que podem rodar de novo sem duplicar. |
| 5 | [Kimball in the context of the modern data warehouse: what's worth keeping, and what's not](https://www.youtube.com/watch?v=3OcS2TMXELU) | dbt Labs | EN | Vídeo | Discute o que ainda vale do Kimball num warehouse em nuvem. |

## 4. Ingestão, ETL e ELT (inclusive coleta de APIs)

| # | Vídeo ou playlist | Canal | Idioma | Formato | Por que assistir |
|---|---|---|---|---|---|
| 1 | [ETL vs ELT · Arquitetura de Dados](https://www.youtube.com/watch?v=YNGHRSWp7nM) | Faculdados | PT-BR | Vídeo | Explica em português a diferença entre transformar antes ou depois de carregar. |
| 2 | [Introdução ao Python 12: Dados de API](https://www.youtube.com/watch?v=iBsyZ0RQCqc) | Téo Me Why | PT-BR | Vídeo | Coleta dados de API com Python, do request ao arquivo salvo. |
| 3 | [Ingestão de Dados de APIs com Python, Docker e Airflow](https://www.youtube.com/watch?v=ewZCaiyunAk) | Apoena Stack - Iury Rosal | PT-BR | Vídeo | Projeto completo de ingestão de API, já agendado e em contêiner. |
| 4 | [Data Ingestion From APIs to Warehouses and Data Lakes · Violetta Mishechkina](https://www.youtube.com/watch?v=pgJWP_xqO1g) | DataTalksClub ⬛ | EN | Vídeo | Workshop com dlt que cobre paginação, carga incremental e schema. |
| 5 | [SQL Data Warehouse from Scratch · Full Hands-On Data Engineering Project](https://www.youtube.com/watch?v=9GVqKuTVANE) | Data with Baraa | EN | Curso completo | Projeto de ETL de ponta a ponta com camadas bronze, prata e ouro. |

## 5. Orquestração (cron, Airflow, Kestra, Prefect)

| # | Vídeo ou playlist | Canal | Idioma | Formato | Por que assistir |
|---|---|---|---|---|---|
| 1 | [Cron, crontab e cronjob: agendando tarefas automáticas](https://www.youtube.com/watch?v=TG--rQkZvGc) | WDEV | PT-BR | Vídeo | O agendamento mais simples, que resolve boa parte dos casos pequenos. |
| 2 | [Aprenda Airflow RÁPIDO para Engenharia de Dados](https://www.youtube.com/watch?v=4DGRqMoyrPk) | Codifike | PT-BR | Vídeo | Introdução rápida em português a DAGs, tarefas e agendamento. |
| 3 | [Airflow Tutorial for Beginners · Full Course in 2 Hours 2022](https://www.youtube.com/watch?v=K9AnJ9_ZAXE) | coder2j | EN | Curso completo | Curso prático de Airflow com operadores, XCom, sensores e conexões. |
| 4 | [DE Zoomcamp 2.2.1 · Workflow Orchestration Introduction](https://www.youtube.com/watch?v=Np6QmmcgLCs) | Kestra | EN | Vídeo | Explica o que um orquestrador resolve e apresenta o Kestra no Zoomcamp. |
| 5 | [Getting Started with Prefect · Task Orchestration & Data Workflows](https://www.youtube.com/watch?v=D5DhwVNHWeU) | Kahan Data Solutions | EN | Vídeo | Mostra o Prefect como alternativa leve, em Python puro. |

## 6. Data lake e lakehouse (S3, Parquet, Athena, Databricks, DuckDB)

| # | Vídeo ou playlist | Canal | Idioma | Formato | Por que assistir |
|---|---|---|---|---|---|
| 1 | [Data Warehouse / Data Lake / Data Lakehouse // Dicionário do Programador](https://www.youtube.com/watch?v=V07Pk4de-5M) | Código Fonte TV | PT-BR | Vídeo | Diferencia os três conceitos em português e sem jargão. |
| 2 | [Parquet File Format · Explained to a 5 Year Old!](https://www.youtube.com/watch?v=5NA57Pfpdr4) | Data Mozart | EN | Vídeo | Mostra por que o formato colunar deixa a consulta mais barata e rápida. |
| 3 | [Consulte dados com o AWS Athena · Português](https://www.youtube.com/watch?v=npe9RcSTIzI) | AWS Developers LATAM | PT-BR | Vídeo | Consulta arquivos no S3 com SQL pelo Athena, em português. |
| 4 | [DuckDB Tutorial For Beginners In 12 min](https://www.youtube.com/watch?v=ZX5FdqzGT1E) | MotherDuck | EN | Vídeo | Analisa Parquet e CSV localmente com SQL, sem servidor. |
| 5 | [Lago do Mago](https://www.youtube.com/playlist?list=PLvlkVRRKOYFTcLehYZ2Bd5hGIcLH0dJHE) | Téo Me Why | PT-BR | Playlist | Monta um lakehouse no Databricks com CDC, camadas e painel final. |

## 7. Transformação com dbt

| # | Vídeo ou playlist | Canal | Idioma | Formato | Por que assistir |
|---|---|---|---|---|---|
| 1 | [What Is DBT and Why Is It So Popular ·  Intro To Data Infrastructure Part 3](https://www.youtube.com/watch?v=8FZZivIfJVo) | Seattle Data Guy | EN | Vídeo | Explica o problema que o dbt resolve antes de entrar na ferramenta. |
| 2 | [dbt Core com PostgreSQL · Transformação de Dados na Prática em 10 MINUTOS!](https://www.youtube.com/watch?v=UF1PaO87FvM) | Jornada de Dados - Luciano Vasconcelos | PT-BR | Vídeo | Primeiro projeto dbt rodando em Postgres, em português. |
| 3 | [Primeiros passos com DBT · Live #13](https://www.youtube.com/watch?v=ZPYmgt4zE7M) | Engenharia de Dados Academy | PT-BR | Vídeo | Live em português com modelos, fontes e testes do zero. |
| 4 | [dbt (data build tool) Crash Course For Beginners (dbt Core) · Full Tutorial](https://www.youtube.com/watch?v=toSAAgLUHuk) | Jie Jenn | EN | Vídeo | Curso rápido com modelos, materializações, seeds e macros. |

## 8. Qualidade e observabilidade de dados

| # | Vídeo ou playlist | Canal | Idioma | Formato | Por que assistir |
|---|---|---|---|---|---|
| 1 | [What is Data Observability?](https://www.youtube.com/watch?v=jfg9wBJBtKk) | IBM Technology | EN | Vídeo | Define observabilidade de dados e os sinais que vale monitorar. |
| 2 | [O que é Data Quality? na teoria e na prática... Com ferramenta SODA](https://www.youtube.com/watch?v=F2HFRKKdyz4) | Wallace Camargo | PT-BR | Vídeo | Junta teoria de qualidade de dados e checagens práticas com Soda. |
| 3 | [DBT Tests · Data Build Tool · Singular · Generic · Custom · Prebuild · Source Freshness](https://www.youtube.com/watch?v=OpsQfyrWTs8) | SleekData | EN | Vídeo | Mostra todos os tipos de teste do dbt, inclusive o de atualização da fonte. |
| 4 | [Great Expectation Tutorial · Mastering Data Quality](https://www.youtube.com/watch?v=oxOj30rl_xs) | Anuj Syal | EN | Vídeo | Escreve validações em Python com Great Expectations. |

## 9. BI e painéis (Metabase, Looker Studio)

| # | Vídeo ou playlist | Canal | Idioma | Formato | Por que assistir |
|---|---|---|---|---|---|
| 1 | [CONHEÇA O METABASE · GUIA COMPLETO PELA FERRAMENTA](https://www.youtube.com/watch?v=HSIZPK4kdIw) | Gabriel Santos | PT-BR | Vídeo | Tour completo do Metabase em português, de pergunta a painel. |
| 2 | [How to create a dashboard · Getting started with Metabase](https://www.youtube.com/watch?v=W-i9E5_Wjmw) | Metabase | EN | Vídeo | O passo a passo oficial para montar o primeiro painel com filtros. |
| 3 | [Tutorials: Charts and visualizations in Metabase](https://www.youtube.com/playlist?list=PLzmftu0Z5MYGgFvWfgmvW6V2X_gqAl1rL) | Metabase | EN | Playlist | Ensina a escolher e configurar cada tipo de gráfico. |
| 4 | [AULA Data Studio do ZERO para INICIANTES (ATUALIZADO) Aprenda Rápido! Antigo Looker Studio](https://www.youtube.com/watch?v=7iI-UTHqPLA) | Pedro Paiva Dashboards | PT-BR | Vídeo | Aula completa em português do Looker Studio, que voltou a se chamar Data Studio. |
| 5 | [12 Dashboard design tips for better data visualization](https://www.youtube.com/watch?v=t3cAUt7sOQg) | Geckoboard | EN | Vídeo | Regras curtas de layout e leitura que servem para qualquer ferramenta. |
