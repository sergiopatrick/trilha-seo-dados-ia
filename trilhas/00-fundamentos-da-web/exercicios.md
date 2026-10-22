# Exercícios · 00 · Fundamentos da web

Como usar. Cada módulo tem exercícios em três níveis. Fixação confere o conceito. Prática aplica num site ou dado real. Desafio pede para ir além. As respostas não estão aqui de propósito. Compare a sua com a documentação oficial citada em leituras.md.

## 1. Como a web funciona (HTTP, status, cabeçalhos, cache)

**Fixação**
1. Explique com as suas palavras a diferença entre GET e HEAD. Em que situação de auditoria o HEAD basta e em qual ele pode enganar?
2. Descreva a diferença entre 301, 302, 307 e 308. Diga quais indicam mudança permanente e quais preservam o método da requisição.
3. Uma página de erro também pode ter title e canonical. Por que olhar só o title não basta para dizer se ela é uma página válida? Que dois sinais você confere juntos?

**Prática**
1. Rode `curl -sI` em 5 URLs de um site público (home, categoria, artigo, uma URL inventada e uma imagem). Monte uma tabela com status, `content-type`, `cache-control`, `last-modified` ou `etag` e `x-robots-tag` quando existir. Escreva uma linha explicando cada cabeçalho.
2. Rode `curl -sIL http://dominio.com.br` (sem https e sem www) em 3 domínios de sua escolha. Conte os saltos até o 200 e anote o status e o `location` de cada salto. Diga qual site faz o caminho mais curto.
3. Peça a mesma URL duas vezes seguidas com `curl -sI` e compare cabeçalhos como `age`, `x-cache` ou `cf-cache-status`. Explique se a segunda resposta veio de cache e de qual camada.

**Desafio**
1. Escreva um script em Bash ou Python que recebe uma URL, segue os redirecionamentos um a um sem o seguimento automático e imprime a cadeia completa com status e `location`. Garanta que ele para depois de 10 saltos e avisa quando detecta um laço.

## 2. DNS, CDN e HTTPS

**Fixação**
1. Explique o que é TTL e por que uma mudança de DNS não aparece para todo mundo ao mesmo tempo.
2. Qual a diferença entre um registro A e um CNAME? Para que serve um registro TXT na verificação de propriedade do Search Console?
3. Por que um teste com user-agent de robô feito do seu computador não prova que o site bloqueia esse robô? Que evidência prova?

**Prática**
1. Use `dig +short A dominio.com.br` e as variantes AAAA, CNAME e TXT em 3 domínios públicos. Rode `dig dominio.com.br A` sem o `+short` e anote o TTL de cada registro.
2. Identifique a CDN de 3 sites pelos cabeçalhos de resposta (`server`, `via`, `cf-ray`, `x-served-by`, `x-amz-cf-id`, `x-vercel-id`). Registre qual cabeçalho denunciou cada uma.
3. Rode `curl -sI` na mesma URL duas vezes, uma com o user-agent padrão do curl e outra com `-A "GPTBot"`. Anote se o status muda. Escreva em duas frases por que esse resultado sozinho não serve como prova de bloqueio.

**Desafio**
1. Documente a cadeia completa de um domínio, do endereço digitado até o HTML. Inclua resolução DNS, CDN, certificado (emissor e validade com `openssl s_client -connect dominio.com.br:443 -servername dominio.com.br`), presença de HSTS (`strict-transport-security`) e redirecionamentos. Entregue como diagrama Mermaid no README de um repositório seu.

## 3. HTML semântico e o DOM

**Fixação**
1. Diferencie HTML de origem e DOM renderizado. Em qual dos dois um robô que não executa JavaScript enxerga os links?
2. Para que servem `link rel=canonical` e `meta name=robots`? Por que um canonical numa página que responde 404 não tem efeito?
3. Por que contar blocos de dados estruturados com `grep` pode dar um número falso? Que tipo de ferramenta resolve?

**Prática**
1. Abra uma página de um site feito em React ou outro framework de JavaScript. Compare o "ver código-fonte" com a aba Elements do DevTools e liste 3 elementos que só existem no DOM.
2. Escreva um script com `requests` e BeautifulSoup que imprime title, meta description, canonical, meta robots e a lista de h1 a h3 de uma URL. Rode em 3 páginas de sites diferentes.
3. Conte os links de uma página no HTML de origem (com parser) e no DOM (no Console do DevTools, `document.querySelectorAll('a[href]').length`). Explique a diferença.

**Desafio**
1. Escolha uma página com dados estruturados e conte os blocos `application/ld+json` de dois jeitos, com `grep -c` e com parser. Se os números diferirem, mostre a linha que enganou o grep. Depois liste o `@type` de cada bloco e diga se algum tipo aparece duplicado.

## 4. Terminal e Git

**Fixação**
1. Explique o que um pipe (`|`) faz e dê um exemplo de comando com três etapas.
2. Qual a diferença entre `git add`, `git commit` e `git push`? Onde fica a mudança depois de cada um?
3. Por que nunca se versiona chave de API, mesmo em repositório privado? Como uma variável de ambiente resolve o problema?

