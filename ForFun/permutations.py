import itertools

'''
gerando todas as permutações
permutações de (1,2,3) = 
(1,2,3)
(1,3,2)
(2,1,3)
(2,3,1)
(3,1,2)
(3,2,1)
'''

lista = [1,2,3]
print(list(itertools.permutations(lista)))