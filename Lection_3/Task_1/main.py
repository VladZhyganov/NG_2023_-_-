first_number = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
second_number = int(input("Enter second number: "))

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        print("Error: Division by zero!")
        return None
    return num1 / num2

if operator == "+":
    result = add(first_number, second_number)
elif operator == "-":
    result = subtract(first_number, second_number)
elif operator == "*":
    result = multiply(first_number, second_number)
elif operator == "/":
    result = divide(first_number, second_number)
else:
    print("Error: Invalid operator entered!")
    result = None

if result is not None:
    print(first_number, operator, second_number, "=", result)