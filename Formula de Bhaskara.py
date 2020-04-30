import math
a= int(input("Digite a:"))
b= int(input("Digite b:"))
c= int(input("Digite c:"))
 
x=(b**2)-(4*a*c)
if x<0:
  print ("Raiz negativa nao pode ser extraida.")

else:
  x=math.sqrt(x)
  x1=(-b+x)/(2*a)
  x2=(-b-x)/(2*a)
  print("x1 =",x1)
  print("x2 =",x2)