dictFile = open("dict.txt", "r")
dictionary = []
words = []
repetition = []
sortednum = []
count = 0
loop = 0

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
print ("Did you mean one of these?")
for prediction in words:
    if prediction[0:len(letter)] == letter:
        print ("%s (Repeated %i times.)" % (prediction,repetition[loop]))
    loop += 1
        

        
    
        

    
