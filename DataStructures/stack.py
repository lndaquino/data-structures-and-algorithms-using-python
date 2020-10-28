# stack sempre insere ao final e tb remove sempre ao final - o primeiro a ser inserido é o último a ser removido - FILO (first in last out)

class Stack:
  def __init__(self):
    self.stack = []
    self.len_stack = 0

  def push(self, element):
    self.stack.append(element)
    self.len_stack += 1

  def pop(self):
    if not self.empty():
      self.stack.pop(self.len_stack - 1)
      self.len_stack -= 1

  def top(self):
    if not self.empty():
      return self.stack[-1]
    return None

  def empty(self):
    if(self.len_stack == 0):
      return True
    return False

  def length(self):
    return self.len_stack

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top())
print(s.empty())
s.pop()
print(s.top())
print(s.length())
s.pop()
s.pop()
print(s.empty())
print(s.top())