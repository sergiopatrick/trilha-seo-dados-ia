# Exercícios · 05 · Mensuração

Como usar. Cada módulo tem exercícios em três níveis. Fixação confere o conceito. Prática aplica num site ou dado real. Desafio pede para ir além. As respostas não estão aqui de propósito. Compare a sua com a documentação oficial citada em [leituras.md](leituras.md).

Os exercícios usam três fontes gratuitas. A conta de demonstração do GA4 (Google Merchandise Store), o conjunto público do GA4 no BigQuery (`bigquery-public-data.ga4_obfuscated_sample_ecommerce`, de novembro de 2020 a janeiro de 2021, consultável no sandbox gratuito) e o Search Console do seu próprio site. Se você ainda não tem site, publique um blog simples no GitHub Pages e use a propriedade dele.

## 1. GA4 do zero

**Fixação**
1. Explique a diferença entre evento automático, evento de medição otimizada, evento recomendado e evento personalizado. Dê um exemplo real de cada um.
2. Um parâmetro de evento aparece no DebugView e some nos relatórios padrão. O que falta configurar para ele virar dimensão? Por que o valor "(other)" aparece em relatórios com alta cardinalidade?
3. A retenção de dados da propriedade está em 2 meses. O que isso afeta nas Explorações e o que não afeta nos relatórios padrão?

**Prática**
1. Abra a conta de demonstração do GA4 (Google Merchandise Store). Liste os eventos marcados como eventos-chave e, para cada um, escreva em uma frase qual decisão de negócio ele apoia.
2. Na mesma conta, crie uma exploração de funil com as etapas `view_item`, `add_to_cart`, `begin_checkout` e `purchase`, aberta e fechada. Anote em qual etapa está a maior perda e como o número muda entre funil aberto e fechado.
3. Crie uma propriedade GA4 de teste ligada ao seu site. Configure 3 eventos personalizados (por exemplo `clique_whatsapp`, `envio_formulario` e `rolagem_90`), registre os parâmetros como dimensões personalizadas e confirme no DebugView. Depois crie um agrupamento de canal personalizado que separe "IA generativa" (referências de chatgpt.com, perplexity.ai, gemini.google.com e copilot.microsoft.com) do restante de "Referral".

**Desafio**
1. Escolha um negócio fictício de geração de leads. Escreva com o "dono" do negócio, em uma página, o que é lead para ele. Depois desenhe os eventos. Mostre por que separar "envio do formulário" e "lead qualificado" em duas etapas do funil criaria uma perda que não existe, ou justifique o caso em que a separação faz sentido.

## 2. Google Tag Manager e dataLayer

**Fixação**
1. Explique a relação entre tag, acionador e variável usando um exemplo de clique em botão.
2. Por que um `dataLayer.push` feito antes do snippet do GTM não se perde? E por que a ordem entre o `push` e o acionador importa?
3. Numa aplicação de página única, a URL muda e a página não recarrega. Quais são as duas formas de medir essa troca de tela e qual é o risco de cada uma (evento duplicado ou evento faltando)?

**Prática**
1. Crie uma página HTML local, sirva com `python -m http.server 8000` e instale um contêiner GTM de teste. Faça um botão executar `dataLayer.push({event: 'clique_cta', posicao: 'topo'})`. Crie a variável de camada de dados, o acionador de evento personalizado e a tag de evento do GA4. Confirme no modo de visualização e no DebugView.
2. Na mesma página, simule uma loja com três produtos. Implemente `view_item_list`, `select_item`, `add_to_cart`, `begin_checkout` e `purchase` com o objeto `ecommerce` no formato da documentação do GA4. Lembre de limpar o objeto com `dataLayer.push({ecommerce: null})` antes de cada evento e explique por quê.
3. Escreva o contrato do dataLayer dessa loja como se fosse para o time de desenvolvimento. Para cada evento, informe quando dispara, os campos obrigatórios, o tipo de cada campo e um exemplo de JSON.

**Desafio**
1. Monte uma aplicação de página única pequena (React com Vite ou HTML com `history.pushState`) com um checkout em três rotas. Escreva uma ponte que lê o estado da aplicação e empurra um evento para o dataLayer em cada rota. Prove no modo de visualização que cada etapa dispara uma vez só, inclusive quando o usuário volta com o botão do navegador.

## 3. UTM e atribuição

**Fixação**
1. Quais são os cinco parâmetros UTM e qual deles o GA4 usa para montar o agrupamento de canais padrão? Por que `Email`, `email` e `e-mail` viram três fontes diferentes?
2. Explique em poucas linhas último clique, primeiro contato e data-driven. Desde novembro de 2023 o GA4 mantém só o data-driven e as variantes de último clique como modelos de atribuição. Onde o primeiro contato ainda aparece na interface (dica, dimensões de "primeiro usuário") e por que isso é diferente de um modelo que divide o crédito da conversão?
3. Liste três motivos pelos quais uma sessão cai em "Direct" ou "Unassigned" no GA4.

