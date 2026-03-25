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