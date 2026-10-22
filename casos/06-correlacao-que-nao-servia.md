# Caso 6 · Performance e receita, a correlação que não servia

**Setor.** Varejo online. **Trilhas.** 02 SEO técnico, 05 Mensuração.

## Contexto
A pergunta era quanto de receita a melhoria de Core Web Vitals poderia trazer, para justificar o investimento de desenvolvimento.

## Sintoma
A correlação entre LCP no celular e receita mensal era forte e estatisticamente significativa.

## Primeira hipótese
Usar a regressão para projetar o ganho de receita de cada milissegundo.

## Teste
Três verificações.
1. O tamanho da amostra. A API pública do CrUX guarda poucas semanas, então só havia seis meses de sobreposição com a receita.
2. O intervalo de confiança da correlação, que ia de quase nada a quase perfeito.
3. Um teste de placebo, calculando a mesma variação de conversão em todos os cortes possíveis da série. O mês em que a métrica de interação piorou foi só o quarto pior entre doze cortes, e os piores meses não tinham nenhum evento técnico.

## Causa
A correlação existia e não servia. Com seis pontos, qualquer tendência sazonal produz correlação forte. A mesma regressão em diferenças dava resultados absurdos.

## O que foi feito
O número entregue saiu de âncoras publicadas (estudos de caso com efeito medido de melhoria de performance em conversão), aplicadas ao tráfego e à receita do próprio site, com uma faixa de mínimo a máximo. O deck mostrou a correlação e explicou por que ela não foi usada.

## Lição
Business case honesto mostra a incerteza. Dizer que o dado não sustenta uma conclusão também é um achado, e protege o consultor quando o resultado vier diferente da projeção.
