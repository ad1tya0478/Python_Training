def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def number_greater(a,b):
    if(a>b): print(a,"is greater")
    elif(b>a): print(b," is greater")
    else:  print("Equal")

a = 9
b = 8
# gmean1 = (a*b)/(a+b)
# print(gmean1)
calculateGmean(a,b)
number_greater(a,b)

c = 8
d = 7
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmean(c,d)
number_greater(c,d)