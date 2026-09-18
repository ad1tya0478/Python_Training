import numpy as np

# my_list = [1,2,3,4]
# my_list = my_list * 2
# print(my_list)

# array = np.array([1,2,3,4,5])
# array = array * 2
# print(array)
# print(type(array))

# array = np.array([['A','B','C'], ['D','E','F'], ['G','H','I']])
# # print(array.ndim) # gives the dimensions of the array 
# # print(array.shape) # for 2d arrays( rows, cols) for 3d its (layers, rows, cols)

# print(array[0][0])

# word = array[0,0] + array[1, 0] + array[2, 2]
# print(word)


# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

#arr[start:end:step]
# print(arr[0])
# print(arr[-1])
# print(arr[-2])

# print(arr[0:2])
# print(arr[0:3])
# print(arr[0:])

# print(arr[::2])
# print(arr[::-2])

# print(arr[:, 0])
# print(arr[:, 0:3])
# print(arr[:, 1:])
# print(arr[:, ::2])
# print(arr[:, 1::2])
# print(arr[:, ::-1])

# print(arr[0:2, 2:4])
# print(arr[2:, 0:2])


# ---- Scalar arithmetic 
# array = np.array([1,2,3])
# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array / 4)
# print(array ** 5)

# ----- Vectorized math functions 
# array1 = np.array([1.01,2.5,3.99])
# print(np.sqrt(array1)) # gives the square root 
# print(np.floor(array1)) # rounds down 
# print(np.round(array1)) # rounds off to the nearest side
# print(np.ceil(array1))  # rounds up 
# print(np.pi)

# 1 
# radii = np.array([1,2,3])
# print(np.pi * radii ** 2)

# 2 
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)
# print(arr1 ** arr2)

# Comparison Operators 
# scores = np.array([91, 55, 100, 73, 82, 64])
# print(scores == 100)
# print(scores >= 60)

# scores[scores < 60] = 0
# print(scores)


# BroadCasting allows numpy to perform operations on arrays with different shapes by virtually expanding dimensions so they match the larger array's shape
# The dimensions have the same size
# OR 
# One of the dimensions has a size of 1

# arr1 = np.array([[1,2,3,4]])
# arr2 = np.array([[1], [2], [3], [4]])

# print(arr1.shape)
# print(arr2.shape)
# print(arr1 * arr2)

# arr3 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# arr4 = np.array([[1], [2], [3], [4]])

# print(arr3.shape)
# print(arr4.shape)
# print(arr3 * arr3)

# arr5 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# arr6 = np.array([[1,2], [2,3], [3,4], [4,5]])

# print(arr5.shape)
# print(arr6.shape)
# print(arr5 * arr6)



# array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
# array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

# print(array1.shape)
# print(array2.shape)
# print(array1 * array2)



# ----- Aggregate Functions = summarize data and typically returns a single value
# array = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print(np.sum(array)) # Addition
# print(np.mean(array))  # Mean
# print(np.std(array))   # Standard Deviation
# print(np.var(array))   # Variance 
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array))  # WHat is the position of the minimum value
# print(np.argmax(array))

# print(np.sum(array, axis=0))  # we can also pass a second argument, where i can select an axis, if axis = 0, then we are applying this fuction to all the columns, and if the axis = 1, the sum will be of all the rows 


# ------- Filtering = Refers to the process of selecting elements from an array that match a given condition

# ages = np.array([[21,17,19,20,16,30,18,65], [39,22,15,99,18,19,20,21]])

# teenagers = ages[ages < 18]
# adults = ages[(ages >= 18) & (ages < 65) ]
# seniors = ages[ages >= 65]
# evens = ages[ages % 2 == 0]
# odds = ages[ages % 2 != 0]

# adults2 = np.where(ages >= 18, ages, 0)  # this returns a new array 
# print(adults2)



# ------- random number 

rng = np.random.default_rng(seed=1) # by putting a seed we get the same results 

# print(rng.integers(1, 7))
# print(rng.integers(low=1, high=101, size=(3,2)))


# -- for floating point number

# np.random.seed(seed=1)
# print(np.random.uniform(low=-1, high=1, size=3))

# -- shuffling an array

# rng = np.random.default_rng()
# array = np.array([1,2,3,4,5])
# rng.shuffle(array)
# print(array)

# -- random choice
rng = np.random.default_rng()
fruits = np.array(["apple","orange","banana", "coconut", "pineapple"])
fruit = rng.choice(fruits, size=3)
print(fruit)


