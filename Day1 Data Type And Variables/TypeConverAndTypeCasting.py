    # Type Conversion and Type Casting in Python

#Type Conversion
a = 10       # int
b = 5.5      # float
c = "20"     # str

print("Before Type Conversion : ")  
print("Type of a is : ",type(a))    # int

print("Type of b is : ",type(b))   # float
print("Type of c is : ",type(c))    # str
# Converting int to float
a = float(a)
# Converting float to int
b = int(b)
# Converting str to int
c = int(c)
print("After Type Conversion : ")
print("Type of a is : ",type(a))    # float
print("Type of b is : ",type(b))   # int
print("Type of c is : ",type(c))    # int