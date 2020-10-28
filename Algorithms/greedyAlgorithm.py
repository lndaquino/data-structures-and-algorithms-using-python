'''
algoritmos gulosos (greedy algorithm) são aqueles que, a cada decisão, sempre escolhem a alternativa que parece mais promissora naquele momento
nunca reconsideram essa decisão, ou seja, uma escolha que foi feita nunca é revista, não há backtracking
exeplo é o algoritmo de Dijkstra
fazer a escolha que parece ser a melhor num dado momento é fazer uma decisão localmente ótima
geralmente são usados em problemas de otimização
um problema de otimização consiste em encontrar a partir de um conjunto S um subconjunto E de S que deva possuir o menor ou maior custo que satisfazem certa propriedade
Problema do troco: possui as seguintes moedas disponiveis(100, 50, 10, 5, 1) e deve-se dar o troco com o menor numero de moedas possivel
exemplos em marathoncode
'''
moedas = [100, 50, 5, 1]
sol = []
soma = 0
troco = 66 # valor do troco

i = 0
while i < len(moedas) and soma != troco:
  if soma + moedas[i] <= troco:
    sol.append(moedas[i])
    soma += moedas[i]
  else:
    i += 1

  if soma == troco:
    break

print(sol)