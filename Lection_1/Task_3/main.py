print ("to calculate, enter the first number and press ENTER, then the action sign, press ENTER, and the second number, press ENTER")
first_number= int(input ("enter first number_ "))
sign= (input ("enter action sign_ "))
second_number= int(input ("enter second number_"))
if sign in ('+','-','/','*'):
    if  sign==  '+':
        print  (first_number,"+",second_number,"=",first_number+second_number)
    if  sign== '-':
        print  (first_number,"-",second_number,"=",first_number-second_number)
    if  sign== '*':
        print  (first_number,"*",second_number,"=",first_number*second_number)
    if  sign== '/' :
        if second_number ==0:
            print ("division by 0 is prohibited!")
        else: 
            print  (first_number,"/",second_number,"=",first_number/second_number)
else: 
    print  ("incorrect action sign")