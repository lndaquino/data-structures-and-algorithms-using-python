#adivinhe o numero
import random

num = random.randint(1,100)

while True:
  resp = input('Digite um número: ')
  n = int(resp)

  if n < num:
    print('Mais para cima')
  elif n > num:
    print('Mais para baixo')
  else:
    print('Parabéns, você acertou!!!')
    break

