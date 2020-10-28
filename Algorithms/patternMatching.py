'''
text processing using brute force for patter matching
ideia é encontrar padrão (palavra, substring etc) dentro de um texto
task - buscar métodos mais otimizados, que retornem multiplas posições do padrão encontrado e pode ser escolhido em ignorar maiuscula/minuscula (por enquanto só retorna o primeiro encontrado)
'''
def bruteForce(text, pattern):
  lenText, lenPattern = len(text), len(pattern)

  for i in range(lenText - lenPattern + 1):
    j = 0
    while j < lenPattern and text[i + j] == pattern[j]:
      j += 1

    if j == lenPattern:
      return i #substring text[i : i+j] corresponde a pattern

  return -1

text = 'Python é uma excelente linguagem, pois python é muito fácil de aprender.'
pattern = 'python'
print(bruteForce(text, pattern))