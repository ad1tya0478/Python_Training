
import numpy as np
from numpy import linalg as LA

# print(np.__version__)

# a = np.array([1,2,3,4,5])
# b = np.zeros((2,3))
# c = np.ones((3,3))
# d = np.full((2,2),5)
# e = np.arange(0,10,2)
# f = np.linspace(0,1,5)

# print("Normal array:\n ", a)
# print("Zeros array:\n ", b)
# print("Ones array:\n ", c)
# print("Full array:\n ", d)
# print("Arange array:\n ", e)
# print("Linspace array:\n ", f)


# arr = np.array(([1,2,3],[4,5,6]))
# print("Shape: ", arr.shape)
# print("Dimension: ", arr.ndim)
# print("Size: ", arr.size)
# print("Dtatype: ", arr.dtype)

# reshaped = arr.reshape(3,2)
# print("Reshaped array: ", reshaped)


# x = np.array([1,2,3])
# y = np.array([4,5,6])
# print("Addition: ", x + y)
# print("Subtraction: ", x - y)
# print("Multiplication: ", x * y)
# print("Division: ", x / y)


# data = np.array(([1,2,3],[4,5,6]))
# print(np.sum(data)) # Sum
# print(np.mean(data)) # Mean
# print(np.std(data))  # Standard deviation
# print(np.max(data))  # Max
# print(np.min(data))  # Min
# print(np.sum(data, axis=0))  # Coloumn-wise Sum


# x = np.array(([1,2,3],[4,5,6]))
# y = np.array([1,0,1])
# print("Broadcasting Result: ", x + y)


# M = np.array(([1,2],[3,4]))
# print("Transpose: ", M.T)
# print("Determinant: ",LA.det(M))
# print("Inverse: ", LA.inv(M))


data1 = np.random.randint(0,255,(3,3))
print("Original Data:\n", data1)

normalized = data1/255.0
print("Normalised Data:\n", normalized)





