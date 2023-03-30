print ("to calculate, enter the first number and press ENTER, then the action sign, press ENTER, and the second number, press ENTER")
a= int(input ("enter first number_ "))
b= (input ("enter action sign_ "))
c= int(input ("enter second number_"))
if b in ('+','-','/','*'):
    if  b==  '+':
        print  (a,"+",c,"=",a+c)
    if  b== '-':
        print  (a,"-",c,"=",a-c)
    if  b== '*':
        print  (a,"*",c,"=",a*c)
    if  b== '/' :
        if c ==0:
            print ("division by 0 is prohibited!")
        else: 
            print  (a,"/",c,"=",a/c)
else: 
    print  ("incorrect action sign")