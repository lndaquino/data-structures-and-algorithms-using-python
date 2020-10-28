'''
Levenshtein distance
serve pra mensurar a diferença entre duas strings - o quão diferentes são essas string
diz qual a quantidade necessária de inserções, deleções e substituições
pode ser usada para correspondencia de strings curtas em textos longos, a maior subsequencia dentro de uma string etc
'''

#método ineficiente pois recomputa subsoluções mais de uma vez
#task - otimizar usando programação dinâmica
def editDistance(s1, s2, len_s1, len_s2):
  if len_s1 == 0:
    return len_s2

  if len_s2 == 0:
    return len_s1

  custo = 0 #custo começa em zero

  if s1[len_s1 - 1] != s2[len_s2 - 1]:
    custo = 1 #se for diferente o último caracter custo é 1
  
  return min(editDistance(s1, s2, len_s1 - 1, len_s2) + 1,
              editDistance(s1, s2, len_s1, len_s2 - 1) + 1,
              editDistance(s1, s2, len_s1 - 1, len_s2 - 1) + custo)


s1 = 'Hello'
s2 = 'Jello'
print(editDistance(s1, s2, len(s1), len(s2)))