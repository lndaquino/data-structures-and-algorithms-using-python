# vetor é matriz unidimensional / matriz é um vetor de vetores (multidimensional)
# matriz = [
#   [10,20,30,40],
#   [50,60,70,80],
#   [90,100,110,120]
# ]

# print(matriz[1][2])

notas = [
  ['joao', 8,7,6],
  ['pedro', 4.5, 9, 10],
  ['marcos', 6,6,8]
]

for line in notas:
  for col in line:
    print(str(col) + '\t', end = '')
  print('')