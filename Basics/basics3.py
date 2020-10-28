#expressões lambdas não precisam ser nomeadas, podem ser anonimas
# def pot2(x):
#   return x ** 2

# sqr = lambda x: x**2

# print(pot2(5))
# print(sqr(4))

# def fat(n):
#   if (n == 0):
#     return 1
#   return (n * fat(n-1))

# fat_ = lambda n: n * fat_(n-1) if n > 1 else 1

# print(fat_(5))

# lista = [1,2,3,4]
# # m = map(lambda x: x**2, lista)
# # for i in m:
# #   print(i)

# import functools
# print(functools.reduce(lambda x,y: x+y, lista))

f = filter(lambda x: x%2 == 0, range(10))
for i in f:
  print(i)