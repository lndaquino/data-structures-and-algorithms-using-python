#similaridade baseada no algoritmo de Ratcliff ad Obershelp com otimizações para reduzir worst case de cubico para quadrático
from difflib import SequenceMatcher


def similar(s1, s2):
  return SequenceMatcher(None, s1, s2).ratio()


print(similar('Python', 'Pytohn'))
print(similar('Marcos', 'Marcus'))
print(similar('Python', 'Java'))
print(similar('Python', 'PHP'))