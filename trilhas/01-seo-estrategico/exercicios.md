# Exercícios · 01 · SEO estratégico

Como usar. Cada módulo tem exercícios em três níveis. Fixação confere o conceito. Prática aplica num site ou dado real. Desafio pede para ir além. As respostas não estão aqui de propósito. Compare a sua com a documentação oficial citada em leituras.md.

Vários exercícios usam o Search Console. Se você ainda não tem um site, crie um blog gratuito, publique 5 textos e conecte a propriedade. Em poucas semanas já há dado para trabalhar.

## 1. Como o Google funciona e a busca hoje

**Fixação**
1. Explique as três etapas do Google (rastreio, indexação e veiculação) e dê um exemplo de falha típica de cada uma.
2. O que é um core update? Por que uma queda logo depois dele raramente se resolve com correção técnica?
3. Por que separar busca de marca e busca genérica muda a leitura de um relatório de tráfego orgânico?

**Prática**
1. Leia o guia de como a busca funciona e o guia de sistemas de ranqueamento do Search Central. Escolha 3 sistemas e escreva um parágrafo sobre cada um, dizendo que tipo de página ele favorece ou rebaixa.
2. No relatório de desempenho do Search Console do seu site, filtre as buscas com uma regex de marca (ex. `minhamarca|minha marca|mnhamarca`) e depois com a opção que exclui a regex. Compare cliques, impressões e CTR dos dois grupos nos últimos 3 meses.
3. Abra o changelog da documentação do Search Central e liste 5 mudanças dos últimos 12 meses. Marque quais contradizem alguma recomendação que você já viu circular em blog.

**Desafio**
1. Pegue 20 buscas do seu tema e anote, em cada SERP, se há AI Overview, featured snippet, vídeos, "as pessoas também perguntam" ou anúncios. Faça em janela anônima e registre data, cidade e dispositivo. Classifique quais buscas tendem a zero clique e escreva o critério que usou.

## 2. Intenção de busca e pesquisa de palavras-chave

**Fixação**
1. Defina as intenções informacional, navegacional, comercial e transacional e dê um exemplo de busca para cada uma dentro do mesmo tema.
2. Explique o agrupamento por SERP. Por que duas buscas com palavras diferentes podem pedir a mesma página?
3. Por que o volume de ferramenta é uma estimativa? Que dado do seu próprio site ajuda a corrigir essa estimativa?

**Prática**
1. Escolha um nicho e colete 50 buscas a partir do autocomplete do Google, do bloco "as pessoas também perguntam" e das consultas relacionadas do Google Trends. Classifique cada uma por intenção numa planilha.
2. Para 10 pares de buscas parecidas, compare o top 10 orgânico de cada uma. Conte quantas URLs se repetem e decida, com uma regra escrita (ex. 4 ou mais URLs em comum viram uma página só), se o par pede uma página ou duas.
3. No Search Console do seu site, encontre uma busca em que duas URLs revezam. Use o filtro de busca exata, abra a aba de páginas e compare as impressões de cada URL semana a semana.

**Desafio**
1. Cruze 30 buscas da sua planilha com as impressões reais do Search Console do seu site. Mostre onde a estimativa de volume da ferramenta mais errou e proponha uma regra de prioridade que combine as duas fontes.

## 3. Arquitetura de informação e linkagem interna

**Fixação**
1. O que é profundidade de clique? Por que páginas a 5 ou mais cliques da home tendem a ser menos rastreadas e menos fortes?
2. Explique hub e cluster de tópico com um exemplo do seu nicho.
3. Quando uma taxonomia de tags vira problema? Descreva o caso em que ela gera páginas finas.

**Prática**
1. Rode um crawl num site público pequeno com o Screaming Frog (a versão gratuita vai até 500 URLs) ou com um crawler em Python com pausa entre requisições e parada no primeiro 429. Exporte a profundidade de cada URL e liste as páginas que dão dinheiro e estão a mais de 3 cliques da home.
2. Cruze as URLs do sitemap com as URLs encontradas no crawl. As que estão no sitemap e não aparecem no crawl são candidatas a órfãs. Confira 5 delas manualmente.
3. Escolha um tema do site e proponha 10 links internos entre páginas desse tema, com página de origem, página de destino e texto âncora descritivo.

