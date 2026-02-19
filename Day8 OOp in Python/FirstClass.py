#first class in oops in python
# class Student:
#     name="Praveen Bhardwaj"

# #object creation

# s1=Student()
# print(s1.name)


#<---------------------now look for constructor which is two types ---------------------------->
# class Student:
#     def __init__(self,name):
#         self.name=name

# #object creation

# s1=Student("Praveen")
# print(s1.name)
#<---------------------now look for method in class ---------------------------->

class Greet:
    def __init__(self,name):
        self.name=name

    def GreetMsg(self):
        print("Hello",self.name)

    
obj=Greet("Praveen")
obj.GreetMsg()
