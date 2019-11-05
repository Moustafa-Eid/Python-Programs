sum = 0
count = 0
while (True):
    age = int(input("Type Ages of Everyone in your family: Type -1 to exit: "))    
    if age > 0:
        sum += age
        count += 1
    elif age == -1:
        break
    else:
        print ("Invalid Input")
average = sum / count
print (" The average age for a member in your family is %.1f years." % (average))

