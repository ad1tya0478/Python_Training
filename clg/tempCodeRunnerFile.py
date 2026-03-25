num3 = 1234
num4 = str(abs(num3))
sum = 0
for i in num4:
    if i.isdigit():
        sum = sum + int(i)
    else:
        print("Invalid Input")
print(sum)