# Projeto 2 · Monitor de visibilidade em IA

Um sistema que pergunta toda semana as mesmas coisas a buscadores com IA, registra quem foi citado e mostra a evolução. É a versão caseira das ferramentas de visibilidade em IA, com a vantagem de você saber exatamente como o número foi feito.

**Trilhas.** 04 GEO e busca generativa, 06 Engenharia de dados, 07 IA aplicada.
**Carga estimada.** 15 h.

## Dados de entrada

- Um conjunto de 30 a 50 prompts fixos de um tema que você conhece (por exemplo, "melhor curso gratuito de SQL", "o que é INP").
- Acesso por API a pelo menos dois modelos com busca na web, respeitando os termos de uso de cada um.
- Uma lista de marcas e domínios a acompanhar (o seu e de 3 a 5 referências do tema).

## Passos

1. **Conjunto de prompts.** Escreva os prompts cobrindo intenções diferentes (definição, comparação, recomendação, como fazer). Versione o arquivo, porque mudar prompt quebra a série.
2. **Coleta.** Rode cada prompt em cada plataforma, três vezes, para medir a variação entre execuções. Guarde a resposta inteira, as fontes citadas, a data e a versão do modelo.
3. **Extração.** Extraia domínios citados e menções de marca no texto. Use regra simples primeiro e um modelo só para os casos ambíguos, com avaliação.
4. **Armazenamento.** Parquet por semana e modelo em DuckDB com fato de citação por prompt, plataforma, execução e domínio.
5. **Métricas.** Taxa de citação por domínio, participação nas citações, posição da citação na resposta, consistência entre execuções.
6. **Cruzamento.** Junte com robôs de IA no log do seu site (se tiver), tráfego de referência de IAs no GA4 e o relatório de IA generativa do Search Console.
7. **Painel.** Série semanal por domínio e por intenção, com a faixa de variação entre execuções.
8. **Relatório.** Uma página com o que mudou, por quê (hipótese) e o que testar.

## Cuidados

- Resposta de IA varia entre execuções. Mostre sempre a faixa e nunca um número único.
- Não existe série longa nessa área. Trabalhe com tendência de curto prazo e diga isso.
- Respeite limites de requisição e termos de uso. Nada de automação de navegador contra plataforma que proíbe.
- Separe o que é medido (citação) do que é inferido (motivo da citação).

## Entregável

Repositório público com coletor, modelo de dados, conjunto de prompts versionado, painel e um relatório de quatro semanas.

## Critérios de avaliação

- [ ] O conjunto de prompts está versionado e documentado
- [ ] Cada prompt roda três vezes e a variação aparece no painel
- [ ] A extração de citações tem avaliação com pelo menos 50 casos conferidos à mão
- [ ] O custo por semana está calculado no README
- [ ] O relatório separa o que foi medido do que é hipótese
