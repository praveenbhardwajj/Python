f=open("Day7 File IO in Python/Demo.txt","r")
# data=f.read(5) # return 5 char from start
data1=f.readline() # readline 1
data2=f.readline() # readline 2
data3=f.readline() # readline 3
print(data1) # line1
print(data2) # line2
print(data3) # line3
# print(type(data))
f.close()