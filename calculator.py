num1 = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
num2 = float(input("Second number: "))

if op == "+": print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-": print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*": print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    print(f"{num1} / {num2} = {num1 / num2}" if num2 != 0 else "Error: Division by zero.")
else: print("Invalid operation.")
