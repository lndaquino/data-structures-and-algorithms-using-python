'''
para redes não linearmente separaveis, como o XOR, não podemos usar o perceptron
task - usar algoritmos genéticos para buscar os melhores parâmetros para a rede e treinamento da rede (numero de camadas, learining rate)
'''
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

#cria-se um conjunto de entradas (dataset) para treinamento da rede, passando as dimensões dos vetores de entrada e do objetivo
dataset = SupervisedDataSet(2,1)

#adiciona as amostras --> XOR
dataset.addSample([1,1],[0])
dataset.addSample([1,0],[1])
dataset.addSample([0,1],[1])
dataset.addSample([0,0],[0])

#construindo a rede tipo feedforward (cada camada se conecta a proxima camada e todas as camadas tem a mesma direção, partindo da entrada para a saida)
network = buildNetwork(dataset.indim, 4, dataset.outdim, bias = True) #bias permite a uma melhor adptação da rede neural ao conhecimento a ela fornecido

#treinando a rede com backpropagation - pybrain usa por padrão a função sigmoide para produzir a saida do neuronio

#define o procedimento como backpropagation
trainer = BackpropTrainer(network, dataset, learningrate = 0.01, momentum = 0.99) #momentum aumenta a velocidade do treinamento da rede e diminuir o perigo de instabilidade

#treinando a rede - definido como 1000 epocas
for epoch in range(1000):
  trainer.train()

#teste da rede
test_data = SupervisedDataSet(2,1)
test_data.addSample([1,1],[0])
test_data.addSample([1,0],[1])
test_data.addSample([0,1],[1])
test_data.addSample([0,0],[0])

trainer.testOnData(test_data, verbose = True) #verbose diz q é pra mostrar as msgs