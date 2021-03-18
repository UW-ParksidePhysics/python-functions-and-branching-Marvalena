from math import pi, cos, sin
print('Part a')
def trapzint1(f, a, b):
 F = ((b - a)/2) * (f(a) + f(b))
 return F
 
print('Part b')
testtrap1 = (pi - 0)/2 * (cos(pi) + cos(0))
testtrap2 = (pi - 0)/2 * (sin(pi) + sin(0))
testtrap3 = (pi/2 - 0)/2 * (sin(pi/2) + sin(0))
error1 = 0 - testtrap1 #int of cos = sin(pi) - sin(0) = 0
error2 = 2 - testtrap2 #int of sin = -cos(pi) + cos(0) = 2
error3 = 1 - testtrap3 #int of sin = -cos(pi/2) + cos(0) = 1
 
print('Part c')
def trapzint2(f, a, b):
 H = h(x)
 return H
 
def test_trap():
 def g(x):
  return f(x) #integrand (input)
 
 def G(x):
  return ((b - a)/2) * (f(a) + f(b)) #result of integration (output)
#Values of integration
a = 0
b = pi
n = 10
exact = G(b) - G(a)
approx = trap(g, a, b, n)
success = abs(exact - approx) < 1E-14
if not success:
 print('you suck at this')
 
print('Part d')
def trap(f, a, b, n=10):
 h = (b - a)/float(n) 
 sum1 = 0
 for i in range(1, n):
  sum1 += h(f((a + i) * h) + f(((a + i) * h) + 1))
 integral = (0.5)*sum1
 return integral
 
#print('Part e')
#def trap(f, a, b, n=10):
 #h = (b - a)/float(n) 
 #sum1 = 0
 #for i in range(1, n):
  #sum1 += (f((a + i) * h)
  #integral2 = (0.5) * h * (f(a) + f(b)) + h * sum1
 #return intergal2



 
#def Simpson(f, a, b, n=500):
 #h = (b - a)/float(n)
 #sum1 = 0
 #for i in range(1, n/2 + 1):
 #sum1 += f(a + (2*i-1)*h)
 #sum2 = 0
 #for i in range(1, n/2):
 #sum2 += f(a + 2*i*h)
 #integral3 = (b-a)/(3*n)*(f(a) + f(b) + 4*sum1 + 2*sum2)
 #return integral3