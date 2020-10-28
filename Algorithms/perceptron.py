'''
w = w + N (d(k) - y) * x(k)
'''
import random, copy

class Perceptron:
  def __init__(self, amostras, saidas, taxa_aprendizado = 0.1, epocas = 1000, limiar = -1):
    self.amostras = amostras #todas as amostras
    self.saidas = saidas #saídas respectivas de cada amostra
    self.taxa_aprendizado = taxa_aprendizado # entre 0 e 1
    self.epocas = epocas
    self.limiar = limiar
    self.num_amostras = len(amostras)
    self.num_amostra = len(amostras[0]) #qtd de elementos por amostra
    self.pesos = [] #vetor de pesos

  #função para treinar a rede
  def treinar(self):
    #adiciona limiar para cada uma das amostras pois se temos o limiar nos pesos temos tb q multiplica-lo na entrada
    for amostra in self.amostras:
      amostra.insert(0, self.limiar)

    #inicia o vetor de pesos com valores aleatórios
    for i in range(self.num_amostra):
      self.pesos.append(random.random())

    #insere o limiar no vetor de pesos
    self.pesos.insert(0, self.limiar)

    #inicia o contador de epocas
    num_epocas = 0

    while True:
      erro = False #o erro inicialmente inexiste

      #para todas as amostras de treinamento
      for i in range(self.num_amostras):
        u = 0

        '''
          realiza o somatório, o limite (self.amostra + 1) pq foi inserido -1 para cada amostra
        '''
        for j in range(self.num_amostra + 1):
          u += self.pesos[j] * self.amostras[i][j]

        #obtém a saida da rede utilizando a função de ativação
        y = self.sinal(u)

        #verifica se a saída da rede é diferente da saída desejada
        if y != self.saidas[i]:
          #calcula o erro
          erro_aux = self.saidas[i] - y #d(k) - y

          #faz o ajuste dos pesos para cada elemento da amostra
          for j in range(self.num_amostra + 1):
            self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.amostras[i][j]

          erro = True #ainda existe erro
      
      #incrementa epocas
      num_epocas += 1

      #critério de parada: atingiu o número de epocas ou não existe mais erro
      if num_epocas > self.epocas or not erro:
        if num_epocas > self.epocas:
          print('Parada por qtd de épocas')
        else:
          print('Sem erro no treinamento')
        break

  def sinal(self, u):
    return 1 if u >= 0 else -1


  #função utilizada para testar a rede: recebe uma amostra a ser classificada e os nomes das classes
  #utiliza a função sinal, se é -1 então é classe1, senão é classe2
  def testar(self, amostra, classe1, classe2):
    #insere o self.limiar (limiar no vetor de pesos)
    amostra.insert(0, self.limiar)

    #utiliza o vetor de pesos que foi ajustado na fase de treinamento
    u = 0
    for i in range(self.num_amostra + 1):
      u += self.pesos[i] * amostra[i]

    #calcula a saida da rede
    y = self.sinal(u)

    if y == -1:
      print('A amostra pertence à classe %s' % classe1)
    else:
      print('A amostra pertence à classe %s' % classe2)

  def getPesos(self):
    for i in range(len(self.pesos)):
      print('%i' % self.pesos[i], end = ' ')
    print('')


print('\nA ou B?\n')

# amostras: um total de 4 amostras
amostras = [[0.1, 0.4, 0.7], [0.3, 0.7, 0.2], [0.6, 0.9, 0.8], [0.5, 0.7, 0.1]]

# saídas desejadas de cada amostra
saidas = [1, -1, -1, 1]

#conjunto de amostras de testes
testes = copy.deepcopy(amostras)

#cria uma rede Perceptron
rede = Perceptron(amostras, saidas, 0.1, 1000, -1)

#treina a rede
rede.treinar()

#mostra os pesos após treinamento
rede.getPesos()

#testando a rede
for teste in testes:
  rede.testar(teste, 'A', 'B')