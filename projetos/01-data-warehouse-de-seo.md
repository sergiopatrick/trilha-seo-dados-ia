# Projeto 1 · Data warehouse de SEO

Um pequeno data warehouse que junta Search Console, GA4 e crawl do seu site, atualiza sozinho todo dia e alimenta um painel. É o projeto que mostra, num só repositório, que você entende SEO, mensuração e engenharia de dados.

**Trilhas.** 02 SEO técnico, 05 Mensuração, 06 Engenharia de dados.
**Carga estimada.** 15 a 20 h.

## Dados de entrada

- Search Console de um site seu (blog, portfólio ou projeto pessoal). Se não tiver, crie um site estático e espere algumas semanas de dados.
- GA4 do mesmo site, ou o dataset público do GA4 no BigQuery (`bigquery-public-data.ga4_obfuscated_sample_ecommerce`) para praticar a modelagem.
- Crawl do site, feito pelo seu próprio script da trilha 00.

## Arquitetura

```
API do Search Console ─┐
API do GA4 ou BigQuery ─┼─> ingestão em Python ─> Parquet (bronze) ─> dbt + DuckDB (prata e ouro) ─> painel
Crawl próprio ─────────┘                         particionado por data       testes e documentação
                                                  orquestrado por cron ou Kestra, com alerta
```

## Passos

1. **Ingestão do Search Console.** Coleta diária por página, busca, país e dispositivo, incremental e idempotente. Respeite a cota e grave em Parquet particionado por data.
2. **Ingestão do GA4.** Sessões e conversões por página de entrada e canal. Use a Data API ou a exportação para BigQuery.
3. **Crawl semanal.** Status, title, canonical, meta robots, profundidade e contagem de links internos.
4. **Modelagem com dbt.** Camada staging (limpeza e tipos), intermediate (normalizar URL, que é a chave entre as três fontes) e marts (fato diário por página, dimensão de página com atributos do crawl).
5. **Testes.** Unicidade da chave, não nulo, frescor de no máximo 3 dias, e reconciliação do total de cliques com o total da API.
6. **Orquestração.** Agende tudo e grave um log de execução. Alerte quando falhar e quando não rodar.
7. **Painel.** Metabase ou Looker Studio com cliques, impressões, CTR e posição por seção, conversões orgânicas por página e páginas indexáveis sem clique.
8. **Documentação.** README com arquitetura, como rodar, decisões tomadas e limites conhecidos.

## Armadilhas que valem pontos se você tratar

- URL em formatos diferentes nas três fontes (barra final, parâmetros, maiúsculas, http e https).
- Buscas anonimizadas no Search Console. O total por página é maior que a soma das buscas.
- Série do Search Console publicada até dois dias antes. Não trate os últimos dias como incompletos sem testar.
- Comparação de período alinhada por dia da semana.

## Entregável

Um repositório público com código, modelos dbt, testes, documentação gerada e capturas do painel. Sem chaves de API versionadas.

## Critérios de avaliação

- [ ] Rodar duas vezes no mesmo dia não duplica dados
- [ ] Todos os testes do dbt passam e cobrem as chaves das três fontes
- [ ] O total de cliques do modelo bate com o total da API
- [ ] Existe alerta para falha e para ausência de execução
- [ ] O painel responde em uma tela quais seções ganharam e perderam cliques e por quê (volume ou CTR)
- [ ] O README explica como outra pessoa roda o projeto do zero
