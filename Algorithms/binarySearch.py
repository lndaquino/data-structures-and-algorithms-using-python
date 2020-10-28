'''
busca um valor em uma lista já ordenada
complexidade no melhor caso é O(1), average case O(logN) e worst case O(logN)
vai no valor do meio da lista ordenada crescentemente, se maior continua na metade a direita, se menor na metade à esquerda
método da substituição ajuda a estimar a complexidade de um algoritmo
'''
def binarySearch(keyList, key, init, end):
  if init > end:
    return False

  average = (init + end) // 2

  if key == keyList[average]:
    return True

  if key < keyList[average]:
    return binarySearch(keyList, key, init, end - 1)
  return binarySearch(keyList, key, average + 1, end)

keyList = [11, 5, 10, 20, 15, 4]
keyList.sort()
print(keyList)

key = 15
if binarySearch(keyList, key, 0, len(keyList) - 1) == True:
  print('Encontrou')
else:
  print('Não encontrou')

