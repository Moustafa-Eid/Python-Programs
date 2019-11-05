num = int(input("Enter a number: "))

odd = 1
total = 0
last = 0
add = ""

for sequence in range(1,num+1):
    for times in range (sequence):
        total += odd
        add += str(odd) + " + " 
        odd += 2
    print ("%i^3 = %s = %i" % (sequence,add[0:len(add)-3],total))
    total = 0
    add = ""
    
    
