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