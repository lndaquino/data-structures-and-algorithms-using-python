#tabela de dispersão ou espalhamento, hash table
'''
funciona no modelo chave-valor
objetivo é fazer uma busca rápida e obter o valor desejado
a tabela hash é uma generalização da ideia de array
utiliza uma função para espalhar os elementos que queremos armazenar na tabela
os elementos ficam dispersos de forma não ordenada
importante é a função de hashing, que é responsável por espalhar os elementos
a table hash permite associação de chaves e valores
através da chave é possível obter uma informação de forma rápida
custo para obter um valor é, em média, O(1), isso acontece pq é calculada a posição onde está o elemento
vantagem: eficiência na operação de busca
desvantagem: alto custo para obter os elementos de forma ordenada
objetivo é diminuir o número de colisões para evitar o pior caso: O(N) sendo N tamanho da tabela
colisão é quando dois elementos tentam ocupar a mesma posição dentro da tabela
aplicações: verificação de integridade dos dados, armazenamento seguro de senhas, criptografia
ideal é escolher número primo (reduz probabilidade de colisões) como tamanho da tabela hash e evitar valores que sejam potência de dois (aumenta probabilidade de colisões)
sempre ao fazer a inserção e busca, tem-se que calcular a posição dos dados dentro da tabela
a função de hashing deve calcular uma posição a partir de uma chave e é mt importante quanto à eficiência
uma boa função de hashing e simples e barata de calcular, garantir q valores diferentes possuam posições diferentes, distribuição equilibrada dos dados (máximo espalhamento)
exemplo de função: H(K) = K mod M onde K é um inteiro correspondente a chave e resultado é resto da divisão por M
existem duas estratégias para tratamento de colisões: encadeamento (implementação a seguir) e endereçamento aberto
no encadeamento, cada posição da tabela mantém uma lista encadeada (linked list). As chaves são inseridas ao final de cada lista, que é percorrida para verificar se a chave já está na tabela
vamos adotar o encadeamento externo para tratar as colisões
'''
class HashTable:
  def __init__(self, table_size):
    if table_size < 1:
      print('Erro: o tamanho da tabela tem que ser positivo')

    self.table_size = table_size
    self.table = [[] for i in range(table_size)]

  def hash_func(self, key):
    return key % self.table_size

  def insert(self, key):
    self.table[self.hash_func(key)].append(key)

  def show(self):
    for linked_list in self.table:
      if linked_list:
        for key in linked_list:
          print('%d' % key, end = ' ')
        print('')

  def search(self, key):
    if key in self.table[self.hash_func(key)]:
      return True
    return False

d = HashTable(9)
d.insert(19)
d.insert(28)
d.insert(20)
d.insert(5)
d.insert(33)
d.insert(15)

d.show()
print(d.search(28))