# 02 · SEO técnico

SEO técnico é garantir que buscadores e robôs de IA consigam encontrar, baixar, renderizar, entender e indexar as páginas certas, rápido. É a trilha mais longa porque é onde mora a maior parte dos problemas que derrubam tráfego de uma vez.

**Pré-requisitos.** Trilha 00 completa e trilha 01, módulos 1 e 3.
**Carga estimada.** 60 h.

**Ao terminar, você consegue**
- rodar uma auditoria técnica completa e separar o que é erro do que é ruído;
- controlar o que entra e o que fica fora do índice;
- planejar e acompanhar uma migração de site sem perder tráfego;
- diagnosticar Core Web Vitals com dado de campo e de laboratório;
- escrever e validar dados estruturados;
- ler logs de servidor para ver o que os robôs fazem de verdade.

## Roteiro

### 1. Rastreio, renderização e indexação

O Googlebot descobre URLs por links e sitemaps, baixa o HTML, coloca na fila de renderização, executa o JavaScript e só então decide se indexa. Cada etapa tem um relatório no Search Console.

**Conceitos-chave.** Descoberta, rastreio, renderização e indexação. Relatório de indexação de páginas e os motivos de exclusão ("rastreada, mas não indexada", "descoberta, mas não indexada", "duplicada sem canonical"). Ferramenta de inspeção de URL. Estatísticas de rastreamento.

**Na prática.** "Descoberta, mas não indexada" em massa costuma ser sinal de qualidade ou de orçamento, raramente de erro técnico. Antes de pedir indexação de 10 mil URLs, pergunte se elas merecem estar no índice.

- [ ] Inspecionei 5 URLs no Search Console e comparei o HTML renderizado com o original
- [ ] Expliquei os 5 principais motivos de exclusão de um site real
- [ ] Li o relatório de estatísticas de rastreamento e identifiquei o tipo de arquivo mais pedido

### 2. robots.txt, meta robots e sitemaps

Três ferramentas, três funções. robots.txt controla rastreio. Meta robots e `x-robots-tag` controlam indexação. Sitemap sugere o que vale a pena rastrear.

**Conceitos-chave.** Sintaxe do robots.txt e precedência de regras. Por que `Disallow` não tira página do índice. `noindex`, `nofollow`, `noarchive`, `max-snippet`. Sitemap índice, limites de 50 mil URLs e 50 MB, `lastmod` honesto. Sitemap de imagem e de notícias.

**Na prática.** Num site de saúde, o sitemap listava pouco mais de mil endereços, e 918 das mil páginas com mais tráfego orgânico não estavam nele. Qualquer varredura que diga "o site todo" precisa usar a união de sitemap, páginas do Search Console e crawl, sem duplicatas.

- [ ] Validei o robots.txt de 3 sites no testador e achei uma regra perigosa
- [ ] Encontrei URLs com `noindex` dentro do sitemap de um site real
- [ ] Cruzei sitemap com as páginas do Search Console e medi a cobertura

### 3. Canonical, duplicação, parâmetros e paginação

O mesmo conteúdo em várias URLs divide sinais e gasta rastreio. Canonical é uma sugestão forte, não uma ordem, e o Google escolhe a sua quando os sinais se contradizem.

**Conceitos-chave.** `rel=canonical` e canonical escolhida pelo Google. Duplicação por parâmetro, barra final, maiúsculas, http e https, www. Parâmetros de rastreamento (UTM) e de filtro. Paginação sem `rel=next`. Navegação facetada.

**Na prática.** Teste sempre um slug inventado nas rotas com parâmetro. Numa auditoria, `/rota/{qualquer-coisa}` devolvia 200, indexável, com título gerado a partir do texto da URL. Um espaço de URLs infinito que nenhuma ferramenta tinha apontado.

- [ ] Achei 3 tipos de duplicação num site real e propus a correção de cada um
- [ ] Testei um slug inventado em 5 rotas parametrizadas
- [ ] Sei explicar quando o Google ignora a canonical declarada

### 4. Status HTTP, redirecionamentos e migração de site

Migração é o momento de maior risco em SEO. Troca de domínio, de CMS, de estrutura de URL ou de layout pode apagar anos de trabalho se o mapa de redirecionamentos estiver errado.

**Conceitos-chave.** 301 e 308 contra 302 e 307. Cadeias e laços. Soft 404. 410. Mapa de redirecionamento um para um. Checklist de pré, durante e pós migração. Monitoramento diário nas primeiras semanas.

**Na prática.** Um 500 que dura cinco minutos pode vir de uma atualização de PHP feita pela hospedagem. Contar linhas do log de erro por minuto e olhar a página de status do provedor separa um incidente seu de um incidente deles.

- [ ] Montei um mapa de redirecionamento para 50 URLs e testei com script
- [ ] Encontrei uma cadeia de 3 ou mais redirecionamentos num site real
- [ ] Escrevi um checklist de migração com responsável e prazo por item

### 5. JavaScript SEO

O Google renderiza JavaScript, mas com atraso, com limites e sem clicar em nada. Conteúdo e links que só aparecem depois de uma interação não existem para ele. Robôs de IA, na maioria, nem executam JavaScript.

**Conceitos-chave.** Renderização no servidor, no cliente, estática e híbrida. Hidratação. Links que são `<a href>` e links que são `onclick`. Lazy loading. SPA e rotas no cliente. Teste de pesquisa aprimorada e inspeção de URL como visão do Googlebot.

