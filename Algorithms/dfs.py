#Depht First Search - busca em profundidade
'''
usado para manipulação de grafos, econtrar componentes conectados, elementos fortemente conectados, ordenação topológica do grafo, resolver labirintos/quebra-cabeças
serve tb para descobrir grafos conexos, encontrar pontes
começa no nó raiz e explora tanto quanto possível antes de retroceder (backtracking)
vamos usar grafos não direcionados nessa implementação de dfs - busca por adjacentes não visitados
'''

class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = [[0] * nodes for i in range(nodes)]
    self.visited = [False] * nodes

  def add_edge(self, u, v):
    self.graph[u - 1][v - 1] = 1
    self.graph[v - 1][u - 1] = 1

  def show(self):
    for i in self.graph:
      for j in i:
        print(j, end = ' ')
      print('')
    print('')

  def hasEdge(self, u, v):
    if self.graph[u - 1][v -1] == 1:
      return True
    return False

  def dfs(self, u):
    self.visited[u - 1] = True
    print('%d visitado' %u)
    for i in range(1, self.nodes + 1):
      if self.graph[u - 1][i - 1] == 1 and self.visited[i - 1] == False:
        self.dfs(i)

g = Graph(5)


g.add_edge(1, 4)
g.add_edge(4, 2)
g.add_edge(4, 5)
g.add_edge(2, 5)
g.add_edge(5, 3)

g.dfs(1)