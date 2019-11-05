#Reading a file
dictionary = open("dict.txt", "r")
word = []
finalword = []
wordcount = []
finalwordcount = []
sortedcount = []
repeat = 0
quit = False

userword = input("Please enter a letter: ")

while True:
    text = dictionary.readline()
    if text == "":
        break    
    word.append(text[:-1])
    
for counting in range (0,len(word)):
    if word[counting][0:len(userword)] == userword:
        
        if word[counting] not in finalword:
            finalword.append(word[counting])
             
            finalwordcount.append(word.count(word[counting]))
            sortedcount.append(word.count(word[counting]))
            sortedcount.sort(reverse=True)          
            del sortedcount [3:len(sortedcount)]






if len(finalwordcount) == 1:
    index1 = finalwordcount.index (sortedcount[0])

if len(finalwordcount) == 2:
    index1 = finalwordcount.index (sortedcount[0])
    for check2 in finalwordcount:
        for r2 in range(1,2):
            if check2 != index1:
                sort2 = sortedcount[r2]            
                if check2 == sort2:
                    index2 = repeat
                    break
        repeat +=1
    repeat = 0    

if len(finalwordcount) >= 3:
    index1 = finalwordcount.index (sortedcount[0])
    
    for check2 in finalwordcount:
        for r2 in range(1,2):
            if check2 != index1:
                sort2 = sortedcount[r2]            
                if check2 == sort2:
                    index2 = repeat
                    quit = True
                    break
        if quit == True:
            break
        repeat +=1
    repeat = 0
    
    for check3 in finalwordcount:
        for r3 in range(2,3):
            if check3 != index1 and check3 != index2:
                sort3 = sortedcount[r3]            
                if check3 == sort3:
                    index3 = repeat
                    break
        repeat +=1
    repeat = 0        
        
     
     
        
print (sortedcount, finalwordcount, finalword)
if len(finalwordcount) >= 1:
    print (finalword[index1],sortedcount[0])
    print (index1)    
if len(finalwordcount) >= 2:
    print (finalword[index2],sortedcount[1])
    print (index2)    
if len(finalwordcount) >= 3:   
    print (finalword[index3],sortedcount[2])
    print (index3)
    



