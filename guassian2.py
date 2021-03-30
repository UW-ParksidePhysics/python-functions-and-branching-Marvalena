from math import sqrt, exp, pi

def gauss(x, m=0, s=1):
    gaussian = 1 / (sqrt(2 * pi) * s) * exp(-0.5 * ((x - m) / s) ** 2)
    return gaussian

print(f'{"x":>3s} {"Gaussian":>s}')
for x in range(-5, 6):
  print (('%3d' % x), ('%.7f' % gauss(x)))