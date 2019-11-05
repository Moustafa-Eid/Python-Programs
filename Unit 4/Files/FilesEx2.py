numFile = open("ages.txt", "r")
names = []
age = []
total = 0
while True:
    text = numFile.readline()
    if text == "":
        break
    names.append(text[:text.find(" ")])
    age.append(int(text[text.find("1"):-1]))
numFile.close()

for ages in age:
    total += ages

average = total / len(age)
print ("Average of Ages")
print ("---------------")

for pos in range(len(age)):
    print ("Name: %s\tAge: %i" % (names[pos], age[pos]))
    
print ("The Average of all the ages is approximately %.1f years." % (average))