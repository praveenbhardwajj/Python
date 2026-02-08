# create file with some data

# with open("Day7 File IO in Python/Practicequestion/practice.txt","w") as f:
#     f.write("Hi everyone \n we are learning Python and file I/O \n uaing java. \n I like programming in python .")




# replace some specific data

with open("Day7 File IO in Python/Practicequestion/practice.txt","r") as f:
    data=f.read()
new_data=data.replace("java","Python")
# print(new_data)


with open("Day7 File IO in Python/Practicequestion/practice.txt","w") as f:
 f.write(new_data)
 print(new_data)