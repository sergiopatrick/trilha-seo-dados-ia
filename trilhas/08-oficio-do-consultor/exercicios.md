# Exercícios · 08 · Ofício do consultor

Como usar. Cada módulo tem exercícios em três níveis. Fixação confere o conceito. Prática aplica num site ou dado real. Desafio pede para ir além. As respostas não estão aqui de propósito. Compare a sua com a documentação oficial citada em [leituras.md](leituras.md).

Os exercícios usam sites públicos, o seu próprio site e os casos da pasta [casos](../../casos). Nada de dado de cliente. Quando o exercício pedir para auditar um site de terceiros, use só o que é público, faça o crawl devagar (pausa entre requisições, parada no primeiro 429) e anonimize o nome no que for para o GitHub.

## 1. Auditoria com método

**Fixação**
1. Defina hipótese, teste e evidência com um exemplo de SEO técnico (por exemplo, "as páginas de categoria estão sem canonical").
2. Explique os três rótulos de verificação. Confirmado (testado na fonte primária, reproduzível), parcial (testado numa amostra ou com uma ressalva) e verificação recomendada (sinal indireto que ainda não foi testado). Dê um exemplo de achado para cada um.
3. Para cada um dos quatro padrões de erro de auditoria, escreva um exemplo de afirmação errada e o teste que a teria evitado.
   - Usar grep em vez de parser.
   - Tratar ausência no relatório da ferramenta como ausência no site.
   - Apresentar estimativa como fato.
   - Usar número que o próprio site declara como se fosse contagem.

**Prática**
1. Grep contra parser. Crie três arquivos HTML locais. Num, o canonical está num comentário HTML. No outro, os atributos estão em outra ordem (`<link href="..." rel="canonical">`). No terceiro, há dois canonicals. Procure com `grep 'rel="canonical"'` e depois com um parser (`BeautifulSoup` ou `lxml` em Python). Anote em que arquivo cada método erra.
2. Ausência na ferramenta contra ausência no site. Faça o crawl de um site público com o Screaming Frog gratuito (limite de 500 URLs). Escolha 5 URLs que aparecem no sitemap e não aparecem no crawl. Para cada uma, abra a URL, confira o status com `curl -I` e diga por que a ferramenta não a listou (limite, profundidade, JavaScript, robots.txt).
3. Estimativa contra fato e número declarado contra contagem. Pegue o tráfego estimado do seu site numa ferramenta de terceiros (Semrush, Ahrefs ou similar, na versão gratuita) e compare com o Search Console no mesmo mês. Depois pegue um número que um site público declara na home (por exemplo "mais de 10 mil produtos") e conte de verdade pelo sitemap. Escreva as duas afirmações da forma certa, dizendo a fonte e a natureza de cada número.

**Desafio**
1. Pegue uma auditoria antiga sua, ou o relatório automático de uma ferramenta sobre o seu site. Marque a origem da evidência de cada achado (fonte primária, ferramenta, estimativa, declaração do site). Reescreva 5 achados no formato achado, teste feito, evidência, rótulo de verificação e solução proposta (como deveria ser, com exemplo de código ou configuração). Separe numa lista o que você pode afirmar e o que só pode recomendar verificar.

## 2. Priorização

**Fixação**
1. Qual é a diferença entre ICE e RICE? Em que situação o alcance (o R) muda a ordem?
2. Por que um quick win que depende de uma tarefa estrutural deixa de ser quick win? Como você mostra dependência num backlog?
3. Dê dois exemplos de item que o SEO faz sozinho com governança e dois que precisam de desenvolvimento.

**Prática**
1. Monte um backlog de 20 itens a partir do crawl do módulo 1 e do Search Console do seu site. Pontue cada item com ICE (impacto, confiança e facilidade de 1 a 10). Justifique por escrito os 5 primeiros, com o número que sustenta o impacto.
2. Separe o mesmo backlog em duas colunas, "SEO com governança" e "precisa de dev". Marque as dependências entre itens.
3. Transforme o backlog num roadmap de dois trimestres, com no máximo 3 projetos estruturais por trimestre, e escreva o que fica para depois e por quê.

