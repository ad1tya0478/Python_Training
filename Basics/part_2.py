# a = [1,2,3,4,5,7]
# print(a)
# b = ['a','b','c',1,2,3,4,5]
# print(b)

# name = ['a','d','i','t','y','a']
# print(name)


# l1 = [10,20,30,40,50]
# print(l1[0],l1[2],l1[3])
# print(l1[:5:2])
# l1.append('kivi')
# print(l1)

# l2 = [1,2,3,4,5]

# l2.remove(1)
# print(l2)

# l2.pop(3)
# print(l2)

# l2.clear()
# print(l2)

# del l2[1]
# print(l2)

# fruit = ['apple','banana','cherry','apple']

# print(fruit.index('banana'))
# print(fruit.count('apple'))

### nested list 
# matrix = [[1,2,3],[4,5,6]]

# print(matrix[0])
# print(matrix[0][2])

### Sort
# l3 = [1,33,22,56,33,2,56,87,32]
# l3.sort()
# print(l3)

### tuple 
t = (1,2,3)
print("tuple : ", t)
print(type(t))

t2 = (1,2,['a','b'],3.9,True,'a')
print("mixed tuple: ",t2)
print(type(t2))

# we have to change the tuple to list, only then we can add something 
t = list(t)
t[0] = 10
t = tuple(t)
print(t)

