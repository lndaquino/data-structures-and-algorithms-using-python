def fatorial(num):
  if num==0:
    return 1
  return num * fat(num-1)

def eh_par(num):
  if(num % 2 == 0):
    return True

def test_fatorial():
  assert fatorial(0) == 1

def test_eh_par():
  assert eh_par(10) == True