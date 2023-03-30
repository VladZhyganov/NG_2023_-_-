a= int(input ("enter first coefficient a= "))
b= int(input ("enter secod coefficient b= "))
c= int(input ("enter third coefficient c= "))
import math
D=pow (b,2)-4*a*c
if D<0:
    print ("the equation has no real roots")
if D >= 0:
    print ("the equation has two roots")
    x1=(-b+(math.sqrt(D)))/(2*a)
    x2=(-b-(math.sqrt(D)))/(2*a)
    print ("x1=",x1)
    print ("x2=",x2)