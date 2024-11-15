# Get the user's input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the mthematical operation (+, -, *, /): ")

# Pecrform operation based on the user's input
if operation == "+":
   result = num1 + num2
elif operation == "-":
   result = num1 - num2
elif operation == "*": 
    result = num1 * num2
elif  operation == "/":
    result = num1 / num2
else:
    print("Invalid operation")

# print the result

print(f"{num1} {operation} {num2} = {result}")      