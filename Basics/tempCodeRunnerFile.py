string = input("Enter a string: ")

result = ""

for char in string:
    if not char.isdigit():
        result += char

print("Result:", result)