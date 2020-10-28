#árvore binária de busca
# elemento é inserido à esquerda de chave for menor e a direita se chave for maior, na ordem em que são inseridos
#elementos à esquerda possui chave menor e elementos à direita possuem chave maior
#visualização em visualgo.net/bst.html
class Node:
  def __init__(self, label):
    self.label = label
    self.left = None
    self.right = None

  def getLabel(self):
    return self.label

  def setLabel(self):
    self.label(label)

  def setLeft(self, left):
    self.left = left

  def getLeft(self):
    return self.left

  def setRight(self, right):
    self.right = right

  def getRight(self):
    return self.right


class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, label):
    #cria novo nó
    node = Node(label)

    #verifica se está vazia
    if self.empty():
      self.root = node

    #árvore não vazia, insere recursivamente
    else:
      dad_node = None
      curr_node = self.root

      while True:
        if curr_node != None:
          dad_node = curr_node

          #verifica se vai para esquerda ou direita
          if node.getLabel() < curr_node.getLabel():
            #vai para esquerda
            curr_node = curr_node.getLeft()
          else:
            #vai para direita
            curr_node = curr_node.getRight()

        #se curr_node é None, então encontrou onde inserir
        else:
          if node.getLabel() < dad_node.getLabel():
            dad_node.setLeft(node)
          else:
            dad_node.setRight(node)
          #sai do loop
          break

  def empty(self):
    if self.root == None:
      return True
    return False

  def show(self, curr_node):
    if curr_node != None:
      print('%d' % curr_node.getLabel(), end = ' ')
      self.show(curr_node.getLeft())
      self.show(curr_node.getRight())

  def getRoot(self):
    return self.root

  def remove(self, label):
    '''
    3 casos:
      1 - nó não tem filhos - seta ligação para o pai de None
      2 - nó tem somente 1 filho - basta colocar o filho no lugar do nó q será removido
      3 - nó tem 2 filhos - pega o menor elemento da sub-arvore a direita
    '''
    dad_node = None # parent
    curr_node = self.root

    while curr_node != None:
      #check if node was found
      if label == curr_node.getLabel():
        #caso 1 - nó folha
        if curr_node.getLeft() == None and curr_node.getRight() == None:
          #verifica se é a raiz
          if dad_node == None:
            self.root = None
          else:
            #verifica se é filho a esquerda ou direita
            if dad_node.getLeft() == curr_node:
              dad_node.setLeft(None)
            elif dad_node.getRight() == curr_node:
              dad_node.setRight(None)

        #caso 2 - nó tem somente 1 filho
        elif (curr_node.getLeft() == None and curr_node.getRight() != None) or \
          (curr_node.getLeft != None and curr_node.getRight() == None):
          #verifica se nó é raiz
          if dad_node == None:
            #verifica se o filho é a esquerda
            if curr_node.getLeft() != None:
              self.root = curr_node.getLeft()
            else:
              self.root = curr_node.getRight()
          #nó não é raiz
          else:
            #verifica se filho de curr_node é filho à esquerda
            if curr_node.getLeft() != None:
              #verifica se curr_node é filho à esquerda
              if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
                dad_node.setLeft(curr_node.getLeft())
              #senão é filho a direita
              else:
                dad_node.setRight(curr_node.getLeft())
            #senão curr_node é filho à direita
            else:
              if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
                dad_node.setLeft(curr_node.getRight())
              #senão é filho a direita
              else:
                dad_node.setRight(curr_node.getRight())

        #caso 3 - nó tem 2 filhos
        elif curr_node.getLeft() != None and curr_node.getRight() != None:
          dad_smaller_node = curr_node
          smaller_node = curr_node.getRight()
          next_smaller = curr_node.getRight().getLeft()

          while next_smaller != None:
            dad_smaller_node = smaller_node
            smaller_node = next_smaller
            next_smaller = smaller_node.getLeft()

          #verifica se o nó a ser removido é a raiz
          if dad_node == None:
            #smaller_node é filho da raiz
            if self.root.getRight().getLabel() == smaller_node.getLabel():
              smaller_node.setLeft(self.root.getLeft())
            #smaller_node não é filho da raiz
            else:
              #verifica se smaller_node é filho à esquerda ou à direita para setar para None o smaller_node
              if dad_smaller_node.getLeft() and dad_smaller_node.getLeft().getLabel() == smaller_node.getLabel():
                dad_smaller_node.setLeft(None)
              else:
                dad_smaller_node.setRight(None)

              #seta os filhos à esquerda e direita de smaller_node
              smaller_node.setLeft(curr_node.getLeft())
              smaller_node.setRight(curr_node.getRight())
            self.root = smaller_node

          else:
            #verifica se curr_node é filho à esquerda ou à direita para setar o smaller como filho do pai do curr_node(dad_node)
            if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
              dad_node.setLeft(smaller_node)
            else:
              dad_node.setRight(smaller_node)

            #verifica se o smaller_node é filho à esquerda ou à direita para setor para None o smaller_node
            if dad_smaller_node.getLeft() and dad_smaller_node.getLeft().getLabel() == smaller_node.getLabel():
              dad_smaller_node.setLeft(None)
            else:
              dad_smaller_node.setRight(None)

            #seta os filhos do smaller_node à esquerda e à direita
            smaller_node.setLeft(curr_node.getLeft())
            smaller_node.setRight(curr_node.getRight())

        break #sai do loop
      
      dad_node = curr_node

      #verifica se vai pra esquerda ou direita
      if label < curr_node.getLabel():
        #vai pra esquerda
        curr_node = curr_node.getLeft()
      else:
        #vai pra direita
        curr_node = curr_node.getRight()




t = BinarySearchTree()

#testes de inserção
t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)
t.insert(9)
t.show(t.getRoot())
print("\n")

t.remove(8)
t.show(t.getRoot())

    