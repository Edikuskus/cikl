from math import *
from re import X

for x in range(10):
    R=float(input("{0}.R: ".format(x)))
    if R>0:
        S=pi*R**2
    else:
        S="R peab > kui 0 olema"
    print("S={0}".format(S))

x=0
while True:
    x+=1
    R=float(input("{0}.R: ".format(x)))
    if R>0:
        S=pi*R**2
    else:
        S="R peab > kui 0 olema"
    print("S={0}".format(S))
    if x==10:
        break



x=0
while x<10:
    x+=1
    R=float(input("{0}.R: ".format(x+1)))
    if R>0:
        S=pi*R**2
        x+=1
    else:
        S="R peab > kui 0 olema"
    print("S={0}".format(S))
    if x==10:
        break


#1
t=0
for x in range(15):
    A=float(input("Sisesta A: "))
    if A.is_integer(): # 5.0, 5=True; 2.45=False
        t+=1
print(t)


#2
summa=0 
A=int(input("chislo A: "))
for x in range(1,A+1,1):
    summa+=x
print("summa: {0}".format(summa))


#3
p=1
predlozenie=""
for x in range(8):
    A=float(input("{0}. samm\nchislo: ".format(x+1)))
    if A>0:
        p*=A
        predlozenie=predlozenie+str(A)+"*"
print(predlozenie[:-1],"=",p)

#4