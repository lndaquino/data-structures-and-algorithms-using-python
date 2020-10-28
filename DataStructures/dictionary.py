d = {}

d['joao'] = 20
d['maria'] = 18
d['pedro'] = 25

print(d)

for k in d.keys():
  print(k)

del d['joao']

if 'joao' in d.keys():
  print('chave encontrada')
else:
  print('chave não existe')

if 'maria' in d.keys():
  print('chave encontrada')
else:
  print('chave não existe')