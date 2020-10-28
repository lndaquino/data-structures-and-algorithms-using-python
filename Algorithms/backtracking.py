#é um tipo de algoritmo que representa um refinamento da busca por força bruta (q examina exaustivamente todas as possibilidades)
'''
múltiplas soluções podem ser eliminadas sem serem explicitamente examinadas
qd usar:
- vc tem q fazer uma série de decisões
- vc não tem informações suficientes para saber o q escolher
- cada decisão leva a um novo conjunto de escolhas
- algumas sequencias de escolhas pode ser uma solução para o seu problema
- backtracking pode ser uma boa forma de experimentar várias sequencias de decisões até encontrar uma que funciona

exemplo> gerando todos os subconjuntos. Tem-se um conjunto S = {1 ... N}, objetivo é imprimir todos os subconjuntos a partir de N elementos, sendo o numero possível de subconjuntos 2^N
para S = {1,2}, N = 2 tem-se: {1,2},{1},{2},{} --> {1,2} é o mesmo que {2,1}
'''
def gerar_subconjuntos(S, vet, K, N):
  if K == N:
    print('{', end=' ')
    for i in range(N):
      if vet[i] == True:
        print('%d' % S[i], end = ' ')
    print('}')

  else:
    vet[K] = True
    gerar_subconjuntos(S, vet, K + 1, N)
    vet[K] = False
    gerar_subconjuntos(S, vet, K + 1, N)


S = [1,2,3,4,5,6,7,8,9,10]
vet = [False for i in range(len(S))]

gerar_subconjuntos(S, vet, 0, len(S))