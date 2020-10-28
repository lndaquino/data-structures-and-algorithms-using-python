#heuristica não garantem a solução otima, mas obtem uma boa solução relativamente rapida em comparação com algoritmos de brute force, que garante a solução ótima
'''
otimização é a escolha do melhor elemento em um conjunto de alternativas disponíveis
o melhor elemento pode variar de um simples valor inteiro que maximiza ou minimiza uma função até estruturas complexas (ex: melhor arranjo de um time de robôs)
área composta por várias subáres: programação inteira (variáveis se restringem a valores inteiros), otimização estocástica (restrições dependem de variáveis aleatórias) etc
algoritmos exatos garantem solução ótima com a desvantagem de alto custo de tempo
heuristica são tecnicas que garantem boas soluções com um custo razoável, mas não garantem otimalidade:
- geralmente são fáceis de implementar e util para resolver problemas reais
- tem a desvantagem da dificuldade de escapar de ótimos locais
- a metodologia metaheuristica surgiu como possibilidade para sair desses otimos locais permitindo busca em regiões mais promissoras

metaheuristica: são procedimentos que empregam estratégias para escapar de mínimos locais em espaços de busca complexas
- visa produzir um resultado satisfatório para um problemas, mas não garante a otimalidade
- são aplicados a problemas sobre os quais há poucas informações e que a estratégia de brute force é desconsiderada por conta do espaço de solução ser muito grande
- exemplos: tabu search, simulated annealing, genetic algorithms, ant colony optimization

vizinhança: um vizinho de uma solução S é uma solução S' na qual foi aplicado um movimento (definido anteriormente) modificando a solução corrente

simulated annealing é um algoritmo baseado no conceito a recozimento (annealing). Estabelece uma conexão entre o comportamento termodinâmico (aquecimento até o ponto de fusão e resfriamento lento) e a busca pelo máximo/minimo global de um problema de otimização discreto
a cada iteração, a função objetivo gera valores para duas soluções: a atual e a escolhida. Essas soluções são comparadas e, então, as soluções melhores que a atual são sempre aceitas, enquanto que uma fração das soluções piores que a atual são aceitas na esperança de se escapar de um minimo/maximo local
a cada iteração a temperatura é reduzida o que diminui a probabilidade de escolha de uma solução menos promissora e aumenta a tendência de se melhorar a solução atual
o processo começa com um valor de temperatura T elevado e a cada T geram-se soluções até que o equilíbrio àquela temperatura seja alcançado
a temperatura é então rebaixada e o processo prossegue até o congelamento
quanto maior a temperatura, maior a probabilidade de aceitação de uma solução de piora e qt menor T menor a aceitação
termina qd T se aproxima do zero, pelo numero de iterações, por tempo etc
os parâmetros mais adequados são obtidos através de experimentação 
'''
# problema q vamos resolver pra entender: OneMax - tem-se uma sequencia de 0s e 1s e deve-se maximizar a qtd de 1s
import random, math

class OneMax:
  def __init__(self, size):
    self.size = size
    self.solution = [random.randint(0,1) for i in range(size)]
    self.cost = self.objFunction(self.solution)

  #função objetivo que retorna a qualidade da solução
  #no caso do OneMax, qt mais 1 melhor
  def objFunction(self, solution):
    return sum(solution)

  #geração de vizinhos para ver se substitui a solução corrente
  #no caso do OneMax, escolhe aleatoriamente uma posição da solução e substitui o 1 por 0 ou o 0 por 1 e retorna o vizinho
  def neighboor(self):
    new_neighboor = self.solution[:]
    pos = random.randint(0, self.size - 1)
    new_neighboor[pos] = 1 if new_neighboor[pos] == 0 else 0
    return new_neighboor

  '''
    Simulated Annealing
    T = temperatura inicial
    T_min = temperatura minima
    alpha = decaimento da temperatura
    max_iter = qtd de iterações com a mesma temperatura
  '''
  def runAnneal(self, T = 1.0, T_min = 0.00001, alpha = 0.9, max_iter = 100):
    while T > T_min:
      # iterações com uma mesma temperatura
      for i in range(max_iter):
        new_solution = self.neighboor() #gera nova solução
        new_cost = self.objFunction(new_solution) #calcula o custo dessa nova solução
        delta = self.cost - new_cost #calcula a diferença de custos
        ap = math.exp(-delta / T) #probabilidade de aceitação de uma solução de piora

        if ap > random.random(): #verifica se aceita ou não a nova solução
          self.solution = new_solution[:] #copia a nova solução
          self.cost = new_cost #atribui novo custo

      T = T * alpha

  def getSolution(self):
    return self.solution

  
oneMax = OneMax(100)
print('Solução inicial: %s' % str(oneMax.getSolution()))
oneMax.runAnneal()
print('Solução final: %s' % str(oneMax.getSolution()))


