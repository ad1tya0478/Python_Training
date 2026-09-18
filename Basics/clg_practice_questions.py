# Program to reverse a string

string = input("Enter a string: ")

reversed_string = string[::-1]

print("Reversed string:", reversed_string)


# Program to remove numbers from a string

string = input("Enter a string: ")

result = ""

for char in string:
    if not char.isdigit():
        result += char

print("Result:", result)

# Program to check if a string contains a substring

string = input("Enter the string: ")
target = input("Enter the substring: ")

if target in string:
    print(True)
else:
    print(False)


# Python program to find the sum of all numeric items in a dictionary

d = {'x': 25, 'y': 18, 'z': 45, 'a': "C", 'd': 'isinstance'}

total = 0

for value in d.values():
    if isinstance(value, (int, float)):
        total += value

print(total)

# Python program to check if two lists have at least one common element using set

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

result = bool(set(a) & set(b))

print(result)



# Program to find maximum and minimum in a list

print("Aditya Sharma\nBCAN1CA24013")
lst = list(map(int, input("Enter elements: ").split()))

max_val = lst[0]
min_val = lst[0]

for num in lst:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max =", max_val, ", Min =", min_val)


# Program to remove empty tuples from a list

print("Aditya Sharma\nBCAN1CA24013")
lst = [(), ('ram','15','8'), (), ('laxman','sita'), ('krishna','akbar','45'), ("",""), ()]

result = []

for t in lst:
    if t != ():
        result.append(t)

print("Empty Tuple Removed = ",result)

# Program to create list of tuples with number and its cube

print("Aditya Sharma\nBCAN1CA24013")
lst = list(map(int, input("Enter elements: ").split()))

result = []

for num in lst:
    result.append((num, num**3))

print("List having both = ",result)

# Program to add tuple to list and list to tuple

print("Aditya Sharma\nBCAN1CA24013")
lst = [5, 6, 7]
tup = (9, 10)

# Tuple to List
result_list = lst + list(tup)

# List to Tuple
result_tuple = tup + tuple(lst)

print("List result:", result_list)
print("Tuple result:", result_tuple)


# Program to reverse words in a string
print("Aditya Sharma\nBCAN1CA24013")
string = input("Enter a string: ")

words = string.split()
reversed_words = words[::-1]

result = " ".join(reversed_words)

print(result)

# Program to check Positive, Negative or Zero

print("Aditya Sharma\nBCAN1CA24013")
num = input("Enter a number: ")

if not num.lstrip('-').isdigit():
    print("Invalid")
else:
    num = int(num)
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")


# Program to check if two numbers have same last digit
print("Aditya Sharma\nBCAN1CA24013")
a = input("Enter first number: ")
b = input("Enter second number: ")

if not (a.isdigit() and b.isdigit()):
    print("Invalid")
else:
    a = int(a)
    b = int(b)
    
    if a < 0 or b < 0:
        print("Invalid")
    else:
        if a % 10 == b % 10:
            print(True)
        else:
            print(False)


# Program to find sum of digits using abs()
print("Aditya Sharma\nBCAN1CA24013")
num = input("Enter a number: ")

if not num.lstrip('-').isdigit():
    print("Invalid Number")
else:
    num = abs(int(num))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    print(total)


# Program to convert ASCII to character and vice-versa
print("Aditya Sharma\nBCAN1CA24013")
val = input("Enter a value: ")

# Case 1: Character to ASCII
if len(val) == 1 and not val.isdigit():
    print(ord(val))

# Case 2: Number to Character
elif val.isdigit() or (val.startswith('-') and val[1:].isdigit()):
    num = int(val)
    if 0 <= num <= 127:
        print(chr(num))
    else:
        print("Invalid Number")

# Invalid case
else:
    print("Invalid Number")


# Program to check Even or Odd
print("Aditya Sharma\nBCAN1CA24013")
num = input("Enter a number: ")

if not num.isdigit():
    print("Invalid Number")
else:
    num = int(num)
    
    if num <= 0:
        print("Invalid Number")
    else:
        if num % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")


# Program to print multiplication table
print("Aditya Sharma\nBCAN1CA24013")
num = input("Enter a number: ")

if not num.isdigit():
    print("Invalid Number")
else:
    num = int(num)
    
    if num < 1:
        print("Invalid Number")
    else:
        for i in range(1, 11):
            print(f"{num} * {i} = {num * i}")

# Program to print digit pattern
print("Aditya Sharma\nBCAN1CA24013")
num = input("Enter a number: ")

if not num.isdigit():
    print("Invalid Number")
elif int(num) < 1:
    print("Invalid Number")
else:
    for digit in num:
        print("*" * int(digit))

# Program to print half diamond pattern
print("Aditya Sharma\nBCAN1CA24013")
num = input("Enter a number: ")

if not num.isdigit():
    print("Invalid")
else:
    num = int(num)
    
    if num <= 0:
        print("Invalid")
    else:
        # Upper half
        for i in range(1, num + 1):
            print("*" * i)
        
        # Lower half
        for i in range(num - 1, 0, -1):
            print("*" * i)


# Program for Weird / Not Weird
print("Aditya Sharma\nBCAN1CA24013")
num = input("Enter a number: ")

if not num.isdigit():
    print("Invalid Number")
else:
    num = int(num)
    
    if num < 1:
        print("Invalid Number")
    elif num % 2 != 0:
        print("Weird")
    elif 3 <= num <= 6:
        print("Not Weird")
    elif 7 <= num <= 24:
        print("Weird")
    else:
        print("Not Weird")


# Program to perform arithmetic operations
print("Aditya Sharma\nBCAN1CA24013")
a = input("Enter first number: ")
b = input("Enter second number: ")

if not (a.lstrip('-').isdigit() and b.lstrip('-').isdigit()):
    print("Invalid Number")
else:
    a = int(a)
    b = int(b)
    
    print(a + b)
    print(a - b)
    print(a * b)