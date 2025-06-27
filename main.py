HEAD
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

import numpy as np

# Create a 2D array (matrix)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix addition
C = A + B
print("\nA + B:")
print(C)

# Matrix multiplication (dot product)
D = np.dot(A, B)
print("\nA dot B:")
print(D)

# Element-wise multiplication
E = A * B
print("\nA * B (element-wise):")
print(E)

# Transpose of a matrix
print("\nTranspose of A:")
print(A.T)
951438c11eb4c879dca2ed998afc983c0a5dfa36
