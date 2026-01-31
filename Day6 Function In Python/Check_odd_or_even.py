def check_num_odd_even(num):
    if(num%2==0):
        return "EVEN"
    else:
        return "ODD"


num=int(input("Enetr number you want check : "))
ans=check_num_odd_even(num)
print(ans)
