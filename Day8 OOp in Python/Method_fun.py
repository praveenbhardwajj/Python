# class Greetings:
#     def __init__(self,name):
#         self.name=name
    
#     def Hello(self):
#         print("Hello , You are Amazing..",self.name)
    
# g1=Greetings("Praveen")
# g1.Hello()


class Cal:
    def Add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        sum=num1+num2
        return sum
    def Sub(self,num1,num2):
        self.num1=num1
        self.num2=num2
        subtraction=num1-num2
        return subtraction
    def Mul(self,num1,num2):
        self.num1=num1
        self.num2=num2
        Multi=num1*num2
        return Multi
    def Division(self,num1,num2):
        self.num1=num1
        self.num2=num2
        Divi=num1/num2
        return Divi

c1=Cal()

print("Press 0 For Exit..\nPress 1 For Addition..\nPress 2 For Subtraction..\nPress 3 For Multiplication..\nPress 4 For Division..")

choise=int(input("Enetr your Choise.."))
print("")
if(choise==1):
    print("<==== You Choise Is Addition ====>")
    print("")
    num1=int(input("Enetr Your 1st Non Zero number.."))
    print("")
    num2=int(input("Enetr Your 2nd Non Zero number.."))
    print("")
    addIs=c1.Add(num1,num2)
    print("Your Addition is = ", addIs)
elif(choise==2):
    print("<==== You Choise Is Subtration ====>")
    print("")
    num1=int(input("Enetr Your 1st Non Zero number.."))
    print("")
    num2=int(input("Enetr Your 2nd Non Zero number.."))
    print("")
    subIs=c1.Sub(num1,num2)
    print("Your Addition is = ", subIs)
elif(choise==3):
    print("<==== You Choise Is Subtration ====>")
    print("")
    num1=int(input("Enetr Your 1st Non Zero number.."))
    print("")
    num2=int(input("Enetr Your 2nd Non Zero number.."))
    print("")
    mulIs=c1.Mul(num1,num2)
    print("Your Addition is = ", mulIs)
elif(choise==4):
    print("<==== You Choise Is Subtration ====>")
    print("")
    num1=int(input("Enetr Your 1st Non Zero number.."))
    print("")
    num2=int(input("Enetr Your 2nd Non Zero number.."))
    print("")
    divIs=c1.Division(num1,num2)
    print("Your Addition is = ", divIs)
else:
    print("Choise Bitween.. \nPress 1 For Addition..\nPress 2 For Subtraction..\nPress 3 For Multiplication..\nPress 4 For Division. ")