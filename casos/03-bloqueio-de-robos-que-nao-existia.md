# Caso 3 · O bloqueio de robôs de IA que não existia

**Setor.** Educação médica. **Trilhas.** 02 SEO técnico, 04 GEO.

## Contexto
Diagnóstico de GEO de um portal grande. A primeira pergunta era se os robôs de IA conseguiam acessar o site.

## Sintoma
Ferramentas automáticas de leitura de página recebiam 403. Um teste com o user-agent de robôs de IA, feito do computador da equipe, também recebia 403.

## Primeira hipótese
O site bloqueia robôs de IA, e todo o esforço de GEO seria inútil até resolver isso.

## Teste
Ler o log do servidor de um mês e contar as visitas por robô, com os IPs oficiais.

## Causa
O bloqueio valia para IPs não verificados, como o da equipe. Os robôs reais, vindos dos blocos de IP oficiais, eram atendidos normalmente. O log mostrou visitas de robôs de busca e de IA de várias empresas, com robôs de busca de IA na casa de mais de mil visitas no mês, e isso contando só uma parte do log. O robots.txt também não bloqueava nenhum robô de IA.

## O que foi feito
O "gate zero" de GEO foi registrado como aberto, com o log como prova. O trabalho seguiu para conteúdo, entidades e dados estruturados.

## Lição
Teste de user-agent feito do seu IP não prova bloqueio nem acesso. A prova é o log do servidor. E uma conclusão errada logo no início teria mudado o projeto inteiro.
