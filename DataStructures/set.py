#conjunto ou set
'''
conjunto é coleção não ordenada que não possui elementos duplicados
objetos set suportam operação matemática como união, intersecção, diferença
usa-se {} ou a função set()
mais rápido q lista []
c1 = {1,2,3}
c2 = {'marcos, maria, yankee}
c3 = {1, 'marcos', 3.14}
c4 = set([1,2,2,3,3]) # se der print vai ver q removeu elementos duplicados
análise assintótica de custo de processamento:
união: O(m+n)
interseçcão: O(min(m,n))
diferença: O(m)
'''
c = {'marcos', 'maria', 'josé'}
print(len(c))
if 'lucas' in c:
  print('elemento encontrado')

#operações
c1 = {1,2,3,4}
c2 = {3,4,5,6}

print(c1 | c2) #união
print(c1 & c2) #intersecção
print(c1 - c2) #diferença
print(c2 - c1) #diferença

c1.remove(1)
print(c1)