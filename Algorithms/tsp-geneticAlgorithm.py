'''
trabalhamos com populações de individuos (soluções) e não com apenas uma solução individual que vamos melhorando, como o simulated annealing
cada individuo é associado com um score de aptidão que mede o quão boa é a solução
individuos mais aptos tem mais oportunidades de serem reproduzidos produzindo descendentes mais aptos, formando uma população de individuos
começamos com uma população inicial, que passa por avaliação, seleção, reprodução e forma uma nova população, que depois repete o ciclo. Adota-se critério de parada, como número de gerações
no caso do tsp, o custo do circuito poderia ser o valor de aptidão - os q tem menores rotas são individuos mais aptos
busca por diversidade de população ajuda na busca global (exploration) em contraposição ao otimos local (exploitation)
seleção por roleta, torneio etc - roleta usa sorteio para definir com cada individuo representado proprocionalmente à sua aptidão / torneio escolhe n individuos da população aleatoriamente
deve haber equilibrio entre pressão seletiva e diversidade. Baixa pressão seletiva leva a demora na busca de solução e alta pressão leva a convergência prematura
faz-se isso controlando numero de oportunidades de reprodução de cada indivíduo, aumentando o tamanho da população e taxa de mutação
operadores genéticos permitem a obtenção de novos individuos (crossover - cruzamento ou recombinação, mutação e elitismo )
crossover - filhos herdam partes das características dos pais durante reprodução, permite q proximas gerações herdem estas características - escolhe dois indivíduos e troca trechos entre eles
taxa de crossover é o operador genético predominante: deve ser maior q a taxa de mutação, ficando entre 0.6 < p < 1.0 - sem crossover descendentes são iguais aos pais - é a operação mais importante para exploração rápida do espaço de busca
mutação permite a introdução e manutenção da diversidade genética aplicado a cada individuo após crossover. Funciona alterando aleatoriamente um ou mais componentes de uma estrutura escolhida. Ajuda a reduzir chance de parada em minimos locais e geralmente é pequeno (0.001)
algoritmo genético corretamente implementado leva a população a evoluir em gerações sucessivas até estabilizar, de modo que aptidões do melhor individuo e do individuo médio aumentam em direção a um ótimo global
critérios de parada: gerações, tempo de execução, valor de aptidão minimo, medio ou máximo, convergência (nas ultimas k iterações não houve melhora nas aptidões)
aplicações: otimização de função numérica, otimização combinatorial (caixeiro viajante, problema do empacotamento, alocação de recursos), projetos (projeto de pontes), aprendizado de máquina (jogos)
dica de livro: Algoritmos genéticos de Ricardo Linden
'''
import random, sys

