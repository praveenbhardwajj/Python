def Find_word_at_Line():
    word="learssing"
    data=True
    line_no=1
    with open("Day7 File IO in Python/Demo.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1
    return -1

print(Find_word_at_Line())

        

        
    