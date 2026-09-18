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