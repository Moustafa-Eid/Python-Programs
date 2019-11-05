import random
dictFile = open("random.txt", "r")
dictionary = []

while True:
    text = dictFile.readline()
    if text == "":
        break
    dictionary.append(text[:-1]) 
dictFile.close()

for repeat in range(500):
    pos = random.randint(0,999)
    word = dictionary[pos]
    print (word)
    dictionary.append(word)
    
    
