# Otimização combinatória
Dentro do contexto de metaheuristicas, tais como simulated annealing, ant colony, grasp e vns, além de metaheurísticas híbridas
método de busca local que explora o espaço de soluções movendo-se de uma solução para outra que seja seu melhor vizinho
estrutura de memória para armazenar soluções geradas (ou características dessas)
essas características permitem escapar de ótimos locais
ideia é criar uma lista tabu de movimentos reversos, pois pode ser inviável armazenar T soluções e testar se uma solução está ou não na lista Tabu
uma lista com T soluções permite escapar de ciclos de até T iterações
critério de aspiração: retirar o status tabu de um movimento sob determinadas circunstâncias, como aceitar um movimento, mesmo que tabu, se ele melhorar o valo da função objetivo global (aspiração por objetivo). Já na aspiração por default realizar o movimento tabu mais antigo se todos os possíveis movimentos forem tabus

# Problema da mochila (knapsack problem)
problema pseudo-polinomial, que pode ser abordado por programação dinamica, mas cuja complexidade é O(Np), depende da capacidade da "mochila"
É como se o problema dos caminhos minimos de dkjistra dependesse da aresta, o q aumenta o custo
desse modo, pode ser abordado por soluções de metaheuristica
s = (s1, s2 ... sn) onde sj E {0,1}
movimento m = troca no valor de um bit
aspiração por objetivo melhora a solução
|T| = 1
BTMax = 1

gera uma solução inicial
avalia seus vizinhos (mudança de um bit)
avalia melhora na solução
gera novos vizinhos da melhor solução local
itera até atingir regra de parada