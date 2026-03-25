

file = open("C:/Users/HP/Desktop/r.txt","r")
print(file.read())
file.close()

file = open("C:/Users/HP/Desktop/r.txt","r")
print(file.read(4))
file.close()

file = open("C:/Users/HP/Desktop/r.txt","r")
print(file.readline())
file.close()

file = open("C:/Users/HP/Desktop/r.txt","r")
print(file.readline(2))
file.close()

file = open("C:/Users/HP/Desktop/r.txt","r")
print(file.readlines())
file.close()

file = open("C:/Users/HP/Desktop/r.txt","w")
file.write("Hello world")
file.write("Overwrite karwadiya mkl ne, code chala gaya bhenchod")
file.close()

file = open("C:/Users/HP/Desktop/mkc.txt","x")
file.write("New file - sabki mkc")
file.close()

import os
if os.path.exists("C:/Users/HP/Desktop/mkc.txt"):
    os.remove("C:/Users/HP/Desktop/mkc.txt")
else:
    print("this file does not exist")