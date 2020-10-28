#algoritmo lento - mais simples q existe, percorre o vetor varias vezes e a cada passada traz para o topo o maior elemento do vetor
# pior e caso médio é O(N^2), melhor caso O(N)
# não recomendado para programas q precisam de alta velocidade e q possuem grande quantidade de dados para ordenar
def bubbleSort(v):
  len_v = len(v)
  print(v)
  for i in range(len_v - 1, 0, -1):
    swapped = False
    for j in range(i):
      if v[j] > v[j + 1]:
        v[j], v[j + 1] = v[j + 1], v[j]
        swapped = True
    if not swapped:
      break
    print(v)

v =[10,40,5,15,30,70,20]
bubbleSort(v)