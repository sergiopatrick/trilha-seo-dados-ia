# Exercícios · 02 · SEO técnico

Como usar. Cada módulo tem exercícios em três níveis. Fixação confere o conceito. Prática aplica num site ou dado real. Desafio pede para ir além. As respostas não estão aqui de propósito. Compare a sua com a documentação oficial citada em leituras.md.

Toda coleta desta trilha segue a mesma regra. Pausa de 2 a 5 segundos entre requisições, user-agent descritivo com contato e parada no primeiro 429.

## 1. Rastreio, renderização e indexação

**Fixação**
1. Descreva o caminho de uma URL da descoberta até o índice. Em que etapa o JavaScript é executado?
2. Diferencie "rastreada, mas não indexada" de "descoberta, mas não indexada". Que hipótese você testa primeiro em cada caso?
3. Por que pedir indexação em massa raramente resolve um volume alto de "descoberta, mas não indexada"?

**Prática**
1. Inspecione 5 URLs do seu site na ferramenta de inspeção do Search Console. Teste a URL publicada e compare o HTML renderizado com o resultado de `curl -s` na mesma URL. Anote as diferenças em title, links e conteúdo principal.
2. Abra o relatório de indexação de páginas e explique os 5 principais motivos de exclusão. Para cada motivo, abra 3 exemplos e diga se a exclusão está correta ou se é um problema.
3. No relatório de estatísticas de rastreamento, anote o tipo de arquivo, a finalidade e o código de resposta mais pedidos. Diga se o Googlebot gasta rastreio com algo que não deveria.

**Desafio**
1. Pegue 50 URLs de "rastreada, mas não indexada" e classifique cada uma por hipótese (conteúdo fino, duplicada, parâmetro, página de baixo valor, erro técnico). Mostre a distribuição e proponha uma ação para cada grupo.

## 2. robots.txt, meta robots e sitemaps

**Fixação**
1. Por que `Disallow` no robots.txt não tira uma página do índice? O que acontece com um `noindex` numa página bloqueada pelo robots.txt?
2. Explique a regra de precedência quando um `Allow` e um `Disallow` casam com a mesma URL.
3. Quais os limites de um arquivo de sitemap (50 mil URLs e 50 MB sem compressão)? Quando você precisa de um sitemap índice e o que é um `lastmod` honesto?

**Prática**
1. Baixe o robots.txt de 3 sites públicos e teste 5 URLs de cada um com a biblioteca `protego` do Python, que segue a especificação do Google. Encontre uma regra que bloqueia mais do que parece e explique o risco.
2. Escreva um script que lê o sitemap de um site, pede cada URL e registra status, meta robots e `x-robots-tag`. Liste as URLs do sitemap que têm `noindex`, redirecionam ou dão erro.
3. Exporte as páginas do relatório de desempenho do Search Console do seu site e cruze com as URLs do sitemap. Calcule quantas páginas com clique faltam no sitemap e quantas URLs do sitemap não tiveram nenhuma impressão.

**Desafio**
1. Monte a lista do "site todo" como a união deduplicada de sitemap, páginas do Search Console e crawl. Normalize as URLs (protocolo, barra final, parâmetros de rastreamento) antes de juntar. Mostre numa tabela quantas URLs cada fonte traz sozinha.

## 3. Canonical, duplicação, parâmetros e paginação

**Fixação**
1. Por que o Google trata o canonical como sugestão? Cite 3 sinais que levam o Google a escolher outra URL.
2. Liste 5 formas de a mesma página existir em URLs diferentes.
3. Como tratar a paginação hoje, sem `rel=next`? Para onde deve apontar o canonical da página 2 de uma categoria?

