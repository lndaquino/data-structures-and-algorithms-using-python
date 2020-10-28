'''
usado quando já sobreposição de subproblemas e subestrutura otima para se resolver o problema principal
subestrutura otima é qd chegamos a solução ótima do problema através da solução ótima se seus subproblemas
sobreposição de subproblemas é qd o algoritmo reexamina o mesmo problemas várias vezes
exemplo é solução do problema de Fibonacci, onde a implementação recursiva pode ser transformada de uma complexidade exponencial para complexidade linear
'''
n = 35

#sem progração dinâmica
def fib(n):
  if n == 1 or n == 2:
    return 1
  return fib(n - 1) + fib(n - 2)

mem = [-1 for i in range(n)]
mem[0] = mem[1] = 1
#com programação dinâmica
def fib_pd(n):
  if mem[n - 1] != -1:
    return mem[n-1]
  mem[n - 1] = fib_pd(n - 1) + fib_pd(n - 2)
  return mem[n - 1]

print(fib_pd(n))
print(fib(n))