**Desafio**
1. Leve o backlog para alguém de produto ou de desenvolvimento (um colega ou alguém de uma comunidade) e peça para essa pessoa reordenar. Registre onde vocês discordaram e se a confiança (o C do ICE) estava inflada em algum item.

## 3. Relatórios e visualização de dados para gestor

**Fixação**
1. O que é a estrutura em pirâmide? Reescreva a abertura "Neste relatório analisamos o desempenho orgânico de setembro" com a conclusão primeiro.
2. Por que comparar o dia 3 de um mês com o dia 3 do mês anterior engana? Qual é a forma justa, e o que mais conferir na janela?
3. Qual é a diferença entre painel recorrente e relatório pontual? Onde vai a narrativa?

**Prática**
1. Reescreva um relatório antigo seu (ou um relatório público de resultados de uma empresa listada) com a conclusão no primeiro parágrafo, a causa no segundo e a recomendação no terceiro.
2. Refaça 3 gráficos aplicando "um gráfico, uma mensagem". O título de cada um é a mensagem, a cor destaca só o que importa e o período está rotulado.
3. Monte um bloco de painel com Search Console (semana móvel) e GA4 (mês corrente) e rotule o período de cada número no título do bloco. Escreva uma nota de uma linha explicando por que os números não somam.

**Desafio**
1. Com o Search Console do seu site, faça a mesma comparação mês contra mês de duas formas, pelo dia do mês e pelo dia da semana. Monte um gráfico que mostre a diferença entre as duas leituras e escreva o parágrafo que você mandaria para um gestor que viu a versão errada.

## 4. Storytelling com dados e apresentações

**Fixação**
1. Explique situação, complicação e resolução com um exemplo de queda de tráfego orgânico.
2. Reescreva os títulos "Tráfego orgânico", "Core Web Vitals" e "Próximos passos" como afirmações com a conclusão.
3. O que vai para o anexo e o que fica no corpo do deck?

**Prática**
1. Monte um deck de 8 slides sobre a auditoria do módulo 1 em que só os títulos, lidos em sequência, contam a história completa. Teste lendo só os títulos em voz alta.
2. Exporte o deck em PDF e revise cada slide renderizado. Procure texto cortado, gráfico sem período, número sem contexto e fonte pequena demais. Corrija e anote o que achou.

**Desafio**
1. Apresente o deck para alguém de fora da área em 10 minutos. Anote cada ponto em que a pessoa se perdeu ou pediu explicação e refaça os slides correspondentes. Registre a versão antes e depois.

## 5. Trabalhar com desenvolvedores e stakeholders

**Fixação**
1. Quais são as partes de uma tarefa técnica bem escrita? Contexto, o que fazer, critério de aceite, exemplo e como testar. Explique por que cada uma evita uma pergunta do desenvolvedor.
2. Qual é a diferença entre critério de aceite e descrição da tarefa? Escreva um critério de aceite verificável para "adicionar canonical nas páginas de categoria".
3. Por que documentar e pedir aprovação antes de construir economiza tempo em entrega grande? O que vai nesse documento?

**Prática**
1. Escreva 3 tarefas técnicas a partir dos achados confirmados do módulo 1. Cada uma com contexto (o problema e a evidência), o que fazer, critério de aceite no formato "dado, quando, então", um exemplo de código pronto e como testar em homologação (comando, URL de teste, ferramenta).
2. Para uma das tarefas, escreva o plano de mudança com backup antes de qualquer gravação, passos de execução, como conferir que funcionou e o rollback passo a passo.
3. Troque as tarefas com um colega e peça para ele listar toda pergunta que faria antes de implementar. Reescreva até a lista ficar vazia.

**Desafio**
1. Escolha uma mudança real no seu site (por exemplo, trocar a estrutura de URLs de uma seção). Escreva o documento de aprovação de uma página com objetivo, escopo, fora de escopo, riscos, plano de redirecionamento, backup, rollback e como vai medir o resultado. Execute só depois de aprovar com alguém e registre o que mudou em relação ao plano.

## 6. Consultoria independente

