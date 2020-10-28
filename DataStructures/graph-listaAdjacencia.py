class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
    self.graph = [[] for i in range(nodes)]

  def add_edge(self, u, v):
    self.graph[u - 1].append(v - 1)

  def show(self):
    for i in range(self.nodes):
      print('%d: ' % (i+1), end = ' ')
      for j in self.graph[i]:
        print('%d -> ' % (j+1), end = ' ')
      print ('')


g = Graph(5)

g.add_edge(1,2)
g.add_edge(4,1)
g.add_edge(2,3)
g.add_edge(2,5)
g.add_edge(5,3)

g.show()