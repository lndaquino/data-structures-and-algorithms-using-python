'''
visualgo.net tem visualização da max-heap
#binary heap - arvore binária completa ou quase completa - todos os níveis (exceto possivelmente o último) estão completamente preenchidos
#min-heap: valor de cada nó é maior ou igual do que o valor do seu pai, o menor valor está na raiz
#max-heap: valor de cada nó é menor ou igual do que o valor do seu pai, o maior valor está na raiz
#o pai sempre tem prioridade maior ou igual a dos seus filhos
cada posição do array é considerado pai de outras duas posições que são os filhos
a posição i passa a ser pais das posições: 2i + 1 (filho à esquerda) e 2i + 2 (filho à direita)
para inserir um novo elemento basta inserir na primeira posição vaga do array, ou seja, ao final do array (elemento folha)
feito isso deve-se fazer o elemento subir à sua posição na árvore
exemplo: inserir a sequencia 12, 7, 6, 10, 8, 20

para remover remove-se o elemento no topo da heap, ou seja, no inicio do array
copia-se o elemento do final para o inicio do array
leva-se o elemento que foi colocado no topo da heap para a sua respectiva posição de acordo com sua prioridade (desce a árvore)
'''
import heapq

class Pessoa:
  def __init__(self, nome):
    self.nome = nome
  
  def __repr__(self):
    return self.nome

class FilaPrioridade:
  def __init__(self):
    self._fila = []
    self._indice = 0

  def insert(self, item, prioridade):
    heapq.heappush(self._fila, (-prioridade, self._indice, item)) #-prioridade é pra criar uma max-heap
    self._indice += 1

  def remove(self):
    return heapq.heappop(self._fila)[-1] #retorna o último elemento da tupla retornada, que contém o elemento removido

queue = FilaPrioridade()
queue.insert(Pessoa('Lucas'), 39)
queue.insert(Pessoa('Juliana'), 40)
queue.insert(Pessoa('Lenita'), 60)
queue.insert(Pessoa('Camilo'), 36)

print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())
#print(queue.remove()) #falta tratamento de erros pra evitar remover de lista vazia