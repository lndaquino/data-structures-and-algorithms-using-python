#grafos onde vc consegue voltar ao vertice de origem são graficos ciclicos
#árvores são aciclicos, pois não contém ciclos e vc não consegue voltar para o vertice de origem
#algoritmo pouco eficiente, pois faz dfs pra cada vertice. Há algoritmos mais eficientes
class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
    self.list = [[] for i in range(nodes)]

  def addEdge(self, origin, destiny):
    self.list[origin].append(destiny)

  def dfs(self, v):
    stack, stack_rec = [], []
    visited = [False for i in range(self.nodes)]
    stack_rec = [False for i in range(self.nodes)]

    while True:
      hasNeighboor = False
      if not visited[v]:
        stack.append(v)
        visited[v] = stack_rec[v] = True

      aux_adj = None

      for adj in self.list[v]:
        aux_adj = adj
        # se o vizinho está na pilha é pq existe ciclo
        if stack_rec[adj]:
          return True
        elif not visited[adj]:
          #se não está na pilha e não foi visitado
          hasNeighboor = True
          break

      if not hasNeighboor:
        stack_rec[stack[-1]] = False #marca que saiu da pilha
        stack.pop() #remove da pilha
        if len(stack) == 0:
          break
        v = stack[-1]

      else:
        v = adj
    
    return False

  def hasCicle(self):
    for i in range(self.nodes):
      if self.dfs(i):
        return True
    
    return False


g = Graph(3)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,1)
print(g.hasCicle()) #True, ciclo entre b e c

h = Graph(4)
h.addEdge(0,1)
h.addEdge(1,2)
h.addEdge(2,3)
print(h.hasCicle())