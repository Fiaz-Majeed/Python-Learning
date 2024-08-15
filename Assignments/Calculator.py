#user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
#perform operation
if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation ==  "/":
    if b != 0:
        result = a / b
    else:
        result = "Error: division by zero not allowed"
else:
    result = "Invalid operation"

print("output:", result)
#varibale method
a = 3
b= 8
add = a + b
minus = a - b
multiply = a * b
divide = a / b
print('addition', add)
print("subtraction", minus)
print("multiplication", multiply)
print("division", divide)
print(f"{a**b}")
