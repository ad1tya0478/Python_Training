# name=input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(name)
# print(age)

# num1 = int(input("Enter 1st Number: "))
# num2 = int(input("Enter 2nd Number: "))
# print(num1 + num2)

# # eval - this function automatically detects the datatype and generate output according to it, note - the string input needs to be winthin quotation.
# name1 = eval(input("Enter your name: "))
# age1 = eval(input("Enter your age: "))
# height = eval(input("Enter your height: "))
# print(name1)
# print(age1)
# print(height)


# length = int(input("Enter no.1: "))
# breadth = int(input("Enter no.2: "))
# print("Area: ", length * breadth)


# 1
# num=int(input("Enter number: "))
# if num>0:
#     print("Positive Number")
# elif num==0:
#     print("zero")
# else: 
#     print("Negative Number")

# # 2
# a = input("Enter no.1: ")
# b = input("Enter no.2: ")

# if a.isdigit() and b.isdigit():
#     a = int(a)
#     b = int(b)

#     if a % 10 == b % 10:
#         print("True")
#     else:
#         print("False")
# else:
#     print("Invalid")

# a = 0
# rang = int(input("Enter the range: "))
# for i in range(1,rang): 
#     a = a + i
# print(a)

# # abs() function - this function returns the absolute value of a number, making it positive regardless of its original sign.
# # 3 
# num3 = 1234
# num4 = str(abs(num3))
# sum = 0
# for i in num4:
#     if i.isdigit():
#         sum = sum + int(i)
#     else:
#         print("Invalid Input")
# print(sum)

# ord() function - returns the Unicode code of a given single character. if the length is more than one when you give something in this function, a type error will be raised.
# chr() function - this function returns a string representing a character whose unicode code points is the integer specified. 

# 4 
import random
gus=random.randrange(1,100)
choice = input ("If you want to play game (Y,N) Enter Your Choice: ")
if choice == "Y":
    times = int(input ("how many times do you want to play the game: "))
    for i in range (times):
        if choice == 'Y':
            num = int(input("Enter the Number(1-100): "))
            if num<gus:
                print("The Number is too low")
            elif num>gus:
                print("The Number is too high") 
            else:
                print("You got it!")
        else:
            break        

               
