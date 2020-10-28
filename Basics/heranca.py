class Transporte:
  def __init__(self, nome, peso, preco):
    self.nome = nome
    self.peso = peso
    self.preco = preco

  def getNome(self):
    return self.nome

  def getPeso(self):
    return self.peso
  
  def getPreco(self):
    return self.preco

class Carro(Transporte):
  def __init__(self, nome, peso, preco, seguro):
    Transporte.__init__(self,nome,peso,preco)
    self.seguro = seguro

  def getSeguro(self):
    return self.seguro


t = Transporte('Fusca', 500, 3500.75)
print(t.getNome())
print(t.getPreco())

carro = Carro('Fusca', 501, 3700.99, 2467.34)
print(carro.getNome())
print(carro.getSeguro())
