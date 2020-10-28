## wiki.python.org/moin/TimeComplexity
Análise de complexidade

## Análise assintótica
Ignora valores pequenos e concentra-se nos valores enormes de n
valores pequenos de n até mesmo algoritmos ineficientes custam pouco para executar
matematicamente é o método de descrever o comportamento dos limites superior e inferior
é desejável exprimir de modo q não se dependa da linguagem de programação

# Exemplo:
numa pesquisa sequencial, tem-se o número de vezes que a chave de consulta é comparada com a chave de cada registro:
- pior caso: f(n) = n ==> era o último elemento - maior tempo de execução de todos os casos n
- caso médio: f(n) = (n+1)/2 - tempo médio de execução de todas as entradas
- melhor caso: f(n) = 1 ==> era o primeiro elemento - menor tempo de execução de todos os casos de n

a notação big-O "O" representa a complexidade no pior caso, pois para vários algoritmos o pior caso ocorre com frequência
