'''
Distancia hamming corresponde ao número de posições que correspondem a simbolos que são diferentes
para tanto é preciso q elas tenham comprimentos iguais
hamming('marcos', 'marcus') = 1
hamming(0101, 1110) = 3
'''
def hamming(s1, s2):
  len_s1, len_s2 = len(s1), len(s2)
  if len_s1 != len_s2:
    raise ValueError('Sequencias de tamanhos diferentes')

  '''dist = 0
  for i in range(len_s1):
    if s1[i] != s2[i]:
      dist += 1

  return dist'''
  return sum(1 for i in range(len_s1) if s1[i] != s2[i])


print(hamming('marcos', 'marcus'))
print(hamming('python', 'pytohn'))
print(hamming('0101', '1110'))