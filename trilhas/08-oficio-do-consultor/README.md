# 08 · Ofício do consultor

Saber a técnica é metade do trabalho. A outra metade é investigar com método, priorizar, convencer quem decide e fazer o time de desenvolvimento implementar. Esta trilha acompanha todas as outras, um módulo por mês.

**Pré-requisitos.** Nenhum. Rende mais a partir da trilha 02.
**Carga estimada.** 20 h.

**Ao terminar, você consegue**
- conduzir uma auditoria em que cada achado foi testado antes de ser afirmado;
- priorizar um backlog por impacto e esforço e defender a ordem;
- entregar relatório e painel que o gestor entende em cinco minutos;
- escrever tarefas que o desenvolvedor implementa sem precisar perguntar;
- montar uma proposta de consultoria com escopo, entregáveis e preço.

## Roteiro

### 1. Auditoria com método

Auditoria é investigação. Cada achado é uma hipótese até ser testado. O relatório que afirma um erro que não existe perde a confiança do cliente no resto.

**Conceitos-chave.** Hipótese, teste e evidência. Fonte primária contra ferramenta. Rótulo de verificação (confirmado, parcial, verificação recomendada). Solução proposta para cada achado. Reprodutibilidade.

**Na prática.** Numa auditoria, nove afirmações de um backlog de 32 estavam erradas, todas pela mesma causa. Inferir estado a partir de sinal indireto em vez de testar. Os quatro padrões que derrubaram o relatório foram estes.
1. Usar grep em vez de parser.
2. Tratar ausência no relatório da ferramenta como ausência no site.
3. Apresentar estimativa como fato.
4. Usar número que o próprio site declara como se fosse contagem.

A regra que ficou é testar antes de afirmar e trazer, junto de cada problema, como deveria ser.

- [ ] Revisei uma auditoria antiga e marquei a origem de cada evidência
- [ ] Reescrevi 5 achados com teste, evidência e solução proposta
- [ ] Separei o que posso afirmar do que só posso recomendar verificar

### 2. Priorização

Tudo parece urgente numa auditoria. Priorizar é escolher o que mexe no resultado com o menor esforço e risco, e dizer o que fica para depois.

**Conceitos-chave.** Matriz impacto e esforço. ICE e RICE. Dependências. Quick wins contra projetos estruturais. Roadmap por trimestre. Separar o que o SEO faz sozinho do que precisa de desenvolvimento.

- [ ] Priorizei um backlog de 20 itens com ICE e justifiquei os 5 primeiros
- [ ] Separei o backlog em "SEO com governança" e "precisa de dev"

### 3. Relatórios e visualização de dados para gestor

O gestor tem cinco minutos. O relatório responde o que aconteceu, por quê, e o que fazer, nessa ordem. O painel recorrente mostra dado e filtro, sem comentário.

**Conceitos-chave.** Pirâmide (conclusão primeiro). Um gráfico, uma mensagem. Escolha do gráfico. Cor com função. Período sempre rotulado. Comparação justa (mesmo dia da semana, feriados). Painel recorrente contra relatório pontual.

**Na prática.** Quando a fonte de cada número tem um período diferente (Search Console em semana móvel, GA4 em mês corrente), rotule no título de cada bloco. Uma gestora cobrou exatamente isso, porque os números não somavam e ninguém dizia por quê.

- [ ] Reescrevi um relatório antigo com a conclusão no primeiro parágrafo
- [ ] Refiz 3 gráficos aplicando "um gráfico, uma mensagem"
- [ ] Rotulei o período de cada número de um painel

### 4. Storytelling com dados e apresentações

Uma apresentação boa conta uma história com começo (situação), meio (complicação) e fim (resolução). Cada slide tem um título que é uma frase com a conclusão.

**Conceitos-chave.** Situação, complicação e resolução. Título de slide como afirmação. Contexto antes do número. Anexo para o detalhe. Revisar cada slide renderizado.

- [ ] Montei um deck de 8 slides em que só os títulos contam a história
- [ ] Apresentei para alguém de fora da área e anotei onde a pessoa se perdeu

### 5. Trabalhar com desenvolvedores e stakeholders

Recomendação que não vira tarefa não vira resultado. Tarefa boa tem contexto, critério de aceite, exemplo e como testar.

**Conceitos-chave.** História de usuário e critério de aceite. Exemplo de código pronto. Ambiente de homologação. Backup e rollback. Documentar antes de construir. Aprovação por escrito.

**Na prática.** Em entregas grandes, documente o plano e peça aprovação antes de construir. Custa um dia e evita refazer uma semana. Em produção, faça backup antes de qualquer gravação e tenha o caminho de volta escrito.

- [ ] Escrevi 3 tarefas técnicas com critério de aceite e forma de testar
- [ ] Documentei uma mudança com backup e rollback antes de executar

### 6. Consultoria independente

Consultoria é vender confiança. Escopo claro, entregável concreto, preço que cobre o risco e histórico de resultado.

**Conceitos-chave.** Escopo e fora de escopo. Proposta. Preço por projeto, por hora e por retenção mensal. Contrato e confidencialidade. Portfólio com casos anonimizados. Rotina de status para o cliente.

- [ ] Escrevi uma proposta para um projeto fictício de auditoria
- [ ] Anonimizei um caso meu para o portfólio
- [ ] Defini a minha rotina de status semanal para clientes

## Material

- [Vídeos](videos.md)
- [Leituras](leituras.md)
- [Exercícios e projeto da trilha](exercicios.md)
