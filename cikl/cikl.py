﻿from math import *
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
predlozhenie=""
for x in range(8):
    A=float(input("{0}. samm\nchislo: ".format(x+1)))
    if A>0:
        p*=A
        predlozhenie=predlozhenie+str(A)+"*"
print(predlozhenie[:-1],"=",p)



#15
for y in range(10):
    for x in range(10):
        print(x,end=" ")
    print()


#29
for i in range(9):
    for x in range(9):
        if x==0 or i==x:
            print("0",end=" ")
    else:
        print("0",end=" ")
    print()



#4
for number in range(10,21):
    kvadrat=number ** 2
    print("kvadrat chisel ot 10 do 20\n{0}: {1}".format(number,kvadrat))


#8
for djuim in range(1, 21):
    float(input("perevod djuim ot 1 do 20: "))
    centimeters = djuim * 2.54  

    print("{0} djuim = {1} santimetr".format(djuim,centimeters))


#12
summa=0
for x in range(1,10):
    N=int(input("skolko gazonokosilik?: "))
    m=int(input("skolko vremeni rabotala odna gazonokosilka?: "))
    
    m+10
    print("vsa brigata otrabotala {0}".format(m))

#12
from random import *
N=randint(2,10)
m=randint(1,10)
summa=0
print("masinad: ", N)
print("tunnid: ", m)
for t in range(N-1):
    summa+=m
    m=(m/6)*7
    print(m)
print("kokku masinad töötasid: ",summa,"tn")


#19
for x in range(20,51):
    if x % 3 == 0 and x % 5 != 0:
        print(x)

#20 
for x in range(35,88):
    if x % 7 in [1,2,5]:
        print(x)


#end
print("wewe")