- [ ] Desativei o JavaScript num site e listei o que some
- [ ] Comparei o HTML de origem com o renderizado de uma SPA
- [ ] Sei explicar por que robôs de IA são mais sensíveis a JavaScript que o Googlebot

### 6. Core Web Vitals (LCP, INP, CLS)

Performance é experiência e é sinal de ranqueamento. As três métricas medem carregamento (LCP), resposta à interação (INP, que substituiu o FID em março de 2024) e estabilidade visual (CLS).

**Conceitos-chave.** Dado de campo (CrUX, Search Console) contra dado de laboratório (Lighthouse, PageSpeed). Percentil 75. Limites de bom (LCP até 2,5 s, INP até 200 ms, CLS até 0,1). TTFB. Imagem do LCP e `fetchpriority`. Tarefas longas e terceiros. Fontes e reserva de espaço.

**Na prática.** O relatório do Search Console agrupa URLs parecidas, e um grupo "ruim" costuma ter causa única. Numa auditoria, todas as URLs ruins no celular eram de um subdomínio de API lento, e todas as ruins no desktop eram a home, por um único elemento que mudava de lugar. Corrigir esses dois pontos valia mais que cem otimizações espalhadas. E correlação entre LCP e receita com seis meses de dado não sustenta business case. Use âncoras publicadas e diga a faixa de incerteza.

- [ ] Rodei PageSpeed em 3 templates e separei dado de campo de laboratório
- [ ] Achei o elemento do LCP e o que atrasa ele numa página real
- [ ] Gravei uma interação no painel de performance do DevTools e achei a tarefa longa

### 7. Dados estruturados

Schema.org em JSON-LD ajuda buscadores e IAs a entenderem entidades (organização, produto, artigo, pessoa) e habilita alguns resultados enriquecidos. Dado estruturado errado ou duplicado atrapalha.

**Conceitos-chave.** JSON-LD, microdados e RDFa. Tipos com resultado enriquecido vigente (Product, Article, Breadcrumb, Organization, Review, Event, entre outros). `@id` e grafo de entidades. Validação no teste de pesquisa aprimorada e no validador do Schema.org. Coerência com o conteúdo visível.

**Na prática.** Numa loja, cada página de produto tinha dois blocos Product, um do tema e outro de um aplicativo de SEO, com dados diferentes. Num site inteiro, a Organization era inválida e a imagem de compartilhamento usava http. Conte blocos com parser, nunca com grep, e confira se eles concordam entre si.

- [ ] Escrevi o JSON-LD de Organization, WebSite e Breadcrumb para um site
- [ ] Encontrei um bloco duplicado ou inválido num site real
- [ ] Ligo entidades por `@id` em vez de repetir dados

### 8. Logs de servidor e ferramentas de crawl

Ferramenta de crawl mostra o que você acha que o robô vê. Log de servidor mostra o que ele viu. Juntos, contam a história inteira.

**Conceitos-chave.** Formato de log de acesso. Verificação de Googlebot e de robôs de IA por IP e DNS reverso. Frequência de rastreio por seção. Screaming Frog e crawlers em Python. Extração customizada. Crawl com renderização.

**Na prática.** Ausência no relatório da ferramenta não é ausência no site. Numa auditoria, páginas que "não existiam" segundo uma ferramenta de SEO respondiam 200 com título próprio. Marque a origem de cada evidência no entregável (crawl próprio, ferramenta, Search Console) e diga o que foi testado.

- [ ] Fiz o crawl de um site de até 5 mil URLs e exportei status, title e canonical
- [ ] Contei visitas de robôs por seção num log real ou de exemplo
- [ ] Verifiquei um Googlebot por DNS reverso

### 9. Sites internacionais (hreflang)

Quando o site tem idiomas ou países, hreflang diz ao Google qual versão mostrar para quem. É simples no conceito e fácil de errar na execução.

**Conceitos-chave.** Códigos de idioma e região. Reciprocidade. `x-default`. Hreflang no HTML, no cabeçalho ou no sitemap. Canonical e hreflang juntos. Subdiretório, subdomínio ou ccTLD.

- [ ] Montei o conjunto de hreflang de um site com 3 versões
- [ ] Achei um erro de reciprocidade com uma ferramenta de validação

### 10. SEO em CMS (WordPress, Elementor, Shopify)

A maior parte dos sites roda num CMS, e cada um tem suas armadilhas. Saber onde o CMS guarda cada coisa decide como você implementa e como você desfaz.

**Conceitos-chave.** WordPress, temas, plugins de SEO, WP-CLI e REST API. Elementor e a diferença entre código (arquivos, Git) e conteúdo (banco de dados). Shopify, Liquid, apps, robots.txt.liquid e limites de URL. Cache de página e de objeto.

**Na prática.** Página do Elementor mora no banco de dados, então não sobe por Git. E gravar o conteúdo dela por WP-CLI passa pelo filtro de segurança do WordPress, que apaga `<script>` de widgets HTML sem avisar. Num host gerenciado, criar uma pasta no diretório público derrubou uma rota do WordPress com o mesmo nome. Teste sempre em homologação e guarde backup antes de gravar.

- [ ] Listei os plugins de um WordPress e o que cada um injeta no `<head>`
- [ ] Sei dizer onde ficam title, canonical e robots.txt no Shopify
- [ ] Escrevi um procedimento de rollback para uma mudança em produção

## Material

- [Vídeos](videos.md)
- [Leituras](leituras.md)
- [Exercícios e projeto da trilha](exercicios.md)

**Próximas trilhas.** [03 SEO em escala](../03-seo-em-escala) e [04 GEO e busca generativa](../04-geo-busca-generativa).
