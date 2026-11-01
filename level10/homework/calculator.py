#calculator
num_1 = float(input("Enter your first number: "))
operation = input("Enter operation (+, -, *, /: ")
num_2 = float(input("Enter your second number: "))

if operation == "+":
    print(num_1 + num_2)

elif operation == "-":
    print(num_1 - num_2)

elif operation == "*":
    print(num_1 * num_2)

elif operation == "/":
    print(num_1 / num_2)
else:
    print("somethin is worng.")