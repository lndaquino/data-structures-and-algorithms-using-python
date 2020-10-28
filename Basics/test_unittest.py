import unittest

def fat(n):
  if(n==0):
    return 1
  return n * fat(n-1)

def pot(base,exp):
  if(exp==0):
    return 1
  return base * pot(base, exp-1)

class TestMathMethods(unittest.TestCase): #herda classe TestCase
  def test_pot(self):
    self.assertEqual(1024, pot(2,10))

  def test_fat(self):
    self.assertEqual(24, fat(4))

  #assertTrue
  #assertFalse

unittest.main()