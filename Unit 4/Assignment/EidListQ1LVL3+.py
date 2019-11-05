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



letter = input("Please enter the first letters from a word: ")
for prediction in words:
    if prediction[0:len(letter)] == letter:
        letterList.append(prediction)
        numberList.append(repetition[loop])
        sortednumberList.append(repetition[loop])
    loop += 1
sortednumberList.sort()

top1 = sortednumberList[len(sortednumberList)-1]
top2 = sortednumberList[len(sortednumberList)-2]
top3 = sortednumberList[len(sortednumberList)-3]

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

    
print ("Did you mean on of these words?")
if len(letterList) >= 1:
    print ("%s (repeated %i times)" % (letterList[pos1],repeat1))
if len(letterList) >= 2:
    print ("%s (repeated %i times)" % (letterList[pos2],repeat2))
if len(letterList) >= 3:
    print ("%s (repeated %i times)" % (letterList[pos3],repeat3))

