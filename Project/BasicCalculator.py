
class Cal:
    def Add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        sum=num1+num2
        return print("Your Addition is :  ","(",num1,"+",num2, ")" ," = ", sum)
    def Sub(self,num1,num2):
        self.num1=num1
        self.num2=num2
        subtraction=num1-num2
        return  print("Your Subtraction is : ","(",num1," - ",num2, ")" ," = ",   subtraction)
    def Mul(self,num1,num2):
        self.num1=num1
        self.num2=num2
        Multi=num1*num2
        return  print("Your Addition is :  ","(",num1," x ",num2, ")" ," = ",  Multi)
    def Division(self,num1,num2):
        self.num1=num1
        self.num2=num2
        if(num1==0 or num2==0 ):
           return print("Can't divied by zero \nchoise non zero number Please !")
        Divi=num1/num2
        return print("Your Addition is :  ","(",num1," / ",num2, ")" ," = ",  Divi)
    def findTable(self,num):
       
       for i in range (1,11):
          print(num, " x ",i, " = ", num * i)

c1=Cal()

while True:
 print("")
 print("Press 0 For Exit..\nPress 1 For Addition..\nPress 2 For Subtraction..\nPress 3 For Multiplication..\nPress 4 For Division..\nPress 5 For Table..")

 choise=int(input("Enetr your Choise.."))
 print("")
 if(choise==0):
    print("Exiting From Calculator")
    break
    
 if(choise==1):
    print("<==== Your Choise Is Addition ====>")
    print("")
    num1=int(input("Enetr Your 1st Non Zero number.."))
    print("")
    num2=int(input("Enetr Your 2nd Non Zero number.."))
    print("")
    c1.Add(num1,num2)
    # addIs=c1.Add(num1,num2)
    # print("Your Addition is :  ","(",num1,"+",num2, ")" ," = ", addIs)
 elif(choise==2):
    print("<==== Your Choise Is Subtration ====>")
    print("")
    num1=int(input("Enetr Your 1st Non Zero number.."))
    print("")
    num2=int(input("Enetr Your 2nd Non Zero number.."))
    print("")
    c1.Sub(num1,num2)
    # subIs=c1.Sub(num1,num2)
    # print("Your Subtraction is : ","(",num1," - ",num2, ")" ," = ",   subIs)
 elif(choise==3):
    print("<==== Your Choise Is Multiplication ====>")
    print("")
    num1=int(input("Enetr Your 1st Non Zero number.."))
    print("")
    num2=int(input("Enetr Your 2nd Non Zero number.."))
    print("")
    c1.Mul(num1,num2)
    # mulIs=c1.Mul(num1,num2)
    # print("Your Addition is :  ","(",num1," x ",num2, ")" ," = ",  mulIs)
 elif(choise==4):
    print("<==== Your Choise Is Division ====>")
    print("")
    num1=int(input("Enetr Your 1st Non Zero number.."))
    print("")
    num2=int(input("Enetr Your 2nd Non Zero number.."))
    print("")
    c1.Division(num1,num2)
    # divIs=c1.Division(num1,num2)
    # print("Your Addition is :  ","(",num1," / ",num2, ")" ," = ",  divIs)
 elif(choise==5):
    print("<==== Your Choise Is Find Table ====>")
    print("")
    num1=int(input("Enetr Your Non Zero number For which want you table.."))
    print("")
    c1.findTable(num1)
    
 else:
    print("")
    print("Choise Bitween.. \nPress 1 For Addition..\nPress 2 For Subtraction..\nPress 3 For Multiplication..\nPress 4 For Division.. \nPress 5 For Table..")