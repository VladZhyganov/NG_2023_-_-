print("To calculate, enter the first number, then the action sign, and the second number.")
first_number = int(input("Enter first number: "))
sign = input("Enter action sign: ")
second_number = int(input("Enter second number: "))

if sign == '+':
    print(first_number, "+", second_number, "=", first_number + second_number)
elif sign == '-':
    print(first_number, "-", second_number, "=", first_number - second_number)
elif sign == '*':
    print(first_number, "*", second_number, "=", first_number * second_number)
elif sign == '/' and second_number != 0:
    print(first_number, "/", second_number, "=", first_number / second_number)
else:
    print("Incorrect action sign or division by 0.")