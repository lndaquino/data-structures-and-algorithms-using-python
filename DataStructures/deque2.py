from collections import deque

d = deque()
d.append(1) #adiciona do lado direito do deque
d.appendleft(2) #adiciona do lado esquerdo
d.append(3)
d.appendleft(4)
d.pop()
d.popleft()
d.remove(2) # remove o elemento

for i in d:
  print(i, end = ' ')