**Desafio**
1. Desenhe a arquitetura de um site do seu nicho como um hub de entidades. Mostre num diagrama Mermaid as entidades, as páginas que já existem e as relações de muitos para muitos entre elas. Aponte onde a taxonomia atual mistura categoria editorial com entidade.

## 4. Conteúdo, E-E-A-T e atualizações de algoritmo

**Fixação**
1. Explique cada letra de E-E-A-T. Por que as diretrizes dos avaliadores tratam a confiança como a mais importante?
2. O que é YMYL? Dê dois exemplos de páginas YMYL e dois de páginas que ficam fora dessa categoria.
3. O que é ganho de informação? Dê um exemplo de dado próprio que um site do seu nicho poderia publicar.

**Prática**
1. Escolha 3 páginas de um concorrente e aplique as perguntas de autoavaliação do guia de conteúdo útil do Google a cada uma. Dê nota de 1 a 5 por pergunta e justifique as notas baixas.
2. Encontre uma página YMYL do seu nicho e liste os sinais de autoria e revisão visíveis (autor, credencial, revisor, data de atualização, fontes). Diga o que falta.
3. Escreva um briefing de conteúdo para uma busca da sua planilha do módulo 2, com intenção, ângulo próprio, estrutura de seções, fontes primárias e quem assina.

**Desafio**
1. Proponha um ativo de dado próprio para o seu nicho, como um levantamento, uma calculadora ou uma base consultável. Descreva de onde vêm os dados, como serão atualizados e que buscas ele atende. Faça um protótipo simples com dado público.

## 5. Links, autoridade e digital PR

**Fixação**
1. Explique em poucas frases a ideia original do PageRank e o que mudou desde então.
2. Diferencie `rel=nofollow`, `sponsored` e `ugc` e diga quando usar cada um.
3. O que a política de spam do Google chama de esquema de links? Dê 3 exemplos.

**Prática**
1. Use o relatório de links do Search Console do seu site ou uma ferramenta gratuita de backlinks (Ahrefs Webmaster Tools para site verificado, ou a cota grátis do Moz Link Explorer). Classifique 30 domínios de referência em editorial, diretório, perfil, spam ou outro.
2. Procure 10 menções a uma marca do seu nicho sem link, com a busca entre aspas e o próprio domínio excluído com `-site:dominio.com.br`. Liste quais seriam boas candidatas a pedido de link.
3. Encontre 3 matérias de imprensa que citam um levantamento de dados. Anote o que o dado tinha de novo, quem o produziu e como foi apresentado.

**Desafio**
1. Esboce uma pauta de digital PR com um dado público que ninguém do seu nicho explorou (IBGE, DATASUS, dados.gov.br). Escreva o título da matéria, 3 números de destaque, o gráfico principal e uma lista de 10 veículos ou jornalistas que cobrem o tema.

## 6. Resultados da SERP, títulos e CTR

**Fixação**
1. Por que o Google reescreve title links? Cite 3 situações em que isso costuma acontecer.
2. Explique a decomposição de uma variação de cliques em efeito volume e efeito CTR. Escreva as duas fórmulas e mostre por que a soma dá a variação total.
3. Posição e impressões ficaram estáveis e o CTR caiu. Onde está o problema e que evidências você coletaria para confirmar?

**Prática**
1. No Search Console do seu site, compare dois períodos de 28 dias. Para as 20 buscas com mais cliques, calcule o efeito volume e o efeito CTR e confira se os dois somam a variação total.
2. Mapeie a SERP das suas 20 buscas principais. Para cada uma, anote o que aparece acima do primeiro resultado orgânico (AI Overview, anúncios, vídeos, featured snippet, produtos, mapa).
3. Reescreva 10 títulos de páginas suas com base na intenção da busca principal. Registre a data da mudança e meça o CTR em janelas de 28 dias antes e depois, na mesma faixa de posição.

