recordFile = open("file.dat", "r")
First = []
Last = []
Math = []
English = []
Science = []
Computer = []

while True:
    text = recordFile.readline()
    if text == "":
        break
    if text[0:2] == "Fi":    
        First.append(text[text.find("-")+1:-1])
    if text[0:2] == "La":    
        Last.append(text[text.find("-")+1:-1])
    if text[0:2] == "Ma":    
        Last.append(text[text.find("-")+1:-1])
    if text[0:2] == "Sc":    
        Last.append(text[text.find("-")+1:-1])    age.append(int(text[text.find("1"):-1]))
numFile.close()

for ages in age:
    total += ages

average = total / len(age)
print ("Average of Ages")
print ("---------------")

for pos in range(len(age)):
    print ("Name: %s\tAge: %i" % (names[pos], age[pos]))
    
print ("The Average of all the ages is approximately %.1f years." % (average))