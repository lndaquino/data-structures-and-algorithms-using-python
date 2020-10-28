# manipulando listas
lista1 = [1,2,3,4]
lista2 = [5,6,7,8,9,10]
lista3 = lista1 + lista2 #união de listas
# print(lista3)

# lista3.pop(0) #remove elemento da posição / len(lista) -1 remove o último elemento
# print(lista3)


# lista3.remove(3) #remove pelo elemento / remove o elemento 3, se não existir dá erro
# print(lista3)

# num=11
# if num in lista3:
#   print('elemento encontrado')
#   lista3.remove(num)
# else:
#   print('elemento não encontrado')

# print(lista3)
t_lista=tuple(lista1) #transforma para tupla imutável
print(t_lista)

lista3.append(11)
print(lista3)

lista3.insert(1,10) #insere elemento 10 na 2a posição da lista
print(lista3)

lista4=[4, 10, 2, 1]
lista4.sort()
print(lista4)
print(lista4[-1]) #último elemento
print(lista4[1:3]) #pega do segundo ao terceiro elemento - limite superior aberto
print(lista4[1:]) #pega do segundo até o final da lista
print(lista4[::-1]) #inverte a lista
print(lista4[-4]) #dá pra referenciar a lista ao contrário tb