**Desafio**
1. Escreva um script em Python ou uma consulta SQL que faz a decomposição volume e CTR por página a partir de duas exportações do Search Console e ordena as páginas pelo maior efeito CTR negativo. A interface exporta no máximo 1.000 linhas, então diga quanto do tráfego a sua amostra cobre. Explique também por que janelas de 28 dias comparam melhor que janelas de 30.

## 7. SEO local e e-commerce

**Fixação**
1. O que é NAP? Por que a inconsistência entre fontes prejudica o SEO local?
2. Por que páginas de cidade que só trocam o nome são um risco? O que uma página de cidade precisa ter de próprio?
3. Explique navegação facetada e por que só alguns filtros devem gerar URL indexável.

**Prática**
1. Audite o Perfil da Empresa no Google de um negócio local (categoria, horário, fotos, avaliações e respostas, NAP). Compare o NAP do perfil com o do site e com o de 2 diretórios.
2. Numa loja pública, aplique filtros de cor, tamanho e preço e anote as URLs geradas. Para cada filtro, confira canonical, meta robots e se o robots.txt bloqueia. Decida quais combinações deveriam ser indexáveis, com base em demanda de busca real.
3. Compare 3 páginas de produto do mesmo item em lojas diferentes. Liste o que falta em cada uma (preço, estoque, variantes, avaliações, dados estruturados de Product, imagens, especificações).

**Desafio**
1. Escreva a regra de indexação de filtros de uma loja do seu nicho. Um filtro só vira página indexável com demanda comprovada (autocomplete, Trends ou impressões) e um mínimo de produtos. Aplique a regra a 20 combinações e justifique cada decisão.

## Projeto da trilha · Estratégia de conteúdo para um nicho

**Objetivo.** Decidir o que um site de um nicho deve publicar, em que estrutura e em que ordem, com cada decisão amparada por dado de busca.

**Dados de entrada.** Autocomplete do Google, "as pessoas também perguntam", Google Trends, SERPs públicas consultadas manualmente e, se tiver, o Search Console do seu próprio site. Sites concorrentes só são lidos, sem coleta em massa.

**Passos**
1. Escolha um nicho e escreva em um parágrafo o público, o objetivo do site e como ele ganha dinheiro.
2. Colete de 100 a 150 buscas e registre a fonte de cada uma.
3. Classifique cada busca por intenção e agrupe por SERP, com a regra de URLs em comum escrita no README.
4. Atribua uma página-alvo a cada grupo e marque se ela é nova, existente ou a atualizar. Confira se dois grupos caíram na mesma página.
5. Desenhe a arquitetura com 3 a 5 hubs e suas páginas-filhas, profundidade máxima de 3 cliques, breadcrumbs e regras de link interno. Use um diagrama Mermaid.
6. Priorize os grupos com uma nota que combine demanda, valor para o negócio, dificuldade e ganho de informação. Explique o peso de cada fator.
7. Escreva 3 briefings completos para os grupos mais prioritários, cada um com intenção, ângulo próprio, estrutura, fontes primárias, dado próprio possível, autoria e links internos de entrada e saída.
8. Defina como medir o resultado em 90 dias (impressões e cliques por hub, CTR, páginas indexadas).

**Entregável.** Repositório público com `mapa-palavras.csv` (busca, fonte, intenção, grupo, página-alvo, prioridade), `arquitetura.md` com o diagrama, a pasta `briefings/` com 3 arquivos e um `README.md` com método, decisões e limites.

**Critérios de avaliação**
- [ ] Toda busca tem fonte e intenção registradas
- [ ] O agrupamento segue uma regra de SERP escrita e reproduzível
- [ ] Nenhuma página-alvo atende dois grupos de intenção diferente
- [ ] A arquitetura mostra hubs, profundidade e regras de link interno
- [ ] A prioridade tem fórmula explícita e justificada
- [ ] Os 3 briefings têm ângulo próprio e fontes primárias
- [ ] O plano de medição diz qual métrica, de onde vem e em que prazo
- [ ] Nenhum dado de cliente ou de terceiro foi usado sem ser público
