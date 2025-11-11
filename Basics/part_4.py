# for i in range(10,0,-1):
#     print(i)

# n = 1
# while n <= 5:
#     print(n)
#     n+=1

# a = True 
# while a==True:
#     print("Aditya Sharma")
#     a+=1

## Continue - Skip current loop iteration 
## Pass - It is a null statement in python. Pass statement instructs to do nothing 
# for i in range(6):
#     if i == 6:
#         continue
#     print(i)

while True:
    a = int(input("Enter: "))
    for i in range(1,11):
        print(f" {i}  x {a}  = {i*a}")
    user_input = input("Do you want to exit: ")
    if(user_input == 'yes'):
        break


def function1():
    print("Hello world")

function1()

def add(a,b):
    result = a + b
    print(result)

add(5,2)

def area_circle(radius):
    pi = 3.14
    return pi*radius*radius

radi = float(input("Enter the radius: "))
print("Area of circle: ", area_circle(radi))



def greet(name = "Aditya"):
    print("Namaste sir,", name)

greet()
