s = 'curso de Python'
#s[0] = 'C' #não pode fazer isso em Python pois string são imutáveis
s = 'C' + s[1:]
print(s)