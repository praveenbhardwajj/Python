num=int(input("enetr number = "))

def Cal_fact(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(fact) 
Cal_fact(num)

