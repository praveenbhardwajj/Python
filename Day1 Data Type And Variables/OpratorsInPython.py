# Assigenmet Operators


"""
a = 10
b = 2
print("This is assignment (=) operator, holds right side value to left side variable")
print("a = ",a)
print("b = ",b)


name="Praveen"
age=21
price=24.44

print("find type of variable using type() function")
print("Type of name is : ",type(name))
print("Type of age is : ",type(age))
print("Type of price is : ",type(price))

"""

#Operators in Python

#1 Arithmetic Operators
a = 10
b = 2
'''''
print (a+b) # Addition
print (a-b) # Subtraction           
print (a*b) # Multiplication
print (a/b) # Division
print (a%b) # Modulus
print (a**b) # Exponentiation


#2 Relational Operators
print ("1 =",a==b)  # Equal to    
print ("2 =",a!=b)  # Not Equal to
print ("3 =",a>b)   # Greater than
print ("4 =",a<b)   # Less than
print ("5 =",a>=b)  # Greater than or equal to
print ("6 =",a<=b)  # Less than or equal to


#3 Assigenmet Operator
a+=5  # a = a + 5
print(a)
a*=2  # a = a * 2
print(a)
a-=4  # a = a - 4
print(a)        
a/=2  # a = a / 2
print(a)
a%=3  # a = a % 3
print(a) #1
a**=2  # a = a ** 2
print(a)


#4 Logical Operators

# print( not True )  # False
# print( not False ) # True

# print( not (a >b))   # (a >b) is True so, not of true is False
val1=True
val2=False  
print( "And Oprator =",val1 and val2 )  # True and False = False, both values should be True to return True
print( "Or Oprator =",val1 or val2 )  # one value should be True to return True,if both are False then return False


#5 Membership Operators
str="Hello, Welcome to Python Programming"  
print( 'Welcome' in str )  # True
print( 'welcome' not in str )  # True


#6 Identity Operators
x=5 


y=5
print( x is y )  # True , because both have same identity and identities means memory location
print( x is not y )  # False , because both have same identity and identities means memory location


a=[1,2,3]
b=a
print( a is b )  # True , because both have same identity , arrray 'b' is pointing to array 'a'

print( a is not b )  # False , because both have same identity



'''''




