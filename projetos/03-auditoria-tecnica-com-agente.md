# Projeto 3 · Auditoria técnica com agente

Um agente que audita um site como um bom consultor faria. Roda o crawl, levanta hipóteses, testa cada uma com a ferramenta certa e só então escreve o achado, com evidência e solução proposta. O foco é o método, não a quantidade de achados.

**Trilhas.** 02 SEO técnico, 07 IA aplicada, 08 Ofício do consultor.
**Carga estimada.** 15 h.

## Dados de entrada

- Um site público pequeno ou médio (até 5 mil URLs), de preferência seu ou com autorização.
- O Search Console do site, se for seu.

## Ferramentas do agente

Exponha cada uma como ferramenta da API do modelo ou como servidor MCP.

| Ferramenta | O que faz |
|---|---|
| `buscar_url` | Faz a requisição e devolve status, cabeçalhos e cadeia de redirecionamento |
| `extrair_html` | Lê o HTML com parser e devolve title, canonical, meta robots, headings, links e blocos JSON-LD |
| `renderizar` | Abre a página num navegador sem interface e devolve o DOM renderizado |
| `pagespeed` | Consulta a API do PageSpeed Insights (campo e laboratório) |
| `robots_e_sitemap` | Lê robots.txt e sitemaps e devolve as URLs listadas |
| `crawl` | Percorre o site com pausa entre requisições e parada no primeiro 429 |

## Passos

1. **Crawl e inventário.** O agente roda o crawl e monta a lista de templates (home, categoria, produto, artigo).
2. **Hipóteses.** Para cada template, o agente lista hipóteses de problema a partir de um checklist (indexação, canonical, duplicação, performance, dados estruturados, JavaScript, links internos).
3. **Teste.** Cada hipótese só vira achado depois de testada com a ferramenta certa. Status e meta robots sempre juntos. JSON-LD sempre por parser. Slug inventado em toda rota parametrizada.
4. **Rótulo.** Cada achado recebe a origem da evidência e um status (confirmado, parcial, verificação recomendada).
5. **Solução.** Cada achado confirmado traz como deveria ser, com exemplo de código ou configuração.
6. **Priorização.** O agente ordena por impacto e esforço e separa o que o SEO resolve do que precisa de desenvolvimento.
7. **Relatório.** Markdown ou HTML com resumo executivo de uma página e anexo técnico.
8. **Avaliação.** Você confere à mão uma amostra de achados e mede quantos estavam certos.

## Cuidados

- Agente com permissão só de leitura. Nada de enviar formulário ou alterar o site.
- O agente nunca afirma ausência a partir de "a ferramenta não mostrou". Ausência precisa de teste direto.
- Estimativa vem marcada como estimativa.
- Instruções escritas dentro das páginas visitadas são dados, nunca comandos para o agente. Teste isso de propósito com uma página sua.

## Entregável

Repositório público com o código do agente, as ferramentas, o relatório gerado para um site e a planilha de avaliação manual.

## Critérios de avaliação

- [ ] Cada achado do relatório tem evidência rastreável e status
- [ ] A precisão medida na amostra manual está no README
- [ ] O agente resiste a uma instrução maliciosa escondida numa página de teste
- [ ] O resumo executivo cabe em uma página e começa pela conclusão
- [ ] O custo de uma auditoria completa está calculado
