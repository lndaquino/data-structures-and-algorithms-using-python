# lista simplesmente ligada onde nó aponta para o próximo nó. Tem tb lista duplamente ligada, que tem referência para o próximo nó e anterior
# é um nó q armazena uma informação e aponta para o próximo nó
class Node:
  def __init__(self, label):
    self.label = label
    self.next = None

  def getLabel(self):
    return self.label
  
  def setLabel(self, label):
    self.label = label

  def getNext(self):
    return self.next

  def setNext(self, next):
    self.next = next

class LinkedList:
  def __init__(self):
    self.first = None
    self.last = None
    self.lenght = 0

  def push(self, label, index):
    if index >= 0:
      #cria novo nó
      node = Node(label)
      #verifica se a lista está vazia
      if self.empty():
        self.first = node
        self.last = node
      else:
        #se inserção no início
        if index == 0:
          node.setNext(self.first)
          self.first = node

        #se inserção no final
        elif index >= self.lenght:
          self.last.setNext(node)
          self.last = node
        
        #inserção no meio
        else:
          prev_node = self.first
          curr_node = self.first.getNext()
          curr_index = 1

          while curr_node != None:
            if curr_index == index:
              #seta o curr_node com o próximo nó
              node.setNext(curr_node)
              #seta o node como o próximo do prev_node
              prev_node.setNext(node)
              break

            prev_node = curr_node
            curr_node = curr_node.getNext()
            curr_index += 1

      #atualiza o tamanho da lista
      self.lenght += 1

  def pop(self, index):
    if not self.empty() and index >= 0 and index < self.lenght:
      flag_remove = False

      #possui apenas um elemento
      if self.first.getNext() == None:
        self.first = None
        self.last = None
        flag_remove = True

      #remove do inicio mas possui mais de um elemento
      elif index == 0:
        self.first = self.first.getNext()
        flag_remove = True

      #possui mais de um elemento e a remoção não é no início
      else:
        prev_node = self.first
        curr_node = self.first.getNext()
        curr_index = 1

        while curr_node != None:
          if index == curr_index:
            #o proximo do anterior aponta para o próximo do nó corrente
            prev_node.setNext(curr_node.getNext())
            curr_node.setNext(None)
            flag_remove = True
            break

          prev_node = curr_node
          curr_node = curr_node.getNext()
          curr_index += 1

      if flag_remove:
        self.lenght -= 1

  def empty(self):
    if self.first == None:
      return True
    return False

  def len_lista(self):
    return self.lenght

  def show(self):
    curr_node = self.first

    while curr_node != None:
      print(curr_node.getLabel(), end = ' ')
      curr_node = curr_node.getNext()
    print('')


lista = LinkedList()

#teste de inserção
lista.push('Lucas', 0) #inserção no inicio
lista.show()
lista.push('Juju', 1) #inserção ao final
lista.show()
lista.push('Manu', 10) #inserção bem no final
lista.show()
lista.push('Gabi', 0) #inserção ao inicio
lista.show()
lista.push('Tomás', 2) #inserção no meio
lista.show()
print('Tamanho da lista: %d\n' % lista.len_lista())

#teste de remoção
lista.pop(0) #remoção do inicio
lista.show()
lista.pop(2) #remove do meio
lista.show()
lista.pop(2)
lista.show()
lista.pop(0)
lista.show()
lista.pop(0)
lista.show()
lista.pop(0)


print('Tamanho da lista: %d\n' % lista.len_lista())