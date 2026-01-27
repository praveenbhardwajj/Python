tup=[1,2,4,9,16,25,36,49,64,81,100]
x=int(input("Enetr number you want search "))
i=0
flag=False
while (i<len(tup)):
    if(tup[i]==x):
       flag=True
    i+=1
if(flag==True):
     print("element found")
else:
    print("element No found")