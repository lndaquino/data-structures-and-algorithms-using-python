import numpy as np

matriz = np.array([[ 1, 2, 3, 4, 5, 6, 7, 8],
                   [ 9,10,11,12,13,15,15,16],
                   [17,18,19,20,21,22,23,24]])

mat = np.matrix([ [1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(matriz[1::2, ::2])
print(matriz)

mask = mat < 6
print(mat[mask])

transposta = mat.transpose()
print(transposta)
