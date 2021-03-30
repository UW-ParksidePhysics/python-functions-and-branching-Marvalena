#def F(a,b,c,x):
  #return a*(x**2) + b*x + c

#print (F(1,1,1,1))

from numpy.lib.scimath import sqrt
def roots(a,b,c):
  x_1=(-b+(sqrt(4*a*c)))/(2*a)
  x_2=(-b-(sqrt(4*a*c)))/(2*a)
  return x_1,x_2

def test_roots_float():
  test_roots=roots(1,-6,4)
  print (type(test_roots[0]), type(test_roots[1]))
  print (test_roots)
  return


def test_roots_complex():
  test_complex=roots(-1,-6,4)
  print (type(test_complex[0]), type(test_complex[1]))
  print (test_complex)
  return

test_roots_float()
test_roots_complex()