# s1 = {1,2,3,4,5,6,7,8,9,9,7,7,7,7,7,8,8,8}
# print(s1)

# s2 = {1,2,[1,2,3]}
# print(s2)  ## this will throw a typeError

## Union means combining all unique elements from both sets. 

# a = {1,2,3}
# b = {3,4,5}
# print(a.intersection(b))
# print(a.union(b))
# print(a.symmetric_difference(b))
# print(a.difference(b))

# l2 = [1,2,3,2,4,1,3,5]
# s3 = set(l2)
# print(s3)


## frozen set - is an immutable, unordered collection of unique elemenst, it is similar to a regular set but cannot be modified after creation.
# s4 = frozenset([1,2,3,3,4,2,1])
# print("frozenset: ", s4)
# print(type(s4))


# grade = int(input("Enter your Marks: "))
# if(grade >= 90 and grade <= 100):
#     print("Grade A(Excellent)")
# elif(grade >= 80 and grade < 90):
#     print("Grade B(Very Good)")
# elif(grade >= 70 and grade < 80):           
#     print("Grade C(Good)")
# elif(grade >= 60 and grade < 70):   
#     print("Grade D(Average)")
# elif(grade >= 50 and grade < 60):   
#     print("Grade E(Below Average)")
# else: 
#     print("Grade F(Fail)")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Enter operation (+, -, *, /): ")
if(choice == '+'): 
    result = num1 + num2
    print("Addition: ", result)
elif(choice == '-'):
    result = num1 - num2
    print("Subtraction: ", result)
elif(choice == '*'):
    result = num1 * num2
    print("Multiplication: ", result)   
elif(choice == '/'):    
    result = num1 / num2
    print("Division: ", result)
