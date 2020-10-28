'''
entidade composta de duas partes: vértices (nós - entidade) e arestas (linhas - relações dessas entidades)

matriz de adjacência
marca-se se aquela intersecção da matriz tem ligação
uma das formas de representar um grafo é a matriz de adjacência, mas há outras formas e deve-se buscar a melhor para aquela estrutura de dados
conceitos:
- grafo simétrico: para aresta (u,v) existe um correspondente (v,u)
- grau de um vértice é o numero de arestas que o vertice tem
custo O(n^2) o q pode ser impeditivo

lista de adjacência
array de array para indicar a ligação

matriz de incidência (pouco utilizado)
associa vertices às linhas e arestas às colunas
usado para grafo não orientado

pontes são arestas que desconectam o grafo e aumenta o numero de componentes
para detectar vc remove a aresta, faz busca em profundidade para ver se o grafo permanece conectado, depois adiciona novamente a aresta
'''
#implementação de grafo não dirigido (u,v) = (v,u)
class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = [[0] * nodes for i in range(nodes)]

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

g = Graph(5)
g.show()

g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(2, 3)
g.add_edge(3, 5)
g.add_edge(4, 5)

g.show()

print(g.hasEdge(1,5))