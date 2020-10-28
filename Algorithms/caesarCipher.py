'''
é um dos algoritmos mais simples de criptografia
substitui uma letra do alfabeto por outra letra - o q determina por qual letra será substituida é a qtd de posições de deslocamento
x é a posição da letra
n é deslocamento desejado
26 é a qtd de letras
criptografa(letra) = (x + n) % 26,
criptografa(A) = (0 + 23) % 26 = 23 = X
criptografa(D) = (3 + 23) % 26 = 0 = A
descriptografa(letra) = (x - n) % 26
'''
#key é o deslocamento
def encript(text, key):
  lista = list(text)
  texto_criptografado = ''
  ord_A = ord('A')

  for i in lista:
    ord_c = (ord(i) - ord_A + key) % 26
    texto_criptografado += chr(ord_c + ord_A)

  return texto_criptografado

def decript(text, key):
  lista = list(text)
  texto_descriptografado = ''
  ord_A = ord('A')

  for i in lista:
    ord_c = (ord(i) - ord_A - key) % 26
    texto_descriptografado += chr(ord_c + ord_A)

  return texto_descriptografado

text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 23
encripted = encript(text, key)
print(encripted)
decripted = decript(encripted, key)
print(decripted)