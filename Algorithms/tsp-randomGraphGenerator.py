#gerador de grafos
#grafo completo - todos os vertices estão conectados entre si
import random

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
      print('Iter: %i: Melhor Circuito: %s - Custo: %d' % (i+1, str(bestPath), bestCost))


gerador = GraphGenerator(20)
gerador.graphGenerator()
gerador.tspRandom(100)