**Prática**
1. Escreva uma convenção de UTM para um negócio fictício com e-mail, redes sociais, parceiros e mídia paga. Inclua regras de minúscula, separador, valores permitidos de `utm_medium` e 10 exemplos de URL montadas no Campaign URL Builder (https://ga-dev-tools.google/ga4/campaign-url-builder/).
2. No BigQuery, usando `bigquery-public-data.ga4_obfuscated_sample_ecommerce`, calcule as compras e a receita por `traffic_source.source` e `traffic_source.medium` (fonte do primeiro contato do usuário). Compare com o relatório de aquisição da conta de demonstração, que usa outro modelo, e explique por que os números não batem.
3. Baixe o conjunto público "Marketing Funnel by Olist" no Kaggle. Cruze a tabela de leads qualificados com a de negócios fechados pela chave `mql_id`. Meça quanto dos negócios fechados está com origem vazia ou `unknown`. Esse é o seu balde sem origem.

**Desafio**
1. Com o mesmo conjunto da Olist, escreva um relatório de uma página que responda "qual canal vende?". Mostre como a resposta muda quando você ignora, distribui proporcionalmente ou isola o balde sem origem. Termine com o que você pediria para conferir na forma como o CRM grava a origem antes de cortar verba de algum canal.

## 4. Search Console a fundo

**Fixação**
1. Por que a soma dos cliques por busca é menor que o total de cliques da propriedade? E por que a soma por página pode ser diferente do total agregado por propriedade?
2. Uma página tem posição média 4,2. Descreva dois cenários de distribuição de posições que dão essa mesma média e levam a decisões diferentes.
3. O Search Console publica a série diária até dois dias antes, e o dia publicado não muda depois. Um gestor diz que a queda dos últimos três dias é "dado ainda entrando". Como você responde, e o que olha primeiro se impressões estão estáveis e cliques caíram?

**Prática**
1. No Search Console do seu site, exporte desempenho por data com e sem a dimensão de busca para os últimos 3 meses. Calcule a porcentagem dos cliques que vem de buscas anonimizadas (total menos soma das buscas). Repita pela API (`searchanalytics.query` com `dataState` igual a `final`) e confira se os números batem.
2. Pela API, colete a série diária dos últimos 28 dias e salve num CSV com a data da coleta. Colete de novo uma semana depois. Junte as duas coletas por data e prove que os dias em comum têm os mesmos números.
3. Ative a exportação em massa para BigQuery na propriedade do seu site. Depois que as tabelas chegarem, conte em `searchdata_url_impression` quantas impressões vêm de linhas com `is_anonymized_query` verdadeiro e compare com o cálculo do exercício 1.

**Desafio**
1. Monte um script que, para cada página do seu site, separe uma variação de cliques entre dois períodos em três efeitos. Efeito de impressões, efeito de CTR e efeito de posição. Aplique a uma página que caiu e escreva a conclusão em três frases.

## 5. Painéis no Looker Studio

**Fixação**
1. Qual é a diferença entre o conector do Search Console com tabela "Site Impression" e com "URL Impression"? Qual deles usar para somar cliques do site inteiro?
2. Por que comparar o dia 3 de um mês com o dia 3 do mês anterior pode inventar viradas? Como alinhar pelo dia da semana?
3. Quando um painel deve virar relatório narrativo e quando um relatório deve virar painel?

**Prática**
1. No Looker Studio, conecte a conta de demonstração do GA4 e o Search Console do seu site. Monte uma página com cliques orgânicos (Search Console) e sessões orgânicas e eventos-chave (GA4) lado a lado, cada bloco com o período escrito no título.
2. Monte uma comparação diária mês contra mês alinhada pelo dia da semana. Uma forma simples é comparar cada dia com o mesmo dia da semana quatro semanas antes (28 dias). Faça a versão ingênua (mesmo dia do mês) e a versão alinhada, e anote a maior diferença de variação entre as duas. Confira os feriados nacionais na janela.
3. Pegue o painel que você montou e corte para no máximo 6 gráficos. Para cada gráfico, escreva a pergunta do gestor que ele responde. O que não responde pergunta sai.

**Desafio**
1. Monte uma fonte combinada (blending) entre Search Console e GA4 por página de destino. Documente onde a junção perde linhas (URL com parâmetro, barra final, maiúscula) e proponha uma regra de normalização num campo calculado.

## 6. Experimentos de SEO

**Fixação**
1. Por que um teste A/B de usuários (como o de uma ferramenta de CRO) não serve para medir efeito de SEO? Como o teste por grupos de páginas resolve isso?
2. Explique contrafactual, diferença em diferenças e teste de placebo em uma frase cada.
3. Você tem 6 pontos mensais e uma correlação de 0,8. Por que isso não sustenta um business case? O que é poder estatístico nesse contexto?

**Prática**
1. Use a API de pageviews da Wikimedia (https://wikimedia.org/api/rest_v1/) para baixar 2 anos de visualizações diárias de 20 artigos parecidos da Wikipédia em português. Mande um User-Agent descritivo, pause entre as requisições e pare no primeiro 429. Divida os artigos em controle e variante ao acaso e "aplique" uma intervenção fictícia numa data.
2. Rode CausalImpact (pacote R ou `tfcausalimpact` em Python) usando o grupo de controle como covariável. Rode também uma diferença em diferenças com regressão simples. Compare os dois resultados.
3. Faça um teste de placebo. Mova a data da intervenção para 12 datas falsas e veja em que posição o efeito "real" fica entre os 12. Se ele não estiver entre os maiores, escreva isso como achado.

**Desafio**
1. Desenhe por escrito um teste de SEO para um site com pelo menos 200 páginas do mesmo modelo (por exemplo, páginas de produto). Defina a hipótese, a métrica, como dividir os grupos (estratificado por tráfego), a duração, o efeito mínimo detectável que você espera e o critério para encerrar. Inclua o que fazer se o resultado for inconclusivo.

## 7. Consentimento e privacidade

**Fixação**
1. Quais são os quatro sinais do Consent Mode v2 e o que cada um controla?
2. Qual é a diferença entre Consent Mode básico e avançado em termos de quais pings chegam ao Google e de modelagem de conversões?
3. Por que e-mail, telefone ou CPF nunca podem ir em URL nem em parâmetro de evento? Cite a base na LGPD e a regra das políticas do Google Analytics.

**Prática**
1. Na página de teste do módulo 2, configure um banner de consentimento (uma CMP gratuita ou um banner próprio) e o Consent Mode v2 pelo GTM, com padrão negado. No modo de visualização, mostre o estado de consentimento antes e depois do aceite. No painel de rede do navegador, observe o parâmetro `gcs` nas requisições e explique os valores.
2. Na conta de demonstração do GA4, ou no seu próprio site, crie uma exploração com `page_location` e filtre por expressões que pegam e-mail (`@`) e CPF (`\d{3}\.?\d{3}\.?\d{3}-?\d{2}`). Documente o que achou e onde o dado entra (formulário com GET, redirecionamento, parâmetro de campanha).

**Desafio**
1. Escreva um procedimento de uma página para quando dado pessoal for encontrado no GA4. Inclua como corrigir a origem, como redigir ou excluir os dados já coletados (solicitação de exclusão de dados do GA4) e como evitar que volte (filtro no GTM e teste automatizado).

## Projeto da trilha · Plano de mensuração de um site

**Objetivo.** Entregar o plano de mensuração completo de um site, do que é conversão até como ler um teste de SEO. É o documento que um time de desenvolvimento e um gestor usariam para implementar e conferir a medição.

**Dados de entrada.** O seu próprio site (ou um site de teste publicado por você), a propriedade GA4 e o Search Console dele, e a conta de demonstração do GA4 como referência. Nada de dado de cliente.

**Passos**
1. Escreva o objetivo de negócio do site e as 3 a 5 perguntas que a medição precisa responder.
2. Defina o que é conversão e o que é lead, por escrito. Liste os eventos-chave.
3. Monte a tabela de eventos. Nome, quando dispara, parâmetros, tipo de cada parâmetro e se vira dimensão personalizada.
4. Escreva o contrato do dataLayer com um exemplo de JSON para cada evento, inclusive os de e-commerce se houver.
5. Implemente no GTM e registre no modo de visualização uma captura de cada evento disparando.
6. Escreva a convenção de UTM com valores permitidos e 10 exemplos.
7. Configure o Consent Mode v2 e prove que nenhum dado pessoal vai em URL ou evento.
8. Monte no Looker Studio um painel com GA4 e Search Console, com no máximo 6 gráficos, período rotulado em cada bloco e uma comparação mês contra mês alinhada pelo dia da semana.
9. Desenhe um teste de SEO para o site, com hipótese, grupos, duração, métrica e teste de placebo previsto.

**Entregável.** Um repositório no GitHub com `README.md` (resumo do plano e link do painel), `plano-de-mensuracao.md`, `datalayer.md`, `utm.md`, `teste-de-seo.md`, a exportação do contêiner GTM em JSON (sem IDs sensíveis) e uma pasta `evidencias/` com as capturas do modo de visualização.

**Critérios de avaliação**
- [ ] Lead e conversão estão definidos por escrito antes da lista de eventos
- [ ] Cada evento tem gatilho, parâmetros com tipo e um exemplo de JSON
- [ ] Os eventos de e-commerce seguem os nomes recomendados do GA4
- [ ] Há evidência de cada evento disparando no modo de visualização
- [ ] A convenção de UTM tem regras de minúscula e lista fechada de `utm_medium`
- [ ] O Consent Mode v2 está configurado com padrão negado e o efeito foi mostrado
- [ ] Nenhum dado pessoal aparece em URL, evento ou captura do repositório
- [ ] O painel tem no máximo 6 gráficos e o período de cada bloco está no título
- [ ] A comparação mês contra mês está alinhada pelo dia da semana e cita feriados da janela
- [ ] O teste de SEO tem grupo de controle, métrica, duração e teste de placebo
