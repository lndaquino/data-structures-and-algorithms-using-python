class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome #self quer dizer q é deste objeto
    self.idade = idade

  def getName(self):
    return self.nome
  
  def getAge(self):
    return self.idade

  def setAge(self, idade):
    self.idade = idade

# p = Pessoa('Lucas', 39)
# p.idade = 38
# print('Nome: %s' % p.getName())
# print('Idade: %d' % p.getAge())

p1 = Pessoa('Maria',10)
p2 = Pessoa('Gabi',9)
p3 = Pessoa('Tomas',7)
p1.setAge(11)

pessoas = []
pessoas.append(p1)
pessoas.append(p2)
pessoas.append(p3)

for pessoa in pessoas:
  print(pessoa.getAge())