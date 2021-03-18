#def C(F):
   #return (5./9.)*(F-32)



#F=2.
#print ('C, F')

#def C(F):
 #Cel=(5/9)*(F-32)
 #return Cel

#while F<=102:
 #print ('{:5.3f} {:3.1f}'.format(C(F), F))
 #print(C(F),F)
 #F=F+10
   
def C(F):
  C = (5.0/9) * (F - 32)
  return C
 
dF = 10
F = 68
print(f'{"F":>5s} {"C(F)":>5s}')
while F <= 100:
 print( '%5.1f %5.1f' % (F, C(F)))
 F += dF
print('-----')
 
def F(c):
 F = ((9.0/5) * c) + 32
 return F
 
c = 4
print(f'{"C(F(c))":>3}')
print('%5.1f' % (C(F(c))))