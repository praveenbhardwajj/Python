#funaction defination
def cal_sum(a,b): #function with parameter
    sum=a+b
    # print(sum)
    return sum # return sum

# cal_sum(10,20)
# cal_sum(10,10)
# cal_sum(10,40)


 #store in variable
# ans=cal_sum(20,20) # function call ; with argument
# print(ans)


#function without parameter

# def hello_print():
#     print("hello")

# hello_print()
# hello_print()
# output=hello_print()
# print(output)


#avg of three number
def cal_avg(a,b,c):
    avg=(a+b+c)/3
    return avg

ans=cal_avg(98,99,96)
print(ans)