**Prática**
1. Num site público, teste com `curl -sIL` as variantes http e https, com e sem www, com e sem barra final e em maiúsculas de 3 URLs. Registre quais redirecionam, quais respondem 200 e qual canonical cada uma declara.
2. Teste um slug inventado em 5 rotas parametrizadas, como `/produto/slug-que-nao-existe-123`. Anote status, title e meta robots. Qualquer 200 indexável é um achado.
3. Adicione `?utm_source=teste` a 5 URLs e confira se o canonical aponta para a versão limpa.

**Desafio**
1. No seu site, compare a canonical declarada com a canonical escolhida pelo Google, pela inspeção de URL, em 10 páginas. Para cada divergência, escreva a hipótese e o teste que a confirmaria.

## 4. Status HTTP, redirecionamentos e migração de site

**Fixação**
1. Explique o soft 404. Por que ele é pior que um 404 honesto?
2. Quando usar 410 em vez de 404? E 301 em vez de 302?
3. Por que o mapa de redirecionamento deve ser um para um? O que acontece quando tudo vai para a home?

**Prática**
1. Monte um mapa de redirecionamento de 50 URLs (origem e destino esperado) para uma mudança de estrutura no seu site ou num site fictício publicado no GitHub Pages. Escreva um script que testa cada linha e marca OK, destino errado, cadeia ou erro.
2. Encontre uma cadeia de 3 ou mais redirecionamentos num site real. Um bom ponto de partida é a versão http sem www de links antigos citados na Wikipédia.
3. Escreva um checklist de migração dividido em pré, durante e pós, com responsável e prazo por item.

**Desafio**
1. Carregue um log de acesso público (os logs HTTP da NASA de 1995 são um clássico) ou o log do seu site no DuckDB. Conte respostas 5xx por minuto, ache os picos e escreva como você separaria um incidente seu de um incidente do provedor, com quais fontes.

## 5. JavaScript SEO

**Fixação**
1. Diferencie renderização no servidor, no cliente, estática e híbrida. Qual é mais segura para robôs de IA e por quê?
2. Por que um link feito com `onclick` é ignorado pelo Googlebot como caminho de descoberta?
3. O que é hidratação? Que problema aparece quando o HTML do servidor e o do cliente divergem?

**Prática**
1. Desative o JavaScript pelo menu de comandos do DevTools em 3 sites e liste o que some (conteúdo, links, preço, imagens).
2. Compare o `curl -s` de uma SPA com o DOM renderizado no navegador. Conte links e palavras do conteúdo principal nas duas versões.
3. Rode o teste de pesquisa aprimorada numa URL de SPA e veja o HTML renderizado pelo Google. Compare com o resultado do item anterior.

**Desafio**
1. Publique no GitHub Pages duas versões mínimas da mesma página, uma com o conteúdo no HTML e outra que injeta o conteúdo com JavaScript depois de 3 segundos. Veja pela inspeção de URL do Search Console o que o Google renderizou em cada uma. Faça também um `curl` com o user-agent de um robô de IA e compare.

## 6. Core Web Vitals (LCP, INP, CLS)

**Fixação**
1. O que cada métrica mede? Quais os limites de bom no percentil 75 (LCP até 2,5 s, INP até 200 ms, CLS até 0,1) e por que se usa o percentil 75?
2. Diferencie dado de campo e dado de laboratório. Por que o Lighthouse, no modo de navegação padrão, usa o TBT como aproximação da responsividade?
3. O INP substituiu o FID em março de 2024. O que o FID deixava de fora?

**Prática**
1. Rode o PageSpeed Insights em 3 templates de um site (home, categoria e artigo ou produto). Separe numa tabela o dado de campo do dado de laboratório e explique por que eles discordam.
2. Ache o elemento do LCP de uma página no painel Performance do DevTools. Decomponha o tempo em TTFB, atraso de carregamento, tempo de carregamento e atraso de renderização. Diga qual fase pesa mais e o que você mudaria.
3. Grave uma interação (abrir menu, filtrar lista) no painel Performance com limitação de CPU de 4x. Encontre a tarefa longa e o script responsável.

