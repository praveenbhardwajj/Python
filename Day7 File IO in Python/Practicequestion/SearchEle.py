with open("Day7 File IO in Python/Demo.txt","r") as f:
    data=f.read()
    if(data.find("learing")!=-1):
        print("Found")
    else:
        print("Not found")

    