**Fixação**
1. Quais são as vantagens e os riscos de cobrar por projeto, por hora e por retenção mensal? Para que tipo de trabalho cada modelo faz sentido?
2. Por que escrever o que está fora de escopo protege o consultor e o cliente?
3. O que precisa sair de um caso para ele ir ao portfólio sem quebrar a confidencialidade? Pense em nome, números absolutos, URLs, capturas e detalhes que identificam o setor.

**Prática**
1. Escreva uma proposta para um projeto fictício de auditoria técnica de SEO num e-commerce de 50 mil URLs. Inclua contexto, objetivo, escopo, fora de escopo, entregáveis com formato, cronograma, preço com a lógica do cálculo, premissas e condições de pagamento.
2. Anonimize um caso seu (ou reescreva um caso da pasta `casos/` como se fosse seu). Troque números absolutos por variação percentual, remova URLs e marcas e mantenha sintoma, hipótese, teste, causa e resultado.
3. Defina a sua rotina de status semanal para clientes. Escreva o modelo da mensagem com o que foi feito, o que está em andamento, o que está bloqueado e o que você precisa do cliente.

**Desafio**
1. Calcule o seu preço por hora a partir da renda mensal que você quer, das horas faturáveis reais (descontando venda, administração e estudo), dos impostos e de uma reserva para meses sem cliente. Use o número para precificar a proposta da prática 1 e compare com o valor que você teria chutado.

## Projeto da trilha · Portfólio de consultor

**Objetivo.** Montar um portfólio que mostra o ofício inteiro, da investigação à proposta, com uma auditoria anonimizada em que cada achado foi testado antes de ser afirmado.

**Dados de entrada.** O seu próprio site ou um site público que você audita com dados públicos (crawl lento, Search Console só do seu site, PageSpeed Insights, ferramentas gratuitas). O nome do site auditado fica fora do repositório.

**Passos**
1. Faça a auditoria técnica do site escolhido com crawl, Search Console (se for seu) e PageSpeed Insights.
2. Para cada achado, registre hipótese, teste, evidência (com fonte primária quando houver), rótulo de verificação e solução proposta.
3. Revise a auditoria contra os quatro padrões de erro e anote o que mudou na revisão.
4. Monte o backlog priorizado com ICE, separado em "SEO com governança" e "precisa de dev", com dependências.
5. Escreva 3 tarefas técnicas com critério de aceite e forma de testar a partir dos itens do topo.
6. Escreva um relatório de uma página com a conclusão no primeiro parágrafo e o período rotulado em cada número.
7. Monte um deck de 8 slides em que os títulos contam a história em situação, complicação e resolução.
8. Escreva uma proposta para executar o backlog, com escopo, fora de escopo, entregáveis, cronograma e preço.
9. Anonimize tudo antes de publicar.

**Entregável.** Um repositório no GitHub com `README.md` (quem você é, o que o portfólio mostra e como ler), `auditoria.md`, `backlog.csv` ou `backlog.md`, `tarefas/` com as 3 tarefas, `relatorio.pdf` (uma página), `deck.pdf` (8 slides), `proposta.md` e `revisao.md` com o que a revisão contra os quatro padrões corrigiu.

**Critérios de avaliação**
- [ ] Todo achado tem teste, evidência, rótulo de verificação e solução proposta
- [ ] Nenhum achado se apoia só em grep, ausência no relatório da ferramenta, estimativa ou número declarado pelo site
- [ ] Os achados com rótulo "verificação recomendada" não aparecem como fato no relatório nem no deck
- [ ] O backlog está pontuado com ICE e os 5 primeiros itens estão justificados
- [ ] O backlog separa o que o SEO faz sozinho do que precisa de desenvolvimento
- [ ] As 3 tarefas têm critério de aceite verificável e forma de testar
- [ ] O relatório cabe numa página e começa pela conclusão
- [ ] Os títulos do deck, lidos em sequência, contam a história completa
- [ ] A proposta tem escopo, fora de escopo, entregáveis, cronograma e preço com a lógica do cálculo
- [ ] Nada no repositório identifica o site auditado ou um cliente
