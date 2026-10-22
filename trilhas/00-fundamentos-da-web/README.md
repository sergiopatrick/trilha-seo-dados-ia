# 00 · Fundamentos da web

A base de tudo que vem depois. SEO técnico é, no fundo, entender o que acontece entre um robô pedir uma URL e o servidor responder. Engenharia de dados é mover e transformar arquivos e tabelas com código. Sem HTTP, HTML, terminal, Git, Python e SQL, as outras trilhas viram decoreba.

**Pré-requisitos.** Nenhum.
**Carga estimada.** 30 h.

**Ao terminar, você consegue**
- ler uma resposta HTTP e dizer se ela está certa para um buscador;
- inspecionar o HTML que o servidor entregou e o DOM que o navegador montou;
- versionar um projeto com Git e publicá-lo no GitHub;
- escrever um script Python que lê um CSV, chama uma API e grava o resultado;
- responder perguntas de negócio com SQL.

## Roteiro

### 1. Como a web funciona (HTTP, status, cabeçalhos, cache)

Toda página começa como uma requisição. O que o servidor devolve (status, cabeçalhos e corpo) decide se o Google rastreia, indexa ou ignora. Aprenda a ler isso no terminal antes de confiar em qualquer ferramenta.

**Conceitos-chave.** Métodos GET e HEAD. Famílias de status (2xx, 3xx, 4xx, 5xx) e a diferença entre 301, 302, 307 e 308. Cabeçalhos `content-type`, `cache-control`, `last-modified`, `etag`, `x-robots-tag`, `location`. Cache de navegador, de CDN e de servidor.

**Na prática.** Uma página de erro também tem título. Numa auditoria, testar só o título fez rotas que davam 404 parecerem páginas canonizadas para a página-pai. A regra que ficou é olhar status e meta robots juntos, sempre, com `curl -sI`.

- [ ] Rodei `curl -sI` em 5 URLs de um site real e expliquei cada cabeçalho
- [ ] Segui uma cadeia de redirecionamento com `curl -sIL` e contei os saltos
- [ ] Sei explicar quando usar 301, 302, 404 e 410

### 2. DNS, CDN e HTTPS

Entre o domínio e o servidor existe uma cadeia de DNS, CDN e certificados. É ali que moram bloqueios de robô, cache que serve versão velha e redirecionamentos que ninguém lembra de ter criado.

**Conceitos-chave.** Registros A, AAAA, CNAME e TXT. TTL. CDN e edge, cache por URL e por cabeçalho. TLS e certificado. HSTS. WAF e regras de bot.

**Na prática.** Um teste com o user-agent de um robô de IA, feito do seu próprio computador, recebeu 403. Parecia que o site bloqueava os robôs. O log do servidor mostrou o contrário, com milhares de visitas reais desses robôs atendidas normalmente. O bloqueio era para o IP não verificado, o seu. A prova de bloqueio é o log, nunca o teste local.

- [ ] Consultei os registros DNS de um domínio com `dig`
- [ ] Identifiquei a CDN de 3 sites pelos cabeçalhos de resposta
- [ ] Sei por que um teste de user-agent feito do meu IP não prova bloqueio

### 3. HTML semântico e o DOM

O buscador lê HTML. Títulos, links, imagens e dados estruturados precisam estar no lugar certo, e de preferência já na resposta do servidor, antes de qualquer JavaScript.

**Conceitos-chave.** `<head>` e `<body>`. `title`, `meta description`, `link rel=canonical`, `meta robots`. Hierarquia de headings. Links com `<a href>`. Atributo `alt`. HTML de origem contra DOM renderizado. DevTools (Elements, Network, Console).

**Na prática.** Contar blocos de dados estruturados com `grep` em vez de um parser deu um número falso, porque o grep pegou a string dentro de um JavaScript. Leia HTML com parser (BeautifulSoup, lxml, ou o próprio DOM no navegador).

- [ ] Comparei o "ver código-fonte" com o DOM no DevTools de uma página feita em React
- [ ] Extraí title, canonical e headings de uma página com Python e BeautifulSoup
- [ ] Sei dizer o que muda para o Google quando um link só existe depois do JavaScript

### 4. Terminal e Git

Todo o resto da trilha roda no terminal. Git é o que permite errar sem medo e mostrar o trabalho.

**Conceitos-chave.** Navegar, listar, buscar (`cd`, `ls`, `grep`, `find`), pipes e redirecionamento. Variáveis de ambiente. `git init`, `add`, `commit`, `branch`, `merge`, `push`, `pull`. `.gitignore`. Pull request. Nunca versionar chave de API.

- [ ] Criei um repositório no GitHub com README e `.gitignore`
- [ ] Fiz uma branch, um commit e um pull request para mim mesmo
- [ ] Uso `grep` e pipes para filtrar um arquivo grande sem abrir no editor

### 5. Python para analistas

Python é a cola entre APIs, planilhas, bancos e modelos de IA. O objetivo é ser fluente em ler, transformar e gravar dados.

**Conceitos-chave.** Tipos, listas, dicionários, funções. Ambiente virtual (`venv` ou `uv`). `requests` para HTTP, `json`, `csv`. pandas para tabelas. Tratamento de erro e espera entre requisições.

**Na prática.** Site com limitador de requisições responde 429. O script certo para no primeiro 429 e retoma depois, com uma pausa entre páginas. Contornar o limitador é a forma mais rápida de ter o IP bloqueado e de perder a confiança do cliente.

- [ ] Escrevi um script que lê uma lista de URLs e grava status e title num CSV
- [ ] O script respeita uma pausa entre requisições e para no primeiro 429
- [ ] Fiz uma análise simples com pandas (agrupar, somar, ordenar)

### 6. SQL básico

SQL é a língua franca dos dados. GA4 no BigQuery, Search Console exportado, CRM e data lake falam SQL.

**Conceitos-chave.** `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`. `JOIN` (inner, left) e o perigo de duplicar linhas. `NULL`. Agregações. `CASE WHEN`. Datas.

- [ ] Resolvi os exercícios básicos de um tutorial interativo de SQL
- [ ] Consigo explicar por que um `LEFT JOIN` pode multiplicar a receita
- [ ] Carreguei um CSV no DuckDB e respondi 5 perguntas com SQL

## Material

- [Vídeos](videos.md)
- [Leituras](leituras.md)
- [Exercícios e projeto da trilha](exercicios.md)

**Próximas trilhas.** [01 SEO estratégico](../01-seo-estrategico), [05 Mensuração](../05-mensuracao) e [06 Engenharia de dados](../06-engenharia-de-dados).