class GraphGenerator:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = [[] for i in range(nodes)]
    self.cost = {}

  #gera um grafo completo, com cada aresta conectada a todas as outras (exceto si mesma) e um custo aleatorio entre elas
  def graphGenerator(self):
    for i in range(self.nodes):
      for j in range(self.nodes):
        if i != j:
          if (i, j) and (j, i) not in self.cost:
            cost = random.randint(1, 100)
            self.cost[(i, j)] = cost
            self.cost[(j, i)] = cost
          self.graph[i].append(j)

  def show(self):
    for i in range(self.nodes):
      print('Adjacentes de %d -->' % i, end = ' ')
      for adj in self.graph[i]:
        print('%d (custo %d)' % (adj, self.cost[i, adj]), end = ' - ')
      print('')

  #problema do caixeiro viajante randomico (randomic travelling salesman problem solution)
  def tspRandom(self, iterations):

    bestPath = []
    bestCost = None

    def pathGenerator(bestPath, bestCost):
      nodes = [i for i in range(1, self.nodes)]
      path = [0]
      pathCost = 0

      while len(nodes) > 0:
        e = random.choice(nodes) #randomly choose a node
        nodes.remove(e) #remove node from list
        pathCost += self.cost[(path[-1], e)] #add edge cost
        path.append(e) #add node to path

      pathCost += self.cost[(path[-1], 0)] #add cost returning to initial node

      if bestCost is None:
        bestPath = path[:]
        bestCost = pathCost
      else:
        if pathCost < bestCost:
          bestPath = path[:]
          bestCost = pathCost

      return(bestPath, bestCost)

    for i in range(iterations):
      bestPath, bestCost = pathGenerator(bestPath, bestCost)

    print('Melhor Circuito: %s - Custo: %d' % (str(bestPath), bestCost))

  def tspGenetic(self, populationLenght, generations, tournamentLenght, crossoverProbability, mutationProbability):
    population = []

    def individualGenerator():
      nodes = [i for i in range(1, self.nodes)]
      individual = [0]
      while len(nodes) > 0:
        e = random.choice(nodes)
        nodes.remove(e)
        individual.append(e)

      return individual

    #fitness function
    def getCost(individual):
      cost = 0
      for i in range(self.nodes - 1):
        cost += self.cost[(individual[i], individual[i + 1])]
      cost += self.cost[(individual[-1], individual[0])]
      return cost

    #generating initial population, maybe repeat ones
    for i in range(populationLenght):
      population.append(individualGenerator())

    #at each generation (critério de parada)
    for i in range(generations):
      #tornament selection
      for j in range(tournamentLenght):
        #if has crossover through probability
        if random.random() <= crossoverProbability: 
          
          father, mother = None, None
          child1, child2 = [], []
          child1ValidsGens = [i for i in range(self.nodes)]
          child2ValidsGens = child1ValidsGens[:]

          #select two individuals
          while True:
            father = random.randint(0, populationLenght -1)
            mother = random.randint(0, populationLenght -1)
            if father != mother:
              break

          #one-point crossover
          while True:
            #select point for crossover without extremities
            point = random.randint(0, self.nodes - 1)
            if point != 0 and point != (self.nodes - 1):
              

              for p in range(point):

                #add crossover until point, checking if it´s not an invalid individual (problem constraints - each node once in the solution/individual)
                if population[father][p] not in child1:
                  child1.append(population[father][p])
                  child1ValidsGens.remove(population[father][p])
                else:
                  e = random.choice(child1ValidsGens)
                  child1.append(e)
                  child1ValidsGens.remove(e)

                if population[mother][p] not in child2:
                  child2.append(population[mother][p])
                  child2ValidsGens.remove(population[mother][p])
                else:
                  e = random.choice(child2ValidsGens)
                  child2.append(e)
                  child2ValidsGens.remove(e)

              for p in range(point, self.nodes):
                 #add crossover from point, checking if it´s not an invalid individual (problem constraints - each node once in the solution/individual)
                if population[mother][p] not in child1:
                  child1.append(population[mother][p])
                  child1ValidsGens.remove(population[mother][p])
                else:
                  e = random.choice(child1ValidsGens)
                  child1.append(e)
                  child1ValidsGens.remove(e)

                if population[father][p] not in child2:
                  child2.append(population[father][p])
                  child2ValidsGens.remove(population[father][p])
                else:
                  e = random.choice(child2ValidsGens)
                  child2.append(e)
                  child2ValidsGens.remove(e)

              '''
              print(point)
              print('Father: %s' % str(population[father]))
              print('Mother: %s' % str(population[mother]))
              print('Child1: %s' % str(child1))
              print('Child2: %s' % str(child2))
              sys.exit(1)
              '''

              break
          
          #mutation operator
          if random.random() <= mutationProbability:
            gens1, gens2 = None, None
            while True:
              gens1 = random.randint(0, self.nodes - 1)
              gens2 = random.randint(0, self.nodes - 1)
              if gens1 != gens2:
                child1[gens1], child1[gens2] = child1[gens2], child1[gens1]
                child2[gens1], child2[gens2] = child2[gens2], child2[gens1]
                break

          #get fitness from parents and childs
          fatherFitness = getCost(population[father])
          motherFitness = getCost(population[mother])
          child1Fitness = getCost(child1)
          child2Fitness = getCost(child2)

          if child1Fitness < fatherFitness or child1Fitness < motherFitness:
            if child1Fitness < fatherFitness:
              population.pop(father)
            else:
              population.pop(mother)
            population.append(child1)

          elif child2Fitness < fatherFitness or child2Fitness < motherFitness:
            if child2Fitness < fatherFitness:
              population.pop(father)
            else:
              population.pop(mother)
            population.append(child2)

        # get best individual
        bestIndividual = population[0][:]
        for individual in range(1, populationLenght):
          if getCost(population[individual]) < getCost(bestIndividual):
            bestIndividual = population[individual][:]

    print('Melhor indivíduo: %s - custo: %d' % (str(bestIndividual), getCost(bestIndividual)))


graph = GraphGenerator(50)
graph.graphGenerator()
print('RANDOM')
graph.tspRandom(1000)
print('\nGENETICO')
graph.tspGenetic(100, 1000, 1, 0.7, 0.2)