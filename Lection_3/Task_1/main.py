print ("to calculate, enter the first number and press ENTER, then the action sign, press ENTER, and the second number, press ENTER")
first_number= int(input ("enter first number_ "))
sign= (input ("enter action sign_ "))
second_number= int(input ("enter second number_"))
def sum(first_number,second_number):
    result = (first_number+second_number)
    return result
def substrakt(first_number,second_number):
    result = (first_number-second_number)
    return result
def multiplay(first_number,second_number):
    result = (first_number*second_number)
    return result
def divid (first_number,second_number):
    result = (first_number/second_number)
    return result
if sign in ('+','-','/','*'):
    if  sign==  '+':
        result= sum  (first_number,second_number)
    elif  sign== '-':
        result= substrakt(first_number,second_number)
    elif  sign== '*':
        result=multiplay(first_number,second_number)
    elif  sign== '/' :
        if second_number ==0:
            print ("division by 0 is prohibited!")
        else: 
            result = divid (first_number,second_number) 
else: 
    print  ("incorrect action sign")
print (first_number,sign,second_number,"=",result)