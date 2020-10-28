#unpack - desempacotamento
lista = [1,2,3]
a,b,c=lista
print(a)
print(b)
print(c)

x,y,_ = lista #não me interessa os elementos com _
print(x)
print(y)

nome = 'abc'
c1,c2,_=nome
print(c1)
print(c2)

def func(x,y=3): #parametro opcional
  return x**2,y**2

r1,r2 = func(2,4)
print(r1)
print(r2)