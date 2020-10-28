import random # gerando numeros pseudo aleatorios

print(random.randrange(4)) #retorna numero inteiro entre 0 e 3 - parametro é limite superior aberto

a = random.randint(1,4) #retorna inteiro no intervalor com limites fechados (inclusive)

lista=[1,2,3,4]
b=random.choice(lista) #seleciona aleatoriamente um elemento da lista
random.shuffle(lista) #embaralha a sequencia e retorna a nova sequencia nela mesmo - perde-se a ordem original
print(lista)

c=random.sample(lista,3) #pega qtd de amostras da sequencia
print(c)

print(random.random()) #gera um numero float entre 0 e 1 exclusive
print(random.uniform(1,10)) #gera float entre o intervalo superior aberto