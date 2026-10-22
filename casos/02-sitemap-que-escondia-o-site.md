# Caso 2 · O sitemap que escondia o site

**Setor.** Saúde. **Trilhas.** 02 SEO técnico.

## Contexto
Era preciso dizer, com segurança, quantas páginas um site tinha e quais respondiam. O número seria usado num documento técnico que podia ser contestado.

## Sintoma
O sitemap listava pouco mais de mil endereços, distribuídos em mais de cem arquivos.

## Primeira hipótese
O sitemap representa o site. Basta varrer o que está nele.

## Teste
Cruzar o sitemap com a lista de páginas que recebem tráfego no Search Console.

## Causa
Das mil páginas com mais tráfego orgânico, cerca de 900 não estavam no sitemap. Uma seção inteira, com algumas das páginas mais visitadas, estava de fora. A varredura só pelo sitemap teria dado um número errado justamente no ponto mais importante.

## O que foi feito
A varredura usou a união de sitemap e páginas do Search Console, sem duplicatas, num total perto de 2 mil endereços. Cerca de 1.770 responderam 200 e 220 deram 404. As URLs vindas do Search Console precisaram de normalização, porque algumas tinham espaços e quebras de linha no meio.

## Lição
Sitemap é o que o site declara, não o que o site é. Qualquer afirmação sobre "o site todo" precisa de pelo menos duas fontes independentes.
