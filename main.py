# main.py

from calculator.operations import add, subtract, multiply, divide

print("Welcome to Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == "+":
    print("Result:", add(a, b))
elif op == "-":
    print("Result:", subtract(a, b))
elif op == "*":
    print("Result:", multiply(a, b))
elif op == "/":
    try:
        print("Result:", divide(a, b))
    except ValueError as e:
        print("Error:", e)
else:
    print("Invalid operation")
