string = ""
start = 15

for count in range(3):
    for number in range(4):       
        string += str(start)+ " "
        start += 1
    print (string)
    start+=6
    string = ""
        

    