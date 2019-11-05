#Reading a file
dictionary = open("dict.txt", "r")
word = []
finalword = []
wordcount = []
finalwordcount = []
sortedcount = []
repeat = 0
start = 0
run = 0
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

#num1 = sortedcount [0]
#num2 = sortedcount [1]
#num3 = sortedcount [2]

if len(finalwordcount) == 1:
    index1 = finalwordcount.index (sortedcount[0])

if len(finalwordcount) == 2:
    num1 = sortedcount [0]
    num2 = sortedcount [1]
    #num3 = sortedcount [2]    
    if num1 == num2:
        for check1 in finalwordcount:
            for r1 in range(1,2):
                sort1 = sortedcount[r1]            
                if check1 == sort1:
                    index1 = repeat
                    quit = True
                    break
            if quit == True:
                break
            repeat +=1
        repeat = 0     
        
        for check2 in finalwordcount:
            for r2 in range(1,2):
                if check2 != index1:
                    sort2 = sortedcount[r2]            
                    if check2 == sort2:
                        index2 = repeat
                        break
            repeat +=1
        repeat = 0
    elif num1 != num2:
        index1 = finalwordcount.index (sortedcount[0])
        index2 = finalwordcount.index (sortedcount[1])
        

if len(finalwordcount) >= 3:
    num1 = sortedcount [0]
    num2 = sortedcount [1]
    num3 = sortedcount [2]    
    if num1 == num2 and num2 == num3 and num1 == num3:
        for top in finalwordcount:
            if top == num1:
                repeat1 = top
                index1 = repeat
                break
            repeat+=1
        repeat = 0
        
        for top in finalwordcount:
            if top == num2:
                run +=1
                if run == 2:
                    repeat2 = top
                    index2 = repeat
                    break
                repeat += 1
            repeat = 0
            run = 0
            
        for top in finalwordcount:
            if top == num3:
                run +=1
                if run == 3:
                    repeat3 = top
                    index3 = repeat
                    break
                repeat += 1
            repeat = 0
            run = 0        
        
                
                
            
        
                
        
    elif num1 != num2 and num1 != num3:
        index1 = finalwordcount.index (sortedcount[0])
        index2 = finalwordcount.index (sortedcount[1])        
        index3 = finalwordcount.index (sortedcount[2]) 
    
    elif num1 != num2 and num1 == num3 and num3 != num2:
        for check1 in finalwordcount:
            for r1 in range(1,2):
                sort1 = sortedcount[r1]            
                if check1 == sort1:
                    index1 = repeat
                    #quit = True
                    break
            #if quit == True:
                #break
            repeat +=1
        repeat = 0   
        
        quit = False
        index2 = finalwordcount.index (sortedcount[1]) 
        
        for check3 in finalwordcount:
            for r3 in range(2,3):
                if check3 != index1 and check3 != index2:
                    sort3 = sortedcount[r3]            
                    if check3 == sort3:
                        index3 = repeat
                        #quit = True
                        break
            #if quit == True:
                #break
            repeat +=1
        repeat = 0 
        
    elif num1 == num2 and num1 != num3 and num2!=num3:
        for check1 in finalwordcount:
            for r1 in range(1,2):
                sort1 = sortedcount[r1]            
                if check1 == sort1:
                    index1 = repeat
                    quit = True
                    break
            if quit == True:
                break
            repeat +=1
        repeat = 0 
        quit = False
        
        for check2 in finalwordcount:
            for r2 in range(1,2):
                if check2 != index1:
                    sort2 = sortedcount[r2]            
                    if check2 == sort2:
                        index2 = repeat
                        #quit = True
                        break
            #if quit == True:
                #break
            repeat +=1
        repeat = 0     
        
        index3 = finalwordcount.index (sortedcount[2])
        
    elif num2 == num3 and num1!= num2 and num1!= num3:
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
        #quit = False
        
        for check3 in finalwordcount:
            for r3 in range(2,3):
                if check3 != index1 and check3 != index2:
                    sort3 = sortedcount[r3]            
                    if check3 == sort3:
                        index3 = repeat
                        #quit = True
                        break
            #if quit == True:
                #break
            repeat +=1
        repeat = 0        
         
print (sortedcount, finalwordcount, finalword)
#if num1 == num2 and num1 == num3:
    #print (finalword[index1],repeat1)
    #print (finalword[index2],repeat2)
    #print (finalword[index3],repeat3)
#else:
    
if len(finalwordcount) >= 1:
    print (finalword[index1],sortedcount[0])
    print (index1)    
if len(finalwordcount) >= 2:
    print (finalword[index2],sortedcount[1])
    print (index2)    
if len(finalwordcount) >= 3:   
    print (finalword[index3],sortedcount[2])
    print (index3)