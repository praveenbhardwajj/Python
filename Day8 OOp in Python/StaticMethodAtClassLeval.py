# class Student:
#     @staticmethod   
#     def college():
#         print("Bansal College")

#Student().college()



#explaination of static method
# static method is a method which is bound to the class and not the object of the class
# it can be called without creating an instance of the class
# it is defined using the @staticmethod decorator
class Student:
    @staticmethod   
    def college():
        print("Bansal College")
Student().college()

