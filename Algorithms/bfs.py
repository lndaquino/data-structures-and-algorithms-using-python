#busca em largura
'''
busca em que parte-se de um vertice e explora todos os vertices vizinhos
para cada um desses vertices mais proximos explora-se os seus vizinhos não visitados e assim sucessivamente
trata-se de uma busca não-informada que expande e examina todos os vertices de um grafo
realiza uma busca exaustiva no grafo
deve garantir que nenhum vertice será visitado mais de uma vez
as visitas aos vértices são realizados  através da ordem de cehgada na fila e um vertice já visitado não pode entrar novamente na fila
complexidade de tempo é O(E + V)
complexidade de espaço é O(V)
E = qt de arestas e V = qt de vertices
'''
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

  # def bfs(self, v):
  #   #visited list
  #   visited = [False] * self.nodes
  #   #marca 'v' como visitado
  #   visited[v - 1] = True
  #   #insere v na fila
  #   fila = [v - 1]
  #   print('%d visitado' % v)

  #   #enquanto a fila não for vazia
  #   while len(fila) > 0:
  #     #obtém o elemento da fila
  #     v = fila[0]
  #     #para cada vértice u adjacente a v
  #     for u in range(self.nodes):
  #       if self.graph[v][u] == 1:
  #         #verifica se u não foi visitado
  #         if visited[u] == False:
  #           visited[u] == True
  #           fila.append(u)
  #           print('%d visitado' % (u+1))
  #     #remove v da fila
  #     fila.pop(0)
  def bfs(self, v):
    visitados = [False] * self.nodes
    visitados[v - 1] = True
    fila = [v - 1]
    print('%d visitado' % v)
    
    while len(fila) > 0:

			# obtém o elemento da fila
      v = fila[0]

			# para cada vértice 'u' adjacente a 'v'
      for u in range(self.nodes):
				# verifica se existe conexão
        if self.graph[v][u] == 1:
					# verifica se 'u' não foi visitado
          if visitados[u] == False:
						# marca 'u' como visitado
            visitados[u] = True
						# insere 'u' na fila
            fila.append(u)
						# imprime o elemento visitado
            print('%d visitado' % (u + 1))

			# remove 'v' da fila
      fila.pop(0)


g = Graph(10)

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_edge(3,6)
g.add_edge(3,7)
g.add_edge(4,8)
g.add_edge(5,9)
g.add_edge(6,10)

g.bfs(1)
