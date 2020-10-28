#algoritmo percorre a lista da esq pra dir, a medida q avança deixa os elementos mais à esq ordenados
#pior caso e caso médio é O(N^2) e melhor caso é O(N)
#eficiente para pequenas qtds de elementos q já estão meio q ordenados
def insertionSort(v):
  len_v = len(v)
  print(v)
  for i in range(1, len_v):
    key = v[i]
    j = i - 1
    while j >= 0 and v[j] > key:
      v[j + 1] = v[j]
      j -= 1
    v[j + 1] = key
    print(v)


v = [50, 10, 5, 70, 60, 40]
insertionSort(v)