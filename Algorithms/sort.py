#timsort - hidrido do insertion sort com merge sort, método padrão do python
#pior caso e caso médio é Teta(N*log(N)) e melhor caso é Teta(N)
import operator

lista = [20, 15, 5, 10]
print(lista)
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

nomes = ['Marcos','Maria','Carol','Lucas']
nomes.sort()
print(nomes)

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def getNome(self):
    return self.nome

  def getIdade(self):
    return self.idade

p1 = Pessoa('Marcos', 28)
p2 = Pessoa('Pedro', 20)
p3 = Pessoa('Carol', 30)
p4 = Pessoa('Yankee', 25)

pessoas = [p1,p2,p3,p4]
for pessoa in pessoas:
  print('Nome: %s, idade: %d' % (pessoa.getNome(), pessoa.getIdade()))

print('')
pessoas.sort(key=operator.attrgetter('idade'))

for pessoa in pessoas:
  print('Nome: %s, idade: %d' % (pessoa.getNome(), pessoa.getIdade()))