**Prática**
1. Crie um repositório no GitHub com README e um `.gitignore` que ignore `.venv/`, `.env` e arquivos de dados grandes. Faça o primeiro commit e o push pelo terminal.
2. Crie uma branch, altere o README, faça commit, abra um pull request para você mesmo e faça o merge pela interface do GitHub. Depois rode `git pull` na main local.
3. Baixe um sitemap público com `curl -s https://dominio.com.br/sitemap.xml -o sitemap.xml`. Se for um sitemap índice, escolha um dos filhos. Só com `grep`, `wc` e pipes, conte quantas URLs ele tem e quantas ficam numa pasta específica, como `/blog/`.

**Desafio**
1. Provoque um conflito de merge de propósito, com duas branches alterando a mesma linha. Resolva no terminal, registre no README os comandos usados e mostre a história com `git log --oneline --graph`.

## 5. Python para analistas

**Fixação**
1. Para que serve um ambiente virtual? O que dá errado quando dois projetos dividem as mesmas bibliotecas?
2. Explique a diferença entre lista e dicionário com um exemplo de SEO, como uma lista de URLs e um dicionário de cabeçalhos.
3. O que significa o status 429? Por que o script certo para no primeiro 429 em vez de tentar de novo na hora?

**Prática**
1. Crie um ambiente com `uv venv` ou `python -m venv .venv`, instale `requests`, `beautifulsoup4` e `pandas` e grave as versões num `requirements.txt`.
2. Escreva um script que lê `urls.txt`, faz GET em cada URL com pausa de 2 a 5 segundos e grava `url`, `status`, `url_final` e `title` num CSV. Ele deve parar no primeiro 429, salvando o que já coletou. Use um user-agent descritivo com um contato seu.
3. Com pandas, leia o CSV do item anterior e responda quantas URLs há por status, qual o tamanho médio do title e quais titles se repetem.

**Desafio**
1. Torne o script retomável. Se ele parar no 429 ou cair, a próxima execução pula as URLs já gravadas. Adicione tratamento para timeout e erro de conexão, registrando o erro na linha em vez de travar o script.

## 6. SQL básico

**Fixação**
1. Explique a diferença entre `WHERE` e `HAVING` com um exemplo de cliques por página.
2. Por que um `LEFT JOIN` entre pedidos e itens de pedido pode multiplicar a receita? Como você detecta isso antes de somar?
3. Como `NULL` se comporta em `COUNT(*)`, em `COUNT(coluna)` e numa comparação com `=`?

**Prática**
1. Resolva os exercícios básicos de um tutorial interativo de SQL, como o SQLBolt, até chegar em `JOIN` e `GROUP BY`.
2. Instale o DuckDB e carregue o CSV do módulo 5 com `SELECT * FROM read_csv_auto('resultado.csv')`. Responda com SQL quantas URLs há por status, quais titles aparecem em mais de uma URL e qual a proporção de redirecionamentos.
3. Baixe um CSV público do dados.gov.br ou do IBGE e escreva 3 consultas, uma com `GROUP BY`, uma com `CASE WHEN` e uma com filtro de data.

**Desafio**
1. Monte duas tabelas pequenas (pedidos e itens) em que um `LEFT JOIN` infle a receita. Mostre o resultado errado, explique a causa e escreva a consulta certa, agregando antes do join.

## Projeto da trilha · Raio-X de um site

**Objetivo.** Construir uma ferramenta pequena que mostra, para uma lista de URLs, o que um buscador recebe de cada uma. Ela junta HTTP, HTML, Python, Git e SQL num só projeto.

**Dados de entrada.** De 50 a 200 URLs de um site público ou do seu próprio site, tiradas do sitemap ou de uma navegação manual. Inclua de propósito 3 URLs inventadas e 3 versões http ou sem www.

**Passos**
1. Escolha o site, leia o robots.txt e monte `urls.txt` sem caminhos bloqueados.
2. Crie o repositório no GitHub com `.gitignore` e ambiente virtual.
3. Escreva `raiox.py`. Para cada URL, ele registra status final, número de saltos, cadeia de redirecionamento, title, canonical, meta robots, `x-robots-tag`, quantidade de h1 e a lista de h2. O HTML é lido com parser.
4. Coloque pausa de 2 a 5 segundos entre requisições, use user-agent descritivo e pare no primeiro 429. O script retoma de onde parou.
5. Grave tudo em `resultado.csv`.
6. Carregue o CSV no DuckDB e responda 5 perguntas em `perguntas.sql`. Sugestões. Quantas URLs respondem 2xx, 3xx, 4xx e 5xx? Quantas páginas 200 têm canonical apontando para outra URL? Quais titles se repetem? Quantas páginas não têm h1 ou têm mais de um? Alguma URL com status diferente de 200 tem title e canonical próprios?
7. Escreva o README com como rodar, o que foi testado, as 5 respostas e o que ficou de fora.

**Entregável.** Repositório público com `raiox.py`, `requirements.txt`, `urls.txt`, `resultado.csv`, `perguntas.sql` e `README.md`.

**Critérios de avaliação**
- [ ] O script roda do zero seguindo só o README
- [ ] Há pausa entre requisições e parada no primeiro 429, com retomada
- [ ] O HTML é lido com parser, nunca com grep ou regex
- [ ] Status e meta robots aparecem lado a lado em cada linha
- [ ] A cadeia de redirecionamento mostra cada salto
- [ ] As 5 perguntas têm consulta SQL e resposta escrita
- [ ] Nenhuma chave, senha ou dado de terceiro foi versionado
- [ ] O README diz o que foi testado e quais limites a ferramenta tem
