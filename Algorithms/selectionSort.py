#algoritmo q passa o menor valor para o inicio da lista, o segundo menor para a segunda posição e assim sucessivamente
#algoritmo lento O(N^2) em qualquer cenário, fácil de implementar, não recomendado para grandes quantidades de dados
def selectionSort(v):
  print(v)
  len_v = len(v)
  for i in range(len_v):
    smaller = i
    for j in range(i + 1, len_v):
      if v[j] < v[smaller]:
        smaller = j
    v[smaller], v[i] = v[i], v[smaller]
    print(v)

v = [4,3,5,2,1]
selectionSort(v)
    