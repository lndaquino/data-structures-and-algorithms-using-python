#fila de prioridade - priority queue - prioridade define o critério de ordenação da fila
#estrutura de dados é escolhida de acordo com a aplicação
'''
Considerando que N é a quantidade de elementos da fila
- inserção e removação na heap binária possui custo O(logN)
- inserção no array ordenado possui custo O(N) e a remoção O(1)
- inserção em um array desordenado possui custo O(1) e remoção O(N)
- inserção em uma lista encadeada possui custo O(N) e remoção O(1)

por exemplo, aplicação possui muitas inserções e pouquissimas remoções - array desordenado seria a melhor escolha
por exemplo, não tenho muita noção da quantidade de inserções e remoções, escolho heap binária
'''

#exemplo de implementação com lista ordenada descrescente pela prioridade
class Person:
  def __init__(self, name, prior):
    self.name = name
    self.prior = prior

  def getName(self):
    return self.name
  
  def getPrior(self):
    return self.prior


class PriorityQueue:
  def __init__(self):
    self.pq = [] # priority queue
    self.len = 0 # queue lenght 

  def push(self, person):
    if self.empty():
      self.pq.append(person)
    else:
      #procura onde inserir para manter a fila ordenada
      flag_push = False
      for i in range(self.len):
        if self.pq[i].getPrior() < person.getPrior():
          self.pq.insert(i, person)
          flag_push = True
          break

      if not flag_push:
        #se entrou aqui é pq tem que inserir ao final
        self.pq.insert(self.len, person)
    
    self.len += 1

  def pop(self):
    if not self.empty():
      self.pq.pop(0)
      self.len -= 1

  def empty(self):
    if self.len == 0:
      return True
    return False

  def show(self):
    for p in self.pq:
      print('Nome: %s' % p.getName())
      print('Prioridade: %d\n' % p.getPrior())

#criando objetos
p1 = Person('Lucas', 20)
p2 = Person('Juliana', 15)
p3 = Person('Lenita', 60)
p4 = Person('Camilo', 18)

pq = PriorityQueue()
pq.push(p1)
pq.push(p2)
pq.push(p3)
pq.push(p4)

pq.show()

pq.pop()
pq.pop()
print('Exibindo após remoções:\n')
pq.show()

print('Exibindo após novas inserções:\n')
pq.push(Person('Goku', 16))
pq.show()