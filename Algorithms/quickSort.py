#algoritmo de ordenção rápida - escolhe-se um pivo, faz-se particionamento, todos à esquerda do pivo serão menores q pivo e os a direita serão maiores q pivo
#depois ordena-se as particões recursivamente escolhendo novo pivo
#melhor caso é O(N * logN), pior caso é O(N^2) mas é raro e pode-se fazer ser quase impossível de ocorrer
#escolha do pivo define a efiacia do algoritmo
def partition(v, init, end):
  #o pivo é o elemento do inicio
  pivo = init
  for i in range(init + 1, end + 1):
    if v[i] <= v[init]:
      pivo += 1
      v[i], v[pivo] = v[pivo], v[i]

  v[pivo], v[init] = v[init], v[pivo]
  return pivo


def quickSort(v, init, end):
  #se o fim for maior q o inicio então calcula-se a posição do pivo
  if end > init:
    #separa os dados em duas partições
    pivo = partition(v, init, end)
    #tendo o pivo, chama a função duas vezes para cada partição, a primeira dos elementos antes e a segundo dos elementos após o pivo
    quickSort(v, init, pivo - 1)
    quickSort(v, pivo + 1, end)
  

v = [4,3,2,1,10,30,48,23,18,90, 105, 33, 68, 55, 19, 45]
quickSort(v, 0, len(v) - 1)
print(v)