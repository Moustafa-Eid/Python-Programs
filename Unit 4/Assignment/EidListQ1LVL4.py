dictFile = open("dict.txt", "r")
dictionary = []
words = []
repetition = []
sortednum = []
letterList = []
numberList = []
sortednumberList = []
count = 0
loop = 0
pos = 0
run = 0

while True:
    text = dictFile.readline()
    if text == "":
        break
    dictionary.append(text[:-1]) 
dictFile.close()

for text in dictionary:
    if text not in words:
        words.append(text)

for text in words:
    for nums in dictionary:
        if text == nums:
            count += 1
    repetition.append(count)
    sortednum.append(count)    
    count = 0
sortednum.sort()



letter = input("Please enter the first letters from a word: ").lower()
for prediction in words:
    if prediction[0:len(letter)] == letter:
        letterList.append(prediction)
        numberList.append(repetition[loop])
        sortednumberList.append(repetition[loop])
    loop += 1
sortednumberList.sort()
if len(letterList) >= 1:
    top1 = sortednumberList[len(sortednumberList)-1]
if len(letterList) >= 2:
    top2 = sortednumberList[len(sortednumberList)-2]
if len(letterList) >= 3:
    top3 = sortednumberList[len(sortednumberList)-3]
if len(letterList) == 0:
    print ("Sorry the dictionary does not contain a word that starts with these letters")
if len(letterList) >= 1:
    for top in numberList:
        if top == top1:
            repeat1 = top
            pos1 = pos
            break
        pos += 1
    pos = 0    
if len(letterList) >= 2:
    if top1 != top2:
        for top in numberList:
            if top == top1:
                repeat1 = top
                pos1 = pos
                break
            pos += 1
        pos = 0   
        for top in numberList:
            if top == top2:
                if top != repeat1:
                    repeat2 = top
                    pos2 = pos
                    break
            pos += 1
        pos = 0
        run = 0
    elif top1 == top2:
        for top in numberList:
            if top == top1:
                repeat1 = top
                pos1 = pos
                break
            pos += 1
        pos = 0   
        for top in numberList:
            if top == top2:
                run += 1
                if run == 2:
                    repeat2 = top
                    pos2 = pos
                    break
            pos += 1
        pos = 0
        run = 0        
if len(letterList) >= 3: 
    if top1 != top2 and top1 != top3 and top2 != top3:
        for top in numberList:
            if top == top1:
                repeat1 = top
                pos1 = pos
                break
            pos += 1
        pos = 0   
        for top in numberList:
            if top == top2:
                if top != repeat1:
                    repeat2 = top
                    pos2 = pos
                    break
            pos += 1
        pos = 0
        run = 0
        for top in numberList:
            if top == top3:
                if top != repeat2 and top != repeat1:        
                    repeat3 = top
                    pos3 = pos
                    break
            pos += 1
    elif top1 == top2 and top1 == top3:
        for top in numberList:
            if top == top1:
                repeat1 = top
                pos1 = pos
                break
            pos += 1
        pos = 0   
        for top in numberList:
            if top == top2:
                run += 1
                if run == 2:
                    repeat2 = top
                    pos2 = pos
                    break
            pos += 1
        pos = 0
        run = 0
        for top in numberList:
            if top == top3:
                run += 1
                if run == 3:
                    repeat3 = top
                    pos3 = pos
                    break
            pos += 1
    elif top1 == top2 and top1 != top3:
        for top in numberList:
            if top == top1:
                repeat1 = top
                pos1 = pos
                break
            pos += 1
        pos = 0   
        for top in numberList:
            if top == top2:
                run += 1
                if run == 2:
                    repeat2 = top
                    pos2 = pos
                    break
            pos += 1
        pos = 0
        run = 0
        for top in numberList:
            if top == top3:
                if top != repeat2 and top != repeat1:        
                    repeat3 = top
                    pos3 = pos
                    break
            pos += 1
    elif top1 != top2 and top1 == top3:
        for top in numberList:
            if top == top1:
                repeat1 = top
                pos1 = pos
                break
            pos += 1
        pos = 0
        for top in numberList:
            if top == top2:
                run += 1
                if run == 2:
                    repeat2 = top
                    pos2 = pos
                    break
            pos += 1
        pos = 0
        run = 0
        for top in numberList:
            if top == top3:
                if top != repeat2 and top != repeat1:        
                    repeat3 = top
                    pos3 = pos
                    break
            pos += 1
    elif top1 != top2 and top1 != top3 and top2 == top3:
        for top in numberList:
            if top == top1:
                repeat1 = top
                pos1 = pos
                break
            pos += 1
        pos = 0
        for top in numberList:
            if top == top2:
                run += 1
                if run == 2:
                    repeat2 = top
                    pos2 = pos
                    break
            pos += 1
        pos = 0
        run = 0
        for top in numberList:
            if top == top3:
                #run += 1
                #if run == 3:
                repeat3 = top
                pos3 = pos
                break
            pos += 1
print (numberList)

    
if len(letterList) > 0:    
    print ("Did you mean on of these words?")
if len(letterList) >= 1:
    print ("%s (repeated %i times)" % (letterList[pos1],repeat1))
if len(letterList) >= 2:
    print ("%s (repeated %i times)" % (letterList[pos2],repeat2))
if len(letterList) >= 3:
    print ("%s (repeated %i times)" % (letterList[pos3],repeat3))
