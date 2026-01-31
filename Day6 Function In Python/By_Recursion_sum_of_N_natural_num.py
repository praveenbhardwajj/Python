
def recc(n):
    sum=0
    if(n==0):
        return 0
    else:
        return recc(n-1) + n
    

sum=recc(10)
print(sum)