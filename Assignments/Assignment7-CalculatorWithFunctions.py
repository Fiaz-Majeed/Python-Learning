#user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
#perform operation
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation ==  "/":
        if b != 0:
            return a / b
        else:
            print("Error: division by zero not allowed")
    else:
        print("Invalid operation")
  
print(int(calculator(a, b, operation)))
