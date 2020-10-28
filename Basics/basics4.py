# recursividade
# #fatorial
# def fat(n):
#   if(n == 0):
#     return 1
#   return n * fat(n-1)

# print(fat(3))

# fibonacci = 1, 1, 2, 3, 5 (soma dos dois membros anteriores, os dois primeiros são 1)
def fib(n):
  if(n == 1 or n == 2):
    return 1
  return fib(n - 1) + fib (n - 2)

print(fib(5))

# def pot(base, exp):
#   if(exp == 0):
#     return 1
#   return base * pot(base, exp-1)

# print(pot(2,8))