**Desafio**
1. Use a API de histórico do CrUX (gratuita, com chave do Google Cloud guardada em variável de ambiente) para puxar LCP, INP e CLS de 3 sites do mesmo nicho. Monte um gráfico das últimas 25 semanas e escreva o que dá e o que não dá para concluir sobre impacto em negócio com esses dados.

## 7. Dados estruturados

**Fixação**
1. Diferencie JSON-LD, microdados e RDFa. Por que o Google recomenda JSON-LD?
2. Para que serve o `@id`? Como ele evita repetir os dados da Organization em cada página?
3. Por que dado estruturado que contradiz o conteúdo visível é um problema? Dê um exemplo.

**Prática**
1. Escreva o JSON-LD de Organization, WebSite e BreadcrumbList para um site seu ou fictício, ligando as entidades por `@id`. Valide no validador do Schema.org e no teste de pesquisa aprimorada.
2. Escreva um script que extrai, com parser, todos os blocos JSON-LD de 20 páginas de produto de uma loja pública. Conte blocos por `@type` e encontre páginas com Product duplicado ou com valores divergentes de nome, preço ou disponibilidade.
3. Confira a Organization de 3 sites. Verifique se `logo` e `image` usam https, se a URL do logo responde 200 e se os perfis de `sameAs` existem.

**Desafio**
1. Escreva o grafo de entidades de um site de conteúdo (Organization, WebSite, WebPage, Article, Person, BreadcrumbList) num único JSON-LD com `@graph` e explique cada ligação. Depois consulte a galeria de resultados da pesquisa do Google e separe os tipos que ainda geram resultado enriquecido dos que só ajudam a entender a entidade.

## 8. Logs de servidor e ferramentas de crawl

**Fixação**
1. Por que o crawl mostra o que você acha que o robô vê, e o log mostra o que ele viu? Dê um exemplo de achado que só aparece em cada um.
2. Como verificar se um acesso que diz ser Googlebot é real? Descreva o DNS reverso seguido do DNS direto.
3. Por que cada evidência de um relatório precisa dizer de onde veio (crawl próprio, ferramenta, Search Console, log)?

**Prática**
1. Faça o crawl de um site público de até 5 mil URLs com o Screaming Frog (500 URLs na versão gratuita) ou com um crawler seu em Python. Exporte status, title, canonical e meta robots.
2. Carregue um log do seu site ou um log público de exemplo no DuckDB. Conte visitas por user-agent e por seção (primeiro nível da URL) e diga qual seção recebe mais rastreio.
3. Pegue um IP que se apresenta como Googlebot no log e verifique com `host <ip>` e depois `host <nome-devolvido>`. Confira também na lista de IPs que o Google publica em JSON.

**Desafio**
1. Configure uma extração customizada no crawl (XPath ou seletor CSS) para capturar um dado que nenhum relatório padrão traz, como data de atualização, autor ou preço. Cruze com o log e responda se páginas atualizadas recentemente são rastreadas com mais frequência.

## 9. Sites internacionais (hreflang)

**Fixação**
1. Explique a reciprocidade do hreflang e o que acontece quando ela falta.
2. Para que serve o `x-default`?
3. Por que cada versão de idioma deve ter canonical para si mesma? O que acontece quando todas apontam para a versão em inglês?

**Prática**
1. Escreva o conjunto de hreflang de uma página em pt-BR, pt-PT e en, com `x-default`, nas três formas (HTML, cabeçalho HTTP e sitemap).
2. Escolha um site internacional público e extraia com script os hreflang de 5 páginas e das versões para onde eles apontam. Confira reciprocidade, status 200 e códigos válidos (ISO 639-1 para idioma e ISO 3166-1 para região).

**Desafio**
1. Compare subdiretório, subdomínio e ccTLD para uma empresa brasileira que vai abrir operação em Portugal e no México. Recomende uma opção e liste numa tabela os riscos de cada uma.

## 10. SEO em CMS (WordPress, Elementor, Shopify)

**Fixação**
1. No WordPress com Elementor, o que fica em arquivo e o que fica no banco de dados? Por que isso muda o jeito de versionar e de desfazer uma mudança?
2. Onde ficam title, canonical e robots.txt no Shopify? O que o `robots.txt.liquid` permite fazer?
3. Que tipos de mudança devem sempre passar por homologação antes da produção? Dê 3 exemplos.

**Prática**
1. Suba um WordPress local (LocalWP ou `wp-env`), instale um plugin de SEO e liste o que cada plugin ativo injeta no `<head>`. Compare o HTML antes e depois.
2. Use a REST API pública de um WordPress (`/wp-json/wp/v2/posts?per_page=10&page=1`) para listar títulos, datas e slugs sem crawl, com pausa entre as páginas da API.
3. Numa loja Shopify pública, abra `/robots.txt`, `/sitemap.xml` e o `<head>` de um produto. Anote o que é padrão da plataforma e o que parece customizado.

**Desafio**
1. Escreva um procedimento de rollback para trocar o plugin de SEO de um WordPress em produção. Inclua backup do banco com `wp db export`, teste em homologação, critérios de sucesso, passos para desfazer e quem decide voltar.

## Projeto da trilha · Auditoria técnica completa

**Objetivo.** Auditar um site de ponta a ponta e entregar achados com evidência, rótulo de certeza e solução proposta. É o tipo de entrega que um cliente lê e consegue executar.

**Dados de entrada.** O seu próprio site com Search Console, que permite cobrir todas as seções. Se usar um site público de terceiro, os itens que dependem de Search Console ou de log entram como verificação recomendada. Nenhum dado de cliente.

**Passos**
1. Defina o escopo e monte a lista do site todo com a união deduplicada de sitemap, Search Console (se houver) e crawl.
2. Rode o crawl com pausa e parada no primeiro 429. Guarde o export bruto.
3. Indexação. Revise robots.txt, meta robots, `x-robots-tag`, sitemap e canonical. Teste slugs inventados nas rotas com parâmetro.
4. Status e redirecionamentos. Liste cadeias, laços, soft 404 e variantes de protocolo e www.
5. JavaScript. Compare HTML de origem e renderizado nos principais templates.
6. Core Web Vitals. Separe dado de campo e de laboratório por template e ache a causa dos grupos ruins.
7. Dados estruturados. Conte blocos com parser, encontre duplicados e inválidos e confira coerência com a página.
8. Logs, se tiver acesso. Rastreio por seção e verificação de robôs por DNS reverso.
9. Rotule cada achado como **confirmado** (testado, com evidência anexada) ou **verificação recomendada** (indício que depende de acesso ou dado que você não tem). Diga a origem de cada evidência.
10. Para cada achado, escreva a solução, o impacto esperado, o esforço e a prioridade.
11. Escreva um resumo executivo de uma página com os 5 achados de maior impacto.

**Entregável.** Repositório público com os scripts, os dados brutos de crawl, `achados.csv` (id, área, achado, rótulo, evidência, origem, impacto, esforço, solução, prioridade) e `relatorio.md` com o resumo executivo e os achados detalhados.

**Critérios de avaliação**
- [ ] A lista de URLs combina pelo menos duas fontes e está deduplicada
- [ ] A coleta respeitou pausa e parou no primeiro 429
- [ ] Todo achado tem rótulo de confirmado ou verificação recomendada
- [ ] Todo achado confirmado tem evidência reproduzível (comando, print ou export)
- [ ] Todo achado diz a origem da evidência
- [ ] Toda solução é específica o bastante para alguém executar
- [ ] Core Web Vitals usam dado de campo quando existe e citam os limites do percentil 75
- [ ] Dados estruturados foram contados com parser
- [ ] Nenhum resultado enriquecido descontinuado (HowTo, FAQ) aparece como oportunidade
- [ ] O resumo executivo cabe em uma página
