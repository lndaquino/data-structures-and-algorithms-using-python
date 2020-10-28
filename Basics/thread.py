from threading import Thread
import time

def my_func(i):
  print('Iniciando a thread %d' % i)
  time.sleep(5)
  print('Thread %d finalizada' % i)

for i in range(10):
  t = Thread(target=my_func, args=(i,))
  t.start()