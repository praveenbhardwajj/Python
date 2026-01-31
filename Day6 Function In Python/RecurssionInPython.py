def recc(n):
    if(n==0):
        return
    print(n)
    recc(n-